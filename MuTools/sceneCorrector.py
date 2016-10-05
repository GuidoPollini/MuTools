
__version__ = '1.0.3'


import MuTools.MuUtils   as Utils
import MuTools.MuCore    as Core
import MuTools.MuScene   as Scene


import maya.cmds     as MC
import maya.mel      as MM
import maya.OpenMaya as OM

import time
import os




#------------------------------------------------------------------------------
# Loading module...
Utils.moduleLoadingMessage()
#------------------------------------------------------------------------------



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
            log.fatality('MISSING FOLDER: {} doesn\'t exist'.format(folderName))
        
        if Scene.parent(folderName):
            log.fatality('MISPLACED FOLDER: {} must be a worldChild!'.format(folderName))





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
            
            if parent.name == assetFolderNames[yakariTag]:
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

                if parent and parent.name == '__SET__':
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
            parentTags = actualTrans.longName.lstrip('|').split('|')

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



















#------------------------------------------------------------------------------
# Module loaded!
Utils.moduleLoadedMessage()
#------------------------------------------------------------------------------
