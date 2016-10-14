__version__ = '1.0.4'
print '--> Executing MuScene...'


import MuTools.MuUtils as Utils
import MuTools.MuCore  as Core

import maya.cmds       as MC
import maya.mel        as MM
import maya.OpenMaya   as OM



#------------------------------------------------------------------------------
# Loading module...
Utils.moduleLoadingMessage()
#------------------------------------------------------------------------------
log = Utils.Log('MuSceneLog', Utils.Log.STANDARD)















class FileError(Exception):
    """
    Generic exception to catch file errors
    """
    def __init__(self, message):
        MC.error('[FILE ERROR] ' + message)






def animationInfo():
    animationInfoDict = {
        'minTime':   MC.playbackOptions(query=True, minTime=True),
        'maxTime':   MC.playbackOptions(query=True, maxTime=True),
        'startTime': MC.playbackOptions(query=True, animationStartTime=True),
        'endTime':   MC.playbackOptions(query=True, animationEndTime=True),
    }
    return animationInfoDict

def createReference(*args, **kwargs):
    """
    Add a reference to the scene and return the 'Reference' object
    """
    pass

def currentUnits():
    # ex: {'angle': 'degree', 'linear': 'centimeter', 'time': 'pal'}
    currentUnitsDict = {
        'linear': MC.currentUnit(query=True, linear=True, fullName=True),
        'angle':  MC.currentUnit(query=True, angle=True, fullName=True),
        'time':   MC.currentUnit(query=True, time=True)
    }
    return currentUnitsDict

def disableUI(*args):
    # Disable all UI elements and disable also all the viewports; but reenable 
    # the 'Help Line' because it offers a load progressBar and could give a hint 
    # if remoteMaya has crashed!
    MELCommand = """
        HideUIElements;
        toggleUIComponentVisibility("Help Line");        
        paneLayout -edit -manage false $gMainPane;
    """                
    MM.eval(MELCommand)

def disableViewport20(*args):
    # A 'viewport' is a panel of type 'modelPanel'
    modelPanels = MC.getPanel(type="modelPanel")
    for panel in modelPanels:
        MC.modelEditor(panel, edit=True, rendererName='base_OpenGL_Renderer')

def enableUI(*args):
    # Enable viewports
    MELCommand = 'paneLayout -edit -manage true $gMainPane;'

    # Enanble only what really matters...
    UIElementNames = [
        #'Attribute Editor',
        #'Channel Box / Layer Editor',
        #'Tool Settings',
        #'Shelf',     
        'Tool Box',  
        'Time Slider',
        'Range Slider',  
        'Command Line',   
        'Help Line',
        'Status Line'                
    ]    
    
    for name in UIElementNames:
        print name
        # If not visible, toggle it's visibility
        MELCommand += """
            if (!`isUIComponentVisible("{0}")`){{
                toggleUIComponentVisibility("{0}");}}
        """.format(name)
    
    MM.eval(MELCommand)

def isModified():
    return MC.file(query=True, anyModified=True)

def isolatedNodes(**kwargs):
    type_value = kwargs.get("type", kwargs.get("t", None))
    # Check for "isolated" (nodes without connections) of a spefic type
    if type:
        candidates = MC.ls(exactType=type_value) or []
    else:
        candidates = MC.ls() or []
    
    isolatedNodes = []

    for nodeName in candidates:
        connections = MC.listConnections(nodeName, source=True, destination=True) or []
        if len(connections) == 0:
            # Orphan found!
            isolatedNodes.append(Wrapper(nodeName))
    
    return isolatedNodes                

def load(filePath, loadReferences=False):
    if not MC.file(filePath, query=True, exists=True):
        raise FileError('The path "{}" is wrong!'.format(filePath))
    
    # type --> [knownTypeStr], an list (!) with a type known by Maya;
    #      --> None, a type of file Maya can't handle.    
    fileType = MC.file(filePath, query=True, type=True)
    if not fileType or fileType[0] not in ('mayaAscii', 'mayaBinary'):
        raise FileError('The file "{}" is not a Maya ASCII or binary!'.format(filePath))
            
    loadReferenceDepth = 'all' if loadReferences else 'none'
    
    MC.file(filePath, 
            open=True,    
            force=True, 
            loadReferenceDepth=loadReferenceDepth,             
            ignoreVersion=True, 
            options="v=0;")  
            
    # Add the filePath to the 'Recent Files' ('optionVars' stuff...)            
    melCommand = 'addRecentFile("{0}", "{1}");'.format(filePath, fileType)
    MM.eval(melCommand)

def loadPlugin(*args):
    """
    loadPlugin(<str>|<list>|<set>|<tuple>)
    """

    # MayaExocortexAlembic Mayatomr ...
    if isinstance(args[0], (list, set, tuple)):
        pluginNames = args[0]
    else: 
        pluginNames = args
    
    with Core.WaitCursorActive():
        for pluginName in pluginNames:
            log('Plugin "{}" loading...'.format(pluginName))
        
            #MC.pluginInfo(pluginName, edit=True, autoload=True)
            MC.loadPlugin(pluginName)
        
            log('Plugin "{}" loaded!'.format(pluginName))
  
def longName():
    return getName(long=True)

def name(long=False):
    """ 'expandName' ??? To resolve things like $PROJECT/fuckMe/now ? """
    sceneName = MC.file(query=True, sceneName=True, shortName=not long)
    return sceneName if sceneName != '' else None

