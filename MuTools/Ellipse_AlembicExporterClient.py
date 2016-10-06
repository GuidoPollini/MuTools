__version__ = '1.0.3'


import MuTools.MuUtils   as Utils
import MuTools.MuCore    as Core
import MuTools.MuScene   as Scene


import maya.cmds     as MC
import maya.mel      as MM
import maya.OpenMaya as OM

import time
import os


"""
import os
muPath = r"C:\Users\guido.pollini\Desktop\MuTools"
if muPath not in os.sys.path:
    os.sys.path.append(muPath)


import MuTools.MuUtils as Utils
reload(Utils)

import MuTools.Ellipse_AlembicExporterClient as AEC
Utils.muReload(AEC)

AEC.spawnRemoteMaya()
"""







#------------------------------------------------------------------------------
# Initialize module
#------------------------------------------------------------------------------
# Loading message
Utils.moduleLoadingMessage()
# Log
log       = Utils.Log('sceneCorrectorLog', Utils.Log.STANDARD)
debug     = log.debug
hardDebug = log.hardDebug







log('--------------------------', 
    '\n    SCENE CORRECTOR', 
    '\n--------------------------')


















def exocortexAlembicExport(nodeList, targetPath, purePointCache):
    """
    Exocortex syntax:
      uvs=1;withouthierarchy=0;normals=1;transformcache=0;globalspace=0;substep=1;
      filename=TARGETPATH;step=1;objects=NODE0,NODE1,NODE2:hands;useInitShadGrp=0;in=101.0;
      purepointcache=0;ogawa=1;dynamictopology=0;facesets=1;out=239.0;
    """

    #nodes          = ['ch_litth:mane','ch_litth:body']
    #path           = 'Y:/01_SAISON_4/07_WIP/3D/__DEBUG_PROD/ALEMBIC/cloud.abc'
    animStartTime  = MC.playbackOptions(query=True, animationStartTime=True)
    animEndTime    = MC.playbackOptions(query=True, animationEndTime=True)
    #purePointCache = 1 # 1->pointCache, 0->wholeMesh
       
    nodeListString = ','.join(nodeList) # [a, b, ...] --> a,b,...
    
    # Preset for "surface & normals" (saves the whole mesh data, i.e. vertices/edges/faces)
    exoAttrs = {'ogawa':            1,
                'objects':          nodeListString,
                'filename':         targetPath,

                'in':               animStartTime,
                'out':              animEndTime,
                'step':             1,
                'substep':          1,
                  
                'purepointcache':   0, # Stores or not edge/face data
                'normals':          1,
                'uvs':              1,
                'facesets':         1, # Face objectSets
                
                'useInitShadGrp':   0, # Per-face shading

                'globalspace':      0, # Apply the transformation to the mesh
                'withouthierarchy': 0,
                'transformcache':   0, # Save only transform data
                'dynamictopology':  0, # Not for a basic mesh                                   
    }
        
    if purePointCache == True:
        # Saves only vertex positions (no edge/face data)
        exoAttrs['purepointcache'] = 1
        exoAttrs['normals']        = 0
        exoAttrs['uvs']            = 0
        exoAttrs['facesets']       = 0
    
    exocortexCommand = ''
    for attr in exoAttrs:
        exocortexCommand += '{0}={1};'.format(attr, exoAttrs[attr])    
    
    try:
        MC.ExocortexAlembic_export(j=exocortexCommand)
        print '[Exocortex] SUCCESS: alembic saved to "{0}"!'.format(targetPath)
    except Exception as exc:
        print '[Exocortex] FATALITY: command failed!'
        raise
        #MC.error('Exocortex command failed!\nCommand: {0}\nReason: {1}\n'.format(exocortexCommand, exc))


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
NAMESPACE SHIT
 
 - WARNING: i cazzari possono aver importato un file senza namespace ma con PREFIX
   ... si comporta come un fakeNamespace e anche se obsolete mettilo in conto
   credo sia modificabile solo con file... spero
 
 *** attento perche viene indicato come NAMESPACE nel getReferenceData

 NON RIESCO A MODIFICARLO..; per il momentoignoralo perche forse e infattibile (senza complicarsi la vita)
 (anche un cambio di prefix non funziona e non puoi attribuirgli un nuovo namespace)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""










