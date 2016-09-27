__version__ = '1.0.0'



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








def getMayaWindow():
    pointer = OMUI.MQtUtil.mainWindow()
    return shiboken.wrapInstance(long(pointer), QG.QWidget)
    






#------------------------------------------------------------------------------
# Module loaded!
Utils.moduleLoadedMessage()
#------------------------------------------------------------------------------
