__version__ = '1.0.2'



import MuTools.MuCore  as Core
import MuTools.MuUtils as Utils

import maya.cmds       as MC
import maya.mel        as MM
import maya.OpenMaya   as OM



#------------------------------------------------------------------------------
# Loading module...
Utils.moduleLoadingMessage()
#------------------------------------------------------------------------------





"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
===============================================================================================================================================
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

SCENE METHODS


Why do I need this shit?
Simple, just compare:

  name = MC.file(query=True, sceneName=True, shortName=True)
  name = MC.file(q=True, sn=True, shn=True)
  name = Scene.getName()

  save = MC.file(query=True, anyModified=True)
  save = MC.file(q=True, am=True)
  save = Scene.isModified()

_______________________________________________________________________________________________________________________________________________
===============================================================================================================================================
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


"""
'MC.file' shitty flags:
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












#=======================================================================================================
#-------------------------------------------------------------------------------------------------------
#
# DISABLING and REENABLING the viewport
#
#-------------------------------------------------------------------------------------------------------
#=======================================================================================================
def disableUI(*args):
    # Disable all UI elements and disable also all the viewports; but reenable 
    # the 'Help Line' because it offers a load progressBar and could give a hint 
    # if remoteMaya has crashed!
    # Disable also the viewports' refresh.
    MELCommand = """
        HideUIElements;
        toggleUIComponentVisibility("Help Line");        
        paneLayout -edit -manage false $gMainPane;
    """                
    MM.eval(MELCommand)





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




def disableViewport20(*args):
    # A 'viewport' is a panel of type 'modelPanel'
    modelPanels = MC.getPanel(type="modelPanel")
    for panel in modelPanels:
        MC.modelEditor(panel, edit=True, rendererName='base_OpenGL_Renderer')




def isModified():
    return MC.file(query=True, anyModified=True)



# Which one is better?
#
#   short = Scene.getName()
#   long  = Scene.getName(long=True)
#
#   short = Scene.getName()
#   long  = Scene.getLongName()
#
# ... The second one:)



def getName(long=False):
    """ 'expandName' ??? To resolve things like $PROJECT/fuckMe/now ? """
    sceneName = MC.file(query=True, sceneName=True, shortName=not long)
    return sceneName if sceneName != '' else None




def getLongName():
    return getName(long=True)




def getType():
    # - "mayaAscii"
    # - "mayaBinary"
    compatibleTypes = MC.file(query=True, type=True) # This is a list of compatible types
    return compatibleTypes[0]




def getNodeSelection(filter=None):
    """
    Filter the selectionList with 'type=DGNode' 
    """
    selectionNames = MC.ls(selection=True, dependencyNodes=True, long=True)
    return Core.Bundle(selectionNames)




def getSets():
    # listSets(allSets=True) is SEVERELY broken:
    #  - 2 parasites (unselectionable fake sets) comes out
    #  - the namespace info is LOST... seriously
    
    sets = MC.ls(type="objectSet") 
    # or MC.ls(sets=True), same thing
    
    return Core.Bundle(sets)




def getWorldChildren():
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

    return Core.Bundle(worldChildren)




def getIsolatedNodes(**kwargs):
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




def getSceneNamespaces(*args):
    with Core.RootNamespaceActive():
        # 'UI' and 'shared' are internal namespaces
        sceneNamespaces = [x for x in MC.namespaceInfo(listOnlyNamespaces=True) if x not in ['UI', 'shared']]
    return sceneNamespaces



     


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
    """
    This can't be a <Bundle>: at the present time Bundle works only for DGNodes and
    a <Reference> is NOT...
    """
    referencedFiles = MC.file(query=True, reference=True, withoutCopyNumber=False)
    return [Core.Reference(x) for x in referencedFiles]




def createReference(*args, **kwargs):
    """
    Add a reference to the scene and return the 'Reference' object
    """
    pass




def getAnimationInfo():
    animationInfoDict = {
        'minTime':   MC.playbackOptions(query=True, minTime=True),
        'maxTime':   MC.playbackOptions(query=True, maxTime=True),
        'startTime': MC.playbackOptions(query=True, animationStartTime=True),
        'endTime':   MC.playbackOptions(query=True, animationEndTime=True),
    }
    return animationInfoDict




def getCurrentUnits():
    # ex: {'angle': 'degree', 'linear': 'centimeter', 'time': 'pal'}
    currentUnitsDict = {
        'linear': MC.currentUnit(query=True, linear=True, fullName=True),
        'angle':  MC.currentUnit(query=True, angle=True, fullName=True),
        'time':   MC.currentUnit(query=True, time=True)
    }
    return currentUnitsDict








def exists(nodeName):
    """
    To add:
     - 'smart' exists;
     - regExp exists;
     - namespace confination 
    """
    return MC.objExists(nodeName)


def getParent(nodeName):
    node = Core.MuNode(nodeName)
    return node.getParent()







def setCurrentUnits():
    pass





#------------------------------------------------------------------------------
# Module loaded!
Utils.moduleLoadedMessage()
#------------------------------------------------------------------------------