ASSETS_PATH    = 'Y:/01_SAISON_4/08_ASSETS/3D/'
ANIMATION_PATH = 'Y:/01_SAISON_4/05_UTILE/Rendu/13_REMOTE_MAYA/'





#==============================================================================
#------------------------------------------------------------------------------
# 'Core.Reference' monkey patching
#
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" 
The module with the monkey patching MUST be the last oneto be reloaded; otherwise
a reload of 'MuCore' will rebuild the class 'Reference' and the patch will be lost!
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
#------------------------------------------------------------------------------
#==============================================================================
def _yakariTag(self):
    yakariTags = ['ch', 'pr', 'st', 'ss']
    
    # Recover the 'asset type'
    assetTag = None

    for tag in yakariTags:
        if self.originalName().startswith(tag + '_'):
            assetTag = tag

    # The camera is not a Shotgun asset        
    if self.originalName() == 'yak_camera':
        assetTag = 'cam'    
        
    return assetTag  

Core.Reference.yakariTag = _yakariTag

"""
@property
def renderSet(self):
    if self.namespace is None:
        # A shitty prefix; fatal...
        return None
    potentialRenderSet = self.namespace + ':RenderSet'
    if not (MC.objExists(potentialRenderSet) and MC.nodeType(potentialRenderSet) == 'objectSet'):
        return None    
    
    return potentialRenderSet
"""
#------------------------------------------------------------------------------