def namespaces(*args):
    with Core.RootNamespaceActive():
        # 'UI' and 'shared' are internal namespaces
        sceneNamespaces = [x for x in MC.namespaceInfo(listOnlyNamespaces=True) if x not in ['UI', 'shared']]
    return sceneNamespaces

    # MC.namespace(rename=['oldNamespace', 'newNamespace'])
    # MC.namespaceInfo(listOnlyDependencyNodes=True) --> get the list of nodes in the current namespace
    # MC.referenceQuery(xxx, nodes=True, dagPath=True) --> get the nodes
    #
    # HERE CHECK IF THE NEW NAMESPACE EXISTS (the '__TEMP__' is to get idempotency)
    # MC.file(fileName, edit=True, namespace='__TEMP__')
    # MC.file(fileName, edit=True, namespace='newNamespace')
    # MC.file(file???, edit=True, namespace='newNamespace'  --> to modify a referenced file namespace (the new one must not exist)

def nodeExists(nodeName):
    """
    To add:
     - 'smart' exists;
     - regExp exists;
     - namespace confination 
    """
    return MC.objExists(nodeName)

def nodeSelection(filter=None):
    """
    Filter the selectionList with 'type=DGNode' 
    """
    selectionNames = MC.ls(selection=True, dependencyNodes=True, long=True)
    return Core.List(selectionNames)

def parent(nodeName):
    node = Core.MuNode(nodeName)
    return node.parent()

def references():
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
    """
    This can't be a <List>: at the present time List works only for DGNodes and
    a <Reference> is NOT...
    """
    referencedFiles = MC.file(query=True, reference=True, withoutCopyNumber=False)
    return [Core.Reference(x) for x in referencedFiles]

def refresh(*args):
    MC.refresh()

def select(*args, **kwargs):
    """
    Scene.select() --> deselect everything
    """
    if not args and not kwargs:
        MC.select(clear=True)
    else:
        MC.select(*args, **kwargs)    

def setCurrentUnits():
    pass

def sets():
    # listSets(allSets=True) is SEVERELY broken:
    #  - 2 parasites (unselectionable fake sets) come out;
    #  - the namespace info is LOST... seriously, FUCK YOU Autodesk!
    
    sets = MC.ls(type="objectSet") 
    # or MC.ls(sets=True), same thing
    
    return Core.List(sets)

def type():
    # - "mayaAscii"
    # - "mayaBinary"
    compatibleTypes = MC.file(query=True, type=True) # This is a list of compatible types
    return compatibleTypes[0]

def worldChildren():
    worldChildren = []

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
                nodeName = fn.fullPathName()
                if MC.objExists(nodeName):
                    # To avoid "weird" transforms like "|groundPlane_transform"
                    # which exist, but invisible to MEL
                    worldChildren.append(nodeName)
        else:
            break

    return Core.List(worldChildren)






#------------------------------------------------------------------------------
# Module loaded!
Utils.moduleLoadedMessage()
#------------------------------------------------------------------------------












"""
NOTE
  156.917671932s:  full scene load
  382.712135774s:  load bare scene, then load all references
  --> In a huge scene (20 heavy references) more than TWICE slower!!!

  With the second system I could get kinda progress bar, but it's hyper slow;
  Try to recover the QWidget of the progressBar (active during loading) and 
  connect it to a Qt-signal...
"""
  

"""
-----------------------
'MC.file' flags
-----------------------
  activate
  activeProxy
  anyModified
  applyTo
  buildLoadSettings
  channels
  cleanReference
  command
  compress
  constraints
  constructionHistory
  copyNumberList
  defaultExtensions
  defaultNamespace
  deferReference
  editCommand
  errorStatus
  executeScriptNodes
  exists
  expandName
  exportAll
  exportAnim
  exportAnimFromReference
  exportAsReference
  exportAsSegment
  exportSelected
  exportSelectedAnim
  exportSelectedAnimFromReference
  exportSelectedNoReference
  exportUnloadedReferences
  expressions
  flushReference
  force
  groupLocator
  groupName
  groupReference
  i
  ignoreVersion
  importReference
  lastFileOption
  lastTempFile
  list
  loadAllDeferred
  loadAllReferences
  loadNoReferences
  loadReference
  loadReferenceDepth
  loadSettings
  location
  lockContainerUnpublished
  lockFile
  lockReference
  mapPlaceHolderNamespace
  mergeNamespacesOnClash
  modified
  moveSelected
  namespace
  newFile
  open
  options
  parentNamespace
  postSaveScript
  preSaveScript
  preserveName
  preserveReferences
  prompt
  proxyManager
  proxyTag
  reference
  referenceDepthInfo
  referenceNode
  removeDuplicateNetworks
  removeReference
  rename
  renameAll
  renameToSave
  renamingPrefix
  renamingPrefixList
  resetError
  returnNewNodes
  save
  saveDiskCache
  saveReference
  saveReferencesUnloaded
  saveTextures
  sceneName
  segment
  selectAll
  shader
  sharedNodes
  sharedReferenceFile
  shortName
  strict
  swapNamespace
  type
  uiConfiguration
  unloadReference
  unresolvedName
  usingNamespaces
  withoutCopyNumber
  writable
"""