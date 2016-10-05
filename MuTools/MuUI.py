__version__ = '1.0.1'



import MuTools.MuUtils as Utils

import maya.cmds       as MC
import maya.OpenMayaUI as OMUI

import PySide.QtCore   as QC
import PySide.QtGui    as QG
import shiboken



#------------------------------------------------------------------------------
# Loading module...
Utils.moduleLoadingMessage()
#------------------------------------------------------------------------------








def mayaWindow():
    pointer = OMUI.MQtUtil.mainWindow() # It's a QMainWindow!
    return shiboken.wrapInstance(long(pointer), QG.QMainWindow) 
    






#------------------------------------------------------------------------------
# Module loaded!
Utils.moduleLoadedMessage()
#------------------------------------------------------------------------------
