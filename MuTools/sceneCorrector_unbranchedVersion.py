import maya.cmds     as MC
import maya.mel      as MM
import maya.OpenMaya as OM
import time
import os
from pprint import pprint


print '[{0}.py] Loading module from "{1}"...'.format(__name__, __file__)


class RootNamespaceActive(object):
    def __enter__(self):
        self.originalNamespace = MC.namespaceInfo(currentNamespace=True)
        MC.namespace(set=':')        
    def __exit__(self, *args):
        MC.namespace(set=self.originalNamespace)


class MainPanelDisabled(object):
    def __enter__(self):
        MM.eval('paneLayout -e -manage false $gMainPane')
    def __exit__(self, *args): 
        MM.eval('paneLayout -e -manage true $gMainPane')


class Timer(object):
    def __enter__(self):
        self.startTime = time.clock()
    def __exit__(self, *args):
        print "-"*80
        print "Elapsed time:", time.clock() - self.startTime
        print "-"*80
        print  


def getFolders(dirName, fullName=False):
    dirContent = os.listdir(dirName)
    prefix = dirName + '/' if fullName else ''        
    folders = [prefix + x for x in dirContent if os.path.isdir(dirName + '/' + x)]
    return folders


def getFiles(dirName, fullName=False):
    dirContent = os.listdir(dirName)
    prefix = dirName + '/' if fullName else ''        
    files = [prefix + x for x in dirContent if os.path.isfile(dirName + '/' + x)]
    return files


def exocortexAlembicExport(nodeList, targetPath, purePointCache):
    """
    Exocortex job syntax:
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
# MC.namespace(rename=['oldNamespace', 'newNamespace'])
# MC.namespaceInfo(listOnlyDependencyNodes=True) --> get the list of nodes in the current namespace
# MC.referenceQuery(xxx, nodes=True, dagPath=True) --> get the nodes
#
# HERE CHECK IF THE NEW NAMESPACE EXISTS (the '__TEMP__' is to get idempotency)
# MC.file(fileName, edit=True, namespace='__TEMP__')
# MC.file(fileName, edit=True, namespace='newNamespace')
# MC.file(file???, edit=True, namespace='newNamespace'  --> to modify a referenced file namespace (the new one must not exist)

def getSceneNamespaces(*args):
    with RootNamespaceActive():
        # 'UI' and 'shared' are internal namespaces
        sceneNamespaces = [x for x in MC.namespaceInfo(listOnlyNamespaces=True) if x not in ['UI', 'shared']]
    return sceneNamespaces
    
def getWorldTransforms():
    worldTransforms = []

    # Initialized to a fake "world" (not a kTransform)
    DAGIter = OM.MItDag(OM.MItDag.kBreadthFirst) 

    selList = OM.MSelectionList()
    fn = OM.MFnTransform()
    
    while True:
        DAGIter.next() # Skip the first one (a "fakeWorld")
        nodePtr = DAGIter.currentItem()
        if DAGIter.depth() == 1:
            if nodePtr.apiType() == OM.MFn.kTransform:
                fn.setObject(nodePtr)
                nodeName = fn.partialPathName()
                if MC.objExists(nodeName):
                    # To avoid "weird" transforms like "|groundPlane_transform"
                    # which exist, but invisible to MEL
                    worldTransforms.append(nodeName)
        else:
            break

    return worldTransforms        




"""
with MainPanelDisabled():
  with Timer():
    filePath = 'Y:/01_SAISON_4/05_UTILE/Rendu/13_REMOTE_MAYA/ORIGINAL__YKR426_051_ani.ma'
    MC.file(filePath, open=True, type='mayaAscii', loadReferenceDepth='none', force=True, options='v=0;', ignoreVersion=True)
  
    referenceData = getReferenceData()    

    #MC.file(filePath, open=True, type='mayaAscii', loadReferenceDepth='all', force=True, options='v=0;', ignoreVersion=True)
    # loadReferenceDepth = 'all', 'none' ('none' -> only path validation)
    for asset in referenceData:
        referencePath = referenceData[asset][0]
        print 'Loading reference "' + referencePath + '"...'
        MC.file(referencePath, loadReference=referenceData[asset][2], loadReferenceDepth='asPrefs')
        print 'Reference "' + referencePath + '" loaded!'
"""

def prettyPrintList(title, content):
    print
    #print '-'*80
    print title
    #print '-'*80
    if len(content) > 0:
        for c in sorted(content):
            print ' ', c
    else:
        print '  NONE'     


#==============================================================================================================
#==============================================================================================================
def getParent(transform):
    try:
        parent = MC.listRelatives(transform, parent=True, path=True)[0]
    except:
        # If child of the world
        parent = None
    return parent


"""
Forse il metodo classico e' migliore:
   if node.getMesh(): ...
   if node.getMeshes(): ...
   if node.getLocator(): ...
   if node.getNurbsCurves(): ...