def run(*args):

    # Predefined asset folders; they must exist and be worldChildren:
    assetFolderNames = {'cam': '__CAMERA__', 
                        'ch':  '__CHARS__', 
                        'pr':  '__PROPS__', 
                        'st':  '__SET__', 
                        'ss':  '__SUBSET__'
    }

    for folderName in assetFolderNames.values():
        if not Scene.nodeExists(folderName):
            MC.error('MISSING FOLDER: {} doesn\'t exist'.format(folderName))
        
        if Scene.parent(folderName):
            MC.error('MISPLACED FOLDER: {} must be a worldChild!'.format(folderName))





    # ...
    prefixedReferences = []
    toDoReferences     = []

    properTransforms   = []
    badTransforms      = []



    #===========================================================================================================
    #-----------------------------------------------------------------------------------------------------------
    # FIRST PASS
    #
    # - Shotgun published assets
    # 
    #-----------------------------------------------------------------------------------------------------------    
    #===========================================================================================================

    # File references
    references = Scene.references()
    log('References:', references)


    for ref in references:

        if ref.namespace() is None:
            # Skip reference with prefixes... It's a FATALITY
            prefixedReferences.append(ref.filePath())
            continue
        

        #print
        #print 
        #print 'Working on "{0}" ({1} {2})'.format(ref.namespace, ref.originalName, ref.category)
        
        """
        print 
        print ref.filePath
        print ref.cleanFilePath
        print ref.namespace
        print ref.referenceNode
        print ref.originalName
        print ref.category
        print ref.isBroken
        print ref.renderSet
        continue 
        """


        """""""""""""""""""""""""""""""""""""""
        ROOTS
          cam     --> camera_rig
          ch      --> rig_group
          pr      --> rig_group
          ss      --> rig_group (if published)
          st      --> NO ROOT 
          unknown --> UNKNOWN
        """""""""""""""""""""""""""""""""""""""





        #--------------------------------------------------------------------------------------------------------------
        # CH PR SS(published) CAM
        #-------------------------------------------------------------------------------------------------------------- 
        # All 'ch', 'pr'(published) and 'ss', 'cam' setups have a transform root 
        # and every other transform is inside it.
        
        yakariTag = ref.yakariTag()

        if yakariTag in ['ch', 'pr', 'ss', 'cam']:
            try:
                rootTransformName = str(ref.namespace()) + (':camera_rig' if yakariTag == 'cam' else ':rig_group')
                rootTransform = Core.MuNode(rootTransformName) 
            except Core.NameFatality:
                raise


            parent = rootTransform.parent()
            
            if parent.name() == assetFolderNames[yakariTag]:
                properTransforms.append(rootTransform)
                #print '[OK] It\'s inside "{}"!'.format(parent)        
            else:                
                badTransforms.append(rootTransform)
                #print '[BAD] It\'s inside "{}"!'.format(parent if parent is not None else '__world__')





        #--------------------------------------------------------------------------------------------------------------
        # ST
        #--------------------------------------------------------------------------------------------------------------                
        # 'st' assets have not necessarily a rootTransform, but a list of <locators> holding meshes.

        elif yakariTag == 'st':
            """ DEVO RECUPERARE ANCHE LE PLACCHE NON REFERENCED? le ..._COPY? sono nel renderset"""

            nodes = ref.namespace().nodes()

            # Filter 'locatorTransforms' only:
            locators = [x for x in nodes if x.isLocatorTransform()]

            for locator in locators:
                parent = locator.parent()

                if parent and parent.name() == '__SET__':
                    # Ok, it's inside '__SET__'
                    properTransforms.append(locator)
                    #print '[OK] It\'s inside "{}"!'.format(parent)  

                else:
                    # Bad: worldChild or badly parented
                    badTransforms.append(locator)
                    #print '[BAD] It\'s inside "{}"!'.format(parent if parent is not None else '__world__')





        #--------------------------------------------------------------------------------------------------------------
        # UNKNOWN
        #--------------------------------------------------------------------------------------------------------------                
        # Referenced files without a proper tag; can't do anything!
        else:
            toDoReferences.append(ref)





    #===========================================================================================================
    #-----------------------------------------------------------------------------------------------------------
    # SECOND PASS
    #
    # - Trying to recover some kind of SS structure
    # - Detect the roots of 'stray meshes' and put them together
    #   by creating the most evident hierarchy possible
    #   (i.e. by going back until one finds the world or the common assetFolders)
    #-----------------------------------------------------------------------------------------------------------    
    #===========================================================================================================   
    
    irrelevantTransforms     = Core.Set('persp', 'top', 'front', 'side', 'front', 'platesHolder')
    transformsToSkip         = Core.Set(properTransforms) | Core.Set(badTransforms) | irrelevantTransforms
    worldTransformsToAnalyze = Core.Set(Scene.worldChildren()) - transformsToSkip
    


    # Transforms potentially holding an SS: 
    # - put them into a proper namespace ("ss_XXXX", only the "ss_" tag matters);
    # - reparent them to the folder "__SET__". 
    rootTransforms = Core.Set()


    def analyzeChildren(actualTrans, depth=0):
        if actualTrans.isMeshTransform():
            #    |fakeParent|pascal:G2|pascal:G1|pascal:GUIDO
            # fakeParent   pascal:G2   pascal:G1   pascal:GUIDO
            parentTags = actualTrans.longName().lstrip('|').split('|')

            if len(parentTags) == 1:
                # It's a world meshTransform
                rootTransforms.add(actualTrans)

            else:    
                rootParent = parentTags[0]
                if rootParent not in assetFolderNames.values():
                    rootTransforms.add(Core.MuNode(rootParent))
                else:
                    nextRootParent = Core.MuNode('|' + rootParent + '|' + parentTags[1])
                    rootTransforms.add(nextRootParent)    

        children = actualTrans.children(type='transform')
        for child in children:
            if child not in transformsToSkip:
                analyzeChildren(child, depth=depth + 1)

    for trans in worldTransformsToAnalyze:
        analyzeChildren(trans, depth=0)


    # Create a suitable 'renderSet'
    log.iterable(rootTransforms, 'ROOT TRANS')
    log.iterable(prefixedReferences, 'PREFIXED')
    log.iterable(properTransforms, 'PROPER')
    log.iterable(toDoReferences, 'UNKNOWN')
    log.iterable(badTransforms, 'BAD')
    log.iterable(Scene.namespaces(), 'SCENE NAMESPACES')

    """
    nodeList = ['ch_yakar:face']
    targetPath = 'Y:/01_SAISON_4/07_WIP/3D/__DEBUG_PROD/ALEMBIC/test.abc'
    purePointCache = False
    exocortexAlembicExport(nodeList, targetPath, purePointCache)
    """






