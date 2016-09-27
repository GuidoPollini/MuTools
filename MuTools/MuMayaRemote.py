__version__ = '1.0.0'



import MuTools.MuCore  as Core
import MuTools.MuScene as Scene
import MuTools.MuUI    as UI
import MuTools.MuUtils as Utils



#------------------------------------------------------------------------------
# Loading module...
Utils.moduleLoadingMessage()
#------------------------------------------------------------------------------














def initialize(*args):
    Scene.disableViewport20()
    Scene.disableUI()

    mayaWindow = UI.getMayaWindow()
    mayaWindow.setWindowTitle(' REMOTE MAYA')
    mayaWindow.setWindowIcon(QG.QIcon('C:/Users/guido.pollini/Desktop/muIcon.png'))
    











#------------------------------------------------------------------------------
# Module loaded!
Utils.moduleLoadedMessage()
#------------------------------------------------------------------------------
