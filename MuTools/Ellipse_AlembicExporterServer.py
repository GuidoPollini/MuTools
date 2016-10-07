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
import MuTools.MuMessaging as Messaging
import MuTools.MuUI        as UI

import maya.cmds           as MM
import maya.mel            as MM

import PySide.QtCore       as QC
import PySide.QtGui        as QG
import shiboken





#------------------------------------------------------------------------------
# Loading module...
Utils.moduleLoadingMessage()
#------------------------------------------------------------------------------









def initialize(clientPortId):
    print '>>> clientPortId', clientPortId

    Scene.disableViewport20()
    Scene.disableUI()
    MM.eval('renderThumbnailUpdate false;')

    mayaWindow = UI.mayaWindow()
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
        Messaging.sendMessage(clientPortId, 'Plugin [' + pluginName + '] loaded!')

    Messaging.sendMessage(clientPortId, 'LOADED')
    

    import time
    for i in range(10):
        Messaging.sendMessage(clientPortId, '<fuck you>')
        time.sleep(1)





#------------------------------------------------------------------------------
# Module loaded!
Utils.moduleLoadedMessage()
#------------------------------------------------------------------------------
