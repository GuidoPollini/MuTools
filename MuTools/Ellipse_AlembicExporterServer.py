__version__ = '1.0.0'


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
NOTE
  The global objects defined in this module live in:
  - "MuTools.Ellipse_AlembicExporterServer"
  because 'Ellipse_AlembicExporterServer.py' lives in the package 'MuTools'
  and its __init__ is automatically invoked!
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



import MuTools.MuUtils     as Utils
import MuTools.MuCore      as Core
import MuTools.MuScene     as Scene
#import MuTools.MuMessaging as Messaging
import MuTools.MuUI        as UI

import maya.cmds           as MC
import maya.mel            as MM

import PySide.QtCore       as QC
import PySide.QtGui        as QG
import shiboken





#------------------------------------------------------------------------------
# Loading module...
Utils.moduleLoadingMessage()
#------------------------------------------------------------------------------






def serverMessagingCallback(message):
    """
    The almighty callback that receives the client orders (string)
    """
    print 'Received from <mayaClient>:', message




def initialize(clientPortId):
    print '>>> clientPortId', clientPortId

    Scene.disableViewport20()
    Scene.disableUI()
    Scene.refresh()
    MM.eval('renderThumbnailUpdate false;')

    mayaWindow = UI.MayaWindow.mainWindow()
    mayaWindow.setWindowTitle(' REMOTE MAYA')
    mayaWindow.setWindowIcon(QG.QIcon('C:/Users/guido.pollini/Desktop/muIcon.png'))




    #--------------------------------------------
    # Plugins loading (the bare minimum)
    #--------------------------------------------
    toonKitPath = 'Y:/01_SAISON_4/00_PROGRAMMATION/Toonkit_Module/Maya2015/plug-ins/'
    pluginsToLoad = (
    	'Turtle.mll',
        'Mayatomr.mll',
        'MayaExocortexAlembic.mll',
        toonKitPath + 'tkSoftIKNode.mll',
        toonKitPath + 'tkSpringNode.mll'
    )

    for pluginName in pluginsToLoad:
        Scene.loadPlugin(pluginName)
        #Messaging.sendMessage(clientPortId, 'Plugin [' + pluginName + '] loaded!')


    # Open a commandPort to receive orders
    serverCommandPort = Messaging.CommandPort(8888, serverMessagingCallback)


    #--------------------------------------------
    # Ready to serve
    #--------------------------------------------
    # Tell the client you're ready...
    Messaging.sendMessage(clientPortId, 'LOADED ' + str(serverCommandPort.portId()))
    



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




def run(*_):
    analyzeScene('YKR513', 'sh103_B')

def getAnimationPath(episodeTag, shotTag):
    # 'YKR###', '###'
    # 'sh012', 'sh099_A', '012', '012_B'

    # long(episodeTag)  --> 'YKR###'
    # short(episodeTag) --> '###'
    # long(shotTag)     --> 'sh###_@'
    # short(shotTag)    --> '###_@'

    animationFolder = 'Y:/01_SAISON_4/09_EPISODES/04_Fabrication_3D/{0}/{1}/ani/maya/'.format(episodeTag, shotTag)
    animationPath = animationFolder + episodeTag + '_' + shotTag.lstrip('sh') + '_ani.ma'
    return animationPath


def analyzeScene(episodeTag, shotTag):
    # --> Animation tags
    # Y:/01_SAISON_4/09_EPISODES/04_Fabrication_3D/@@@@@@/@@@@@@@/ani/maya/@@@@@@@@@@@@_ani.ma
    #                                              YKR513 sh002            YKR513_002
    #                                              YKR513 sh103_B          YKR513_103_B
    

    # --> Cache path
    # Y:/01_SAISON_4/09_EPISODES/04_Fabrication_3D/@@@@@@/@@@@@/ani/maya/publish/caches_@@@
    #                                              YKR506 sh114                         060

    # --> Cache Name (from the folder 'caches_060') 

    # ##########_##########_###.abc
    # YKR506_114 ch_reckq   060
    # YKR506_114 cam        060
    # YKR506_114 cameraPROJ 060
    #
    # But this is a '.ma':
    # YKR506_114_camera_rig_060.ma
    animationPath = getAnimationPath(episodeTag, shotTag)


    # Disable the UI to avoid viewport2.0 interferences after load    
    Scene.disableUI()

    try:
        noLoadErrors = Scene.load(animationPath)
    except Scene.FileError as exc:
        MC.error(str(exc))

    """ THIS SHIT DOESN'T WORK!!! FUCK YOU """
    if noLoadErrors:
        print 'nickel'    
    else:
        print 'error suppressed'

    """
    Scene.load()

    fabricationPath = 'Y:/01_SAISON_4/09_EPISODES/04_Fabrication_3D'
    animationPath   = 'Y:/01_SAISON_4/09_EPISODES/04_Fabrication_3D/YKR513/sh002/ani/maya'
    print eipsodeTag, shotTag
    """







#------------------------------------------------------------------------------
# Module loaded!
Utils.moduleLoadedMessage()
#------------------------------------------------------------------------------
