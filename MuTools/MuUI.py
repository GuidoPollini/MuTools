__version__ = '1.0.1'
print '--> Executing MuUI...'



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


class MayaWindow(object):
    def __init__(self):
        pointer = OMUI.MQtUtil.mainWindow() # It's a QMainWindow, not simply a QWidget!
        self._mayaWindow = shiboken.wrapInstance(long(pointer), QG.QMainWindow)	    
    
    def __getattr__(self, attr):
        return getattr(self._mayaWindow, attr)

"""          
mw = MayaWindow()
# toolBar1 = menuSelection, load save icons, tabs selectors
# toolBar2 = shelf
# toolBar3 = helpLine
# toolBar4 = scriptLine
# toolBar5 = rangeAnim
# toolBar6 = timeslider
# toolBar7 = toolVertica
# dockControl1 = channelBox
# dockControl2 = ?
# dockControl3 = ?
# dockControl4 = attrEditor
# dockControl5 = toolProperties
for x in sorted(mw.children()):
    name = x.objectName() or '""'
    print '{0:>30.30}'.format(name), x
    if name == 'dockControl5':
        x.setStyleSheet('background-color: cyan; color: black;')
class MayaWindow(object):
    def __new__(cls):
        pointer = OMUI.MQtUtil.mainWindow() # It's a QMainWindow, not simply a QWidget!
        return shiboken.wrapInstance(long(pointer), QG.QMainWindow)	    
"""


def mayaWindow():
    pointer = OMUI.MQtUtil.mainWindow() # It's a QMainWindow, not simply a QWidget!
    return shiboken.wrapInstance(long(pointer), QG.QMainWindow) 
    






#------------------------------------------------------------------------------
# Module loaded!
Utils.moduleLoadedMessage()
#------------------------------------------------------------------------------
