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
       

def mayaWindow():
    pointer = OMUI.MQtUtil.mainWindow() # It's a QMainWindow, not simply a QWidget!
    return shiboken.wrapInstance(long(pointer), QG.QMainWindow) 
    

class RemoteMayaIcon(QG.QPushButton):
    def __init__(self):
        mayaWin = mayaWindow()
        parent = mayaWin.findChild(QG.QWidget, 'MainStatusLineLayout')    
        
        iconName = '_RemoteMayaIcon'

        if MC.control(iconName, exists=True):
            print '>>> _RemoteMayaIcon deleted!'
            MC.deleteUI(iconName)
        
        super(RemoteMayaIcon, self).__init__('?', parent=parent)
        self.setObjectName(iconName)
        self.setFixedSize(26, 26)
        self.setStyleSheet('font-size:20px;')
        self.move(parent.width() - 26 * 5, 0)
        self.setInactive()
        self.show()
    
        self.clicked.connect(self._clicked)



    def _clicked(self):
        print 'CLICKED', self.objectName()



    def setInactive(self):
        self.setStyleSheet("""
            background-color:rgb(80, 80, 80);
            color: rgb(30, 30, 30); 
        """)



    def setSuccess(self):
        self.setStyleSheet("""
            background-color:rgb(80, 255, 80);
            color: rgb(30, 30, 30); 
        """)



    def setFatality(self):
        self.setStyleSheet("""
            background-color:rgb(255, 100, 80);
            color: rgb(30, 30, 30); 
        """)




#------------------------------------------------------------------------------
# Module loaded!
Utils.moduleLoadedMessage()
#------------------------------------------------------------------------------











"""
w = mayaWindow()

# Get the rightmost widget holding the 4 QPushButtons ('attrEditor', 'channelBox', 'tools', ...)
mainStatusLineWidget = mw.findChild(QG.QWidget, 'MainStatusLineLayout')
attributeEditorPushButton = mainStatusLineWidget.findChild(QG.QPushButton, 'attributeEditorButton')
# The parent should be the QWidget named 'formLayout8'... But Don't trust Maya:)

 "toolBar1" PySide.QtGui.QToolBar
     "MainStatusLineLayout" PySide.QtGui.QWidget
       "MainStatusLineLayout" PySide.QtGui.QLayout
       "formLayout5" PySide.QtGui.QWidget
       
parentWidget = attributeEditorPushButton.parent().parent() # This is the bar: 'formLayout5'
print parentWidget.objectName()
#parentWidget.setFixedHeight(27)
newNames = ['_newButton']
for x in newNames:
    try:
        MC.deleteUI(x)
        print x, 'deleted!'
    except Exception as exc:
        pass


_newButton = QG.QPushButton('X', parentWidget)
_newButton.setObjectName('_newButton')
_newButton.setFixedSize(40, 40)
_newButton.setStyleSheet('background-color:rgb(130, 255, 130); color:black;')
#parentWidget.layout().addWidget(_newButton)
_newButton.show()
_newButton.move(1500, 0)

"""


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