"""
def isTypedTransform(node, allowedType='mesh', noIntermediate=True, onlyOne=True):
    """
    Check if it's a <transform> and filter according to its shapes
    """
    
    if MC.nodeType(node) != 'transform':
        return False

    # The flag combination 'shapes + noIntermediate' is valid, 
    # but not 'type + noIntermediate' (the latter is ignored)
    shapeChildren = MC.listRelatives(node, children=True, path=True, shapes=True, noIntermediate=noIntermediate) or []
    allowedShapeChildren = [x for x in shapeChildren if MC.nodeType(x) == allowedType]
    
    if onlyOne:
        return len(allowedShapeChildren) == 1
    else:
        return len(allowedShapeChildren) >= 1 


def isLocatorTransform(node):
    return isTypedTransform(node, allowedType='locator', noIntermediate=True, onlyOne=True)

    
def isMeshTransform(node):
    return isTypedTransform(node, allowedType='mesh', noIntermediate=True, onlyOne=True)

        
def isNurbsCurveTransform(node):
    return isTypedTransform(node, allowedType='nurbsCurve', noIntermediate=True, onlyOne=False)
    


#==============================================================================================================
#==============================================================================================================



"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Quando un filePath non viene trovato, on a lapossibilita di SKIP IGNORE RETRY, CHANGE
... lo SKIP lascia la referenza not loaded ma dentro la sceneNamespaces
... IGNORE getta via la referenza

KOSA SUCCEDE IN MAYAPY????
- da dei warnings, ma continua;
- getReferences() funziona
- abbiamo tutti i referenceNodes
- abbiamo anche i namespace...

QUINDI TUTTO OK anche in mayapy
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class Reference(object):
    def __init__(self, filePath):
        self.filePath = filePath


    @staticmethod
    def getReferences():
        #----------------------------------------------------------------------------------
        # File referenced once:
        #   "Y:/01_SAISON_4/08_ASSETS/3D/ch/ch_buffa/rig/ch_fucky_rig.ma"
        #
        # File referenced multiple times:
        #   "Y:/01_SAISON_4/08_ASSETS/3D/ch/ch_buffa/rig/ch_buffa_rig.ma"      (NOT {0})
        #   "Y:/01_SAISON_4/08_ASSETS/3D/ch/ch_buffa/rig/ch_buffa_rig.ma{1}"
        #   ...
        #   "Y:/01_SAISON_4/08_ASSETS/3D/ch/ch_buffa/rig/ch_buffa_rig.ma{16}"
        #----------------------------------------------------------------------------------
        referencedFiles = MC.file(query=True, reference=True, withoutCopyNumber=False)
        return [Reference(x) for x in referencedFiles]


    @property
    def cleanFilePath(self):
        return self.filePath.split('{')[0]


    @property
    def category(self):
        knownAssetTags = ['ch', 'pr', 'st', 'ss']
        # Recover the 'asset type'
        assetTag = 'unknown'
        for tag in knownAssetTags:
            if self.originalName.startswith(tag + '_'):
                assetTag = tag
        # The camera is not a Shotgun asset        
        if self.originalName == 'yak_camera':
            assetTag = 'cam'    
        
        return assetTag   


    @property
    def originalName(self):
        originalName = self.filePath.split('/')[-1].split('{')[0].replace('.ma', '')
        return originalName


    @property
    def referenceNode(self):
        return MC.file(self.filePath, query=True, referenceNode=True)
    

    @property
    def namespace(self):
        """
        Every referenced file MUST have either a namespace or a prefix (and the latter is FATAL)
        """
        potentialNamespace = MC.file(self.filePath, query=True, namespace=True)
        # It could be a "prefix" (and it would be a serious problem because this can't be corrected via a command!!!)
        """ NOT EXACTLY; if the namespace already existed because assigned to another asset, this check would fail """
        """ ... protect everything!!! """
        if MC.namespace(exists=potentialNamespace):
            return potentialNamespace
        else:
            return None    


    @property
    def renderSet(self):
        if self.namespace is None:
            # A shitty prefix; fatal...
            return None
        potentialRenderSet = self.namespace + ':RenderSet'
        if not (MC.objExists(potentialRenderSet) and MC.nodeType(potentialRenderSet) == 'objectSet'):
            return None    
        
        return potentialRenderSet


    @property
    def isBroken(self):
        return os.path.isfile(self.cleanFilePath)







ASSETS_PATH    = 'Y:/01_SAISON_4/08_ASSETS/3D/'
ANIMATION_PATH = 'Y:/01_SAISON_4/05_UTILE/Rendu/13_REMOTE_MAYA/'


def run(*args):

    # Predefined asset folders; they must exist and be worldChildren:
    assetFolders = {'cam': '__CAMERA__', 
                    'ch':  '__CHARS__', 
                    'pr':  '__PROPS__', 
                    'st':  '__SET__', 
                    'ss':  '__SUBSET__'
    }
    for folder in assetFolders.values():
        if not MC.objExists(folder):
            print 'MISSING FOLDER: {0} doesn\'t exist'.format(folder)
        else:
            if MC.listRelatives(folder, parent=True):
                print 'MISPLACED FOLDER: {0} must be a worldChild!'.format(folder)
  





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
    references = Reference.getReferences()

    for ref in references:

        if ref.namespace is None:
            # Skip reference with prefixes... It's a FATALITY
            prefixedReferences.append(ref.filePath)
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

        if ref.category in ['ch', 'pr', 'ss', 'cam']:
            rootTransform = ref.namespace + (':camera_rig' if ref.category == 'cam' else ':rig_group') 
            if not MC.objExists(rootTransform):
                MC.error('NO IDEA!!!')

            parent = getParent(rootTransform)
            if parent == assetFolders[ref.category]:
                properTransforms.append(rootTransform)
                #print '[OK] It\'s inside "{}"!'.format(parent)        
            else:                
                badTransforms.append(rootTransform)
                #print '[BAD] It\'s inside "{}"!'.format(parent if parent is not None else '__world__')





        #--------------------------------------------------------------------------------------------------------------
        # ST
        #--------------------------------------------------------------------------------------------------------------                
        # 'st' assets have not necessarily a rootTransform, but a list of <locators> holding meshes.

        elif ref.category == 'st':
            """ DEVO RECUPERARE ANCHE LE PLACCHE NON REFERENCED? le ..._COPY? sono nel renderset"""
            nodes = MC.namespaceInfo(ref.namespace, listOnlyDependencyNodes=True)
            #nodes = MC.referenceQuery(ref.filePath, nodes=True, dagPath=True)
            locators = [x for x in nodes if isLocatorTransform(x)]
            for locator in locators:
                parent = getParent(locator)
                if parent == '__SET__':
                    properTransforms.append(locator)
                    #print '[OK] It\'s inside "{}"!'.format(parent)        
                else:
                    badTransforms.append(locator)
                    #print '[BAD] It\'s inside "{}"!'.format(parent if parent is not None else '__world__')





        #--------------------------------------------------------------------------------------------------------------
        # UNKNOWN
        #--------------------------------------------------------------------------------------------------------------                
        # Referenced files without a proper tag; can't do anything!
        else:
            toDoReferences.append(ref.filePath)





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
    irrelevantTransforms = set(['persp', 'top', 'front', 'side', 'front', 'platesHolder'])
    transformsToSkip = set(properTransforms) | set(badTransforms) | irrelevantTransforms

    worldTransformsToAnalyze = set(getWorldTransforms()) - transformsToSkip


    # Transforms potentially holding an SS: 
    # - put them into a proper namespace ("ss_XXXX", only the "ss_" tag matters);
    # - reparent them to the folder "__SET__". 
    rootTransforms = set()


    def analyzeChildren(actualTrans, depth=0):
        if isMeshTransform(actualTrans):
            longName = MC.ls(actualTrans, long=True)[0]
            #print 'MT ' + ' '*depth, longName

            #    |fakeParent|pascal:G2|pascal:G1|pascal:GUIDO
            # fakeParent   pascal:G2   pascal:G1   pascal:GUIDO
            parentTags = longName.lstrip('|').split('|')

            if len(parentTags) == 1:
                # It's a world meshTransform
                rootTransforms.add('|' + actualTrans)

            else:    
                rootParent = parentTags[0]
                if rootParent not in assetFolders.values():
                    rootTransforms.add('|' + rootParent)
                else:
                    nextRootParent = '|' + rootParent + '|' + parentTags[1]
                    rootTransforms.add(nextRootParent)    


        children = MC.listRelatives(actualTrans, children=True, path=True) or []
        for child in children:
            if child not in transformsToSkip:
                analyzeChildren(child, depth=depth + 1)

    for trans in worldTransformsToAnalyze:
        analyzeChildren(trans, depth=0)


    # Create a suitable 'renderSet'
    print 
    print 'ROOT MESHTRANSFORMS:'
    for root in rootTransforms:
        print '  ', root


    prettyPrintList('PREFIXED', prefixedReferences)
    prettyPrintList('PROPER', properTransforms)
    prettyPrintList('UNKNOWN', toDoReferences)
    prettyPrintList('BAD', badTransforms)
    prettyPrintList('SCENE NAMESPACES', getSceneNamespaces())

    """
    nodeList = ['ch_yakar:face']
    targetPath = 'Y:/01_SAISON_4/07_WIP/3D/__DEBUG_PROD/ALEMBIC/test.abc'
    purePointCache = False
    exocortexAlembicExport(nodeList, targetPath, purePointCache)
    """




t = os.path.getmtime(__file__) # Seconds passed between Epoch and last modification 
formattedTime = time.strftime("%d/%m/%y, %H:%M:%S", time.localtime(t))
print '[{0}.py] SUCCESS: module loaded! Last update {1}.'.format(__name__, formattedTime)