import subprocess
import getpass
import os

def spawnRemoteMaya():
    actualEnv = os.environ.copy() # .copy() is a <dict> method for shallow copy
    

    #-----------------------------------------
    # Nullify custom vars ('delete' them?)
    #-----------------------------------------
    varToNullify = [
        "MAYADEV_APP_PATH", 
        "LOCAL_PATH", 
        "SERVER_PATH", 
        "PROMPT", 
        "MAYA_APP_PATH", 
        "MAYA_CUSTOM_TEMPLATE_PATH"
    ]
    for var in varToNullify:
        actualEnv[var] = ""
 


  
    #-----------------------------------------
    # Clean Maya vars
    #-----------------------------------------
    """    
    modifiedVars = {
        "MAYA_MODULE_PATH":           "C:/Program Files/Autodesk/Maya2015/modules;C:/Users/guido.pollini/Documents/maya/2015-x64/modules;C:/Users/guido.pollini/Documents/maya/modules;C:/Program Files/Common Files/Autodesk Shared/Modules/maya/2015",
        "PYTHONPATH":                 "C:/Program Files/Autodesk/Maya2015/plug-ins/bifrost/scripts/presets;C:/Program Files/Autodesk/Maya2015/plug-ins/bifrost/scripts;C:/ExocortexAlembic/Maya2015/Module/scripts;C:/Program Files/Autodesk/Maya2015/plug-ins/fbx/scripts;C:/Program Files/Autodesk/mentalrayForMaya2015/scripts/AETemplates;C:/Program Files/Autodesk/mentalrayForMaya2015/scripts/mentalray;C:/Program Files/Autodesk/mentalrayForMaya2015/scripts/unsupported;C:/Program Files/Autodesk/mentalrayForMaya2015/scripts;C:/Program Files/Autodesk/Maya2015/plug-ins/substance/scripts;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/cafm;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/xmaya;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/brushes;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/dialogs;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/fxmodules;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/tabs;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/util;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/widgets;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts",
        "MAYA_PRESET_PATH":           "C:/Program Files/Autodesk/Maya2015/plug-ins/bifrost/presets;C:/ExocortexAlembic/Maya2015/Module/presets;C:/Program Files/Autodesk/Maya2015/plug-ins/fbx/presets;C:/Program Files/Autodesk/mentalrayForMaya2015/presets/attrPresets;C:/Program Files/Autodesk/mentalrayForMaya2015/presets/attrPresets/maya_bifrost_liquid;C:/Program Files/Autodesk/mentalrayForMaya2015/presets/attrPresets/mia_material;C:/Program Files/Autodesk/mentalrayForMaya2015/presets/attrPresets/mia_material_x;C:/Program Files/Autodesk/mentalrayForMaya2015/presets/attrPresets/mia_material_x_passes;C:/Program Files/Autodesk/mentalrayForMaya2015/presets;C:/Program Files/Autodesk/Maya2015/plug-ins/substance/presets;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/presets",
        "XBMLANGPATH":                "C:/Users/guido.pollini/Documents/maya/2015-x64/prefs/icons;C:/Users/guido.pollini/Documents/maya/prefs/icons;C:/ProgramData/Autodesk/maya/2015;C:/Program Files/Autodesk/Maya2015/icons;C:/Program Files/Autodesk/Maya2015/app-defaults;C:/Program Files/Autodesk/Maya2015/icons/paintEffects;C:/Program Files/Autodesk/Maya2015/icons/fluidEffects;C:/Program Files/Autodesk/Maya2015/icons/hair;C:/Program Files/Autodesk/Maya2015/icons/cloth;C:/Program Files/Autodesk/Maya2015/icons/live;C:/Program Files/Autodesk/Maya2015/icons/fur;C:/Program Files/Autodesk/Maya2015/icons/muscle;C:/Program Files/Autodesk/Maya2015/icons/turtle;C:/Program Files/Autodesk/Maya2015/icons/FBX;C:/Program Files/Autodesk/Maya2015/icons/mayaHIK;C:/Program Files/Autodesk/Maya2015/plug-ins/bifrost/icons;C:/ExocortexAlembic/Maya2015/Module/icons;C:/Program Files/Autodesk/Maya2015/plug-ins/fbx/icons;C:/Program Files/Autodesk/mentalrayForMaya2015/icons;C:/Program Files/Autodesk/Maya2015/plug-ins/substance/icons;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/icons",
        "MAYA_PLUG_IN_PATH":          "C:/Users/guido.pollini/Documents/maya/2015-x64/plug-ins;C:/Users/guido.pollini/Documents/maya/plug-ins;C:/Program Files/Autodesk/Maya2015/bin/plug-ins;C:/Program Files/Autodesk/Maya2015/plug-ins/bifrost/plug-ins;C:/ExocortexAlembic/Maya2015/Module/plug-ins;C:/Program Files/Autodesk/Maya2015/plug-ins/fbx/plug-ins;C:/Program Files/Autodesk/mentalrayForMaya2015/plug-ins;C:/Program Files/Autodesk/Maya2015/plug-ins/substance/plug-ins;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/plug-ins",
        "PATH":                       "C:/Program Files/Autodesk/Maya2015/bin/Cg;C:/Program Files/Autodesk/Maya2015/bin;C:/windows/system32;C:/windows;C:/windows/System32/Wbem;C:/windows/System32/WindowsPowerShell/v1.0/;C:/Program Files/Puppet Labs/Puppet/bin;C:/Program Files/Common Files/Autodesk Shared/;C:/Program Files (x86)/Autodesk/Backburner/;C:/Program Files (x86)/QuickTime/QTSystem/;C:/Program Files/TortoiseGit/bin;C:/Program Files (x86)/Skype/Phone/;C:/windows/system32/config/systemprofile/.dnx/bin;C:/Program Files/Microsoft DNX/Dnvm/;C:/Program Files/Microsoft SQL Server/130/Tools/Binn/;C:/Program Files/Microsoft SQL Server/120/Tools/Binn/;C:/Program Files (x86)/Windows Kits/10/Windows Performance Toolkit/;C:/Program Files/Microsoft SQL Server/110/Tools/Binn/;C:/Program Files (x86)/Microsoft SDKs/TypeScript/1.0/;C:/Users/guido.pollini/AppData/Local/Google/Chrome/Application;C:/windows/system32;C:/windows;C:/windows/System32/Wbem;C:/windows/System32/WindowsPowerShell/v1.0/;C:/Program Files/Puppet Labs/Puppet/bin;C:/Program Files/Common Files/Autodesk Shared/;C:/Program Files (x86)/Autodesk/Backburner/;C:/Program Files (x86)/QuickTime/QTSystem/;C:/wamp/bin/php/php5.6.15;C:/Program Files/Autodesk/Maya2015/plug-ins/bifrost/bin;C:/Program Files/Autodesk/mentalrayForMaya2015/bin;C:/Program Files/Autodesk/Maya2015/plug-ins/substance/bin;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/bin",
        "MAYA_SCRIPT_PATH":           "C:/Users/guido.pollini/Documents/maya/2015-x64/scripts;C:/Users/guido.pollini/Documents/maya/scripts;C:/Users/guido.pollini/Documents/maya/2015-x64/presets;C:/Users/guido.pollini/Documents/maya/2015-x64/prefs/shelves;C:/Users/guido.pollini/Documents/maya/2015-x64/prefs/markingMenus;C:/Users/guido.pollini/Documents/maya/2015-x64/prefs/scripts;C:/Program Files/Autodesk/Maya2015/scripts;C:/Program Files/Autodesk/Maya2015/scripts/startup;C:/Program Files/Autodesk/Maya2015/scripts/others;C:/Program Files/Autodesk/Maya2015/scripts/AETemplates;C:/Program Files/Autodesk/Maya2015/scripts/unsupported;C:/Program Files/Autodesk/Maya2015/scripts/paintEffects;C:/Program Files/Autodesk/Maya2015/scripts/fluidEffects;C:/Program Files/Autodesk/Maya2015/scripts/hair;C:/Program Files/Autodesk/Maya2015/scripts/cloth;C:/Program Files/Autodesk/Maya2015/scripts/live;C:/Program Files/Autodesk/Maya2015/scripts/fur;C:/Program Files/Autodesk/Maya2015/scripts/muscle;C:/Program Files/Autodesk/Maya2015/scripts/turtle;C:/Program Files/Autodesk/Maya2015/scripts/FBX;C:/Program Files/Autodesk/Maya2015/scripts/mayaHIK;C:/Program Files/Autodesk/Maya2015/plug-ins/bifrost/scripts/presets;C:/Program Files/Autodesk/Maya2015/plug-ins/bifrost/scripts;C:/ExocortexAlembic/Maya2015/Module/scripts;C:/Program Files/Autodesk/Maya2015/plug-ins/fbx/scripts;C:/Program Files/Autodesk/mentalrayForMaya2015/scripts/AETemplates;C:/Program Files/Autodesk/mentalrayForMaya2015/scripts/mentalray;C:/Program Files/Autodesk/mentalrayForMaya2015/scripts/unsupported;C:/Program Files/Autodesk/mentalrayForMaya2015/scripts;C:/Program Files/Autodesk/Maya2015/plug-ins/substance/scripts;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/cafm;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/xmaya;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/brushes;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/dialogs;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/fxmodules;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/tabs;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/util;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/widgets;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts",
        "MAYA_PLUG_IN_RESOURCE_PATH": "C:/Program Files/Autodesk/Maya2015/plug-ins/bifrost/resources;C:/ExocortexAlembic/Maya2015/Module/resources;C:/Program Files/Autodesk/Maya2015/plug-ins/fbx/resources;C:/Program Files/Autodesk/mentalrayForMaya2015/resources;C:/Program Files/Autodesk/Maya2015/plug-ins/substance/resources;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/resources"
    }
    """

    # I removed every reference to 'user'
    modifiedVars = {
        "MAYA_MODULE_PATH":           "C:/Program Files/Autodesk/Maya2015/modules;C:/Users/guido.pollini/Documents/maya/2015-x64/modules;C:/Users/guido.pollini/Documents/maya/modules;C:/Program Files/Common Files/Autodesk Shared/Modules/maya/2015",
        "PYTHONPATH":                 "C:/Program Files/Autodesk/Maya2015/plug-ins/bifrost/scripts/presets;C:/Program Files/Autodesk/Maya2015/plug-ins/bifrost/scripts;C:/ExocortexAlembic/Maya2015/Module/scripts;C:/Program Files/Autodesk/Maya2015/plug-ins/fbx/scripts;C:/Program Files/Autodesk/mentalrayForMaya2015/scripts/AETemplates;C:/Program Files/Autodesk/mentalrayForMaya2015/scripts/mentalray;C:/Program Files/Autodesk/mentalrayForMaya2015/scripts/unsupported;C:/Program Files/Autodesk/mentalrayForMaya2015/scripts;C:/Program Files/Autodesk/Maya2015/plug-ins/substance/scripts;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/cafm;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/xmaya;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/brushes;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/dialogs;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/fxmodules;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/tabs;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/util;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/widgets;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts",
        "MAYA_PRESET_PATH":           "C:/Program Files/Autodesk/Maya2015/plug-ins/bifrost/presets;C:/ExocortexAlembic/Maya2015/Module/presets;C:/Program Files/Autodesk/Maya2015/plug-ins/fbx/presets;C:/Program Files/Autodesk/mentalrayForMaya2015/presets/attrPresets;C:/Program Files/Autodesk/mentalrayForMaya2015/presets/attrPresets/maya_bifrost_liquid;C:/Program Files/Autodesk/mentalrayForMaya2015/presets/attrPresets/mia_material;C:/Program Files/Autodesk/mentalrayForMaya2015/presets/attrPresets/mia_material_x;C:/Program Files/Autodesk/mentalrayForMaya2015/presets/attrPresets/mia_material_x_passes;C:/Program Files/Autodesk/mentalrayForMaya2015/presets;C:/Program Files/Autodesk/Maya2015/plug-ins/substance/presets;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/presets",
        "XBMLANGPATH":                "C:/ProgramData/Autodesk/maya/2015;C:/Program Files/Autodesk/Maya2015/icons;C:/Program Files/Autodesk/Maya2015/app-defaults;C:/Program Files/Autodesk/Maya2015/icons/paintEffects;C:/Program Files/Autodesk/Maya2015/icons/fluidEffects;C:/Program Files/Autodesk/Maya2015/icons/hair;C:/Program Files/Autodesk/Maya2015/icons/cloth;C:/Program Files/Autodesk/Maya2015/icons/live;C:/Program Files/Autodesk/Maya2015/icons/fur;C:/Program Files/Autodesk/Maya2015/icons/muscle;C:/Program Files/Autodesk/Maya2015/icons/turtle;C:/Program Files/Autodesk/Maya2015/icons/FBX;C:/Program Files/Autodesk/Maya2015/icons/mayaHIK;C:/Program Files/Autodesk/Maya2015/plug-ins/bifrost/icons;C:/ExocortexAlembic/Maya2015/Module/icons;C:/Program Files/Autodesk/Maya2015/plug-ins/fbx/icons;C:/Program Files/Autodesk/mentalrayForMaya2015/icons;C:/Program Files/Autodesk/Maya2015/plug-ins/substance/icons;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/icons",
        "MAYA_PLUG_IN_PATH":          "C:/Program Files/Autodesk/Maya2015/bin/plug-ins;C:/Program Files/Autodesk/Maya2015/plug-ins/bifrost/plug-ins;C:/ExocortexAlembic/Maya2015/Module/plug-ins;C:/Program Files/Autodesk/Maya2015/plug-ins/fbx/plug-ins;C:/Program Files/Autodesk/mentalrayForMaya2015/plug-ins;C:/Program Files/Autodesk/Maya2015/plug-ins/substance/plug-ins;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/plug-ins",
        "PATH":                       "C:/Program Files/Autodesk/Maya2015/bin/Cg;C:/Program Files/Autodesk/Maya2015/bin;C:/windows/system32;C:/windows;C:/windows/System32/Wbem;C:/windows/System32/WindowsPowerShell/v1.0/;C:/Program Files/Puppet Labs/Puppet/bin;C:/Program Files/Common Files/Autodesk Shared/;C:/Program Files (x86)/Autodesk/Backburner/;C:/Program Files (x86)/QuickTime/QTSystem/;C:/Program Files/TortoiseGit/bin;C:/Program Files (x86)/Skype/Phone/;C:/windows/system32/config/systemprofile/.dnx/bin;C:/Program Files/Microsoft DNX/Dnvm/;C:/Program Files/Microsoft SQL Server/130/Tools/Binn/;C:/Program Files/Microsoft SQL Server/120/Tools/Binn/;C:/Program Files (x86)/Windows Kits/10/Windows Performance Toolkit/;C:/Program Files/Microsoft SQL Server/110/Tools/Binn/;C:/Program Files (x86)/Microsoft SDKs/TypeScript/1.0/;C:/windows/system32;C:/windows;C:/windows/System32/Wbem;C:/windows/System32/WindowsPowerShell/v1.0/;C:/Program Files/Puppet Labs/Puppet/bin;C:/Program Files/Common Files/Autodesk Shared/;C:/Program Files (x86)/Autodesk/Backburner/;C:/Program Files (x86)/QuickTime/QTSystem/;C:/wamp/bin/php/php5.6.15;C:/Program Files/Autodesk/Maya2015/plug-ins/bifrost/bin;C:/Program Files/Autodesk/mentalrayForMaya2015/bin;C:/Program Files/Autodesk/Maya2015/plug-ins/substance/bin;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/bin",
        "MAYA_SCRIPT_PATH":           "C:/Program Files/Autodesk/Maya2015/scripts;C:/Program Files/Autodesk/Maya2015/scripts/startup;C:/Program Files/Autodesk/Maya2015/scripts/others;C:/Program Files/Autodesk/Maya2015/scripts/AETemplates;C:/Program Files/Autodesk/Maya2015/scripts/unsupported;C:/Program Files/Autodesk/Maya2015/scripts/paintEffects;C:/Program Files/Autodesk/Maya2015/scripts/fluidEffects;C:/Program Files/Autodesk/Maya2015/scripts/hair;C:/Program Files/Autodesk/Maya2015/scripts/cloth;C:/Program Files/Autodesk/Maya2015/scripts/live;C:/Program Files/Autodesk/Maya2015/scripts/fur;C:/Program Files/Autodesk/Maya2015/scripts/muscle;C:/Program Files/Autodesk/Maya2015/scripts/turtle;C:/Program Files/Autodesk/Maya2015/scripts/FBX;C:/Program Files/Autodesk/Maya2015/scripts/mayaHIK;C:/Program Files/Autodesk/Maya2015/plug-ins/bifrost/scripts/presets;C:/Program Files/Autodesk/Maya2015/plug-ins/bifrost/scripts;C:/ExocortexAlembic/Maya2015/Module/scripts;C:/Program Files/Autodesk/Maya2015/plug-ins/fbx/scripts;C:/Program Files/Autodesk/mentalrayForMaya2015/scripts/AETemplates;C:/Program Files/Autodesk/mentalrayForMaya2015/scripts/mentalray;C:/Program Files/Autodesk/mentalrayForMaya2015/scripts/unsupported;C:/Program Files/Autodesk/mentalrayForMaya2015/scripts;C:/Program Files/Autodesk/Maya2015/plug-ins/substance/scripts;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/cafm;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/xmaya;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/brushes;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/dialogs;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/fxmodules;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/tabs;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/util;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/widgets;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts",
        "MAYA_PLUG_IN_RESOURCE_PATH": "C:/Program Files/Autodesk/Maya2015/plug-ins/bifrost/resources;C:/ExocortexAlembic/Maya2015/Module/resources;C:/Program Files/Autodesk/Maya2015/plug-ins/fbx/resources;C:/Program Files/Autodesk/mentalrayForMaya2015/resources;C:/Program Files/Autodesk/Maya2015/plug-ins/substance/resources;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/resources"
    }
    
    # Replace "guido.pollini" with the local userName
    """
    userName = getpass.getuser()    
    for var in modifiedVars:
        modifiedVars[var] = modifiedVars[var].replace("guido.pollini", userName)
    """

    # Add the path of 'MuTools'
    modifiedVars['PYTHONPATH'] += ';C:/Users/guido.pollini/Desktop/MuTools'

    # To resolve reference relative paths
    modifiedVars["PROD_SERVER"] = "Y:"    

    # Now clean all
    for var in modifiedVars:
        actualEnv[var] = modifiedVars[var]








    #------------------------------------
    # READY TO SPAWN...
    #------------------------------------

    # Maya's commandLine flags:
    #   -command -->  MEL code block
    #   -script  -->  MEL script
    # Apparently, you can't directly pass a Python script (whatever, use the MEL command 'python"...";') 

    thisCommandPortIP = 123456
    mayaCommandLine = 'maya.exe -noAutoloadPlugins -command "python \\\"'\
                      'import MuTools.Ellipse_AlembicExporterServer;'\
                      'MuTools.Ellipse_AlembicExporterServer.initialize(' + str(thisCommandPortIP) + ')'\
                      '\\\""'
    
    #SW_MINIMIZE = 6
    #info = subprocess.STARTUPINFO()
    #info.dwFlags = subprocess.STARTF_USESHOWWINDOW
    #info.wShowWindow = SW_MINIMIZE

    remoteMayaProcess = subprocess.Popen(mayaCommandLine, env=actualEnv) #, startupinfo=info) 

    print 'SPAWNED >>>', remoteMayaProcess
    return remoteMayaProcess












#------------------------------------------------------------------------------
# Module loaded!
Utils.moduleLoadedMessage()
#------------------------------------------------------------------------------
