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
    """
    Just a namespace to manipulate Maya window...
    """
    @staticmethod
    def mainWindow():
        pointer = OMUI.MQtUtil.mainWindow() # It's a QMainWindow, not simply a QWidget!
        return shiboken.wrapInstance(long(pointer), QG.QMainWindow)	    
  





class RemoteMayaIcon(QG.QPushButton):
    """
    remoteMayaIcon = UI.RemoteMayaIcon('myIconPath_26x26')
    remoteMayaIcon.clicked.connect(myCustomSlot)

    """



    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    By setting the entire styleSheet you reset the static attributes;
    you need a direct way to set the styleSheet without using the string...
    QPalette doesn't seem to work!

    It works, but apparently it's incompatible with a styleSheet with 'borders'
    overrides... just FUCK YOU

    NO! Replace the shitty background, with an overlay in ADD and animate that
        shit... one icon, with pulsating color!
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


    #-----------------------------
    # INITIALIZER
    #-----------------------------    
    def __init__(self, iconPath):
        mayaWin = MayaWindow.mainWindow()
        parent = mayaWin.findChild(QG.QWidget, 'MainStatusLineLayout') 


        # Private attributes
        self._iconName  = '_RemoteMayaIcon' # Maya name
        self._pulsation = None
        self._status    = None


        if MC.control(self._iconName, exists=True):
            MC.deleteUI(self._iconName)
        
        super(RemoteMayaIcon, self).__init__(parent=parent)

        self.setObjectName(self._iconName)
        self.setIcon(QG.QIcon(iconPath))
        
        self.setFixedSize(26, 26)
        self.move(parent.width() - 26 * 5, 0)
        
        self.setDisabledStatus()
        self.clicked.connect(self._clicked)

        # Show it        
        self.show()
    


    def setStatus(self, status):
        """
        Check the status and create the QPropertyAnimation object and 
        activate it (if the status needs it).
        """

        neutralColor = (68, 68, 68)
        visualStatusData = {
            'default': {
                'baseColor': (80, 80, 80),
                'colorAnimation': None,
                'cursor': QC.Qt.PointingHandCursor,
                'enabled': True                                
            },

            'waiting': {
                'baseColor': neutralColor,
                'colorAnimation': {
                    0.00: neutralColor,
                    0.50: (110, 110, 110),
                    1.00: neutralColor   
                }, 
                'cursor': QC.Qt.WaitCursor,
                'enabled': True                                                           
            },

            'warning': {
                'baseColor': neutralColor,
                'colorAnimation': {
                    0.00: neutralColor,
                    0.65: neutralColor,
                    0.70: (200, 200, 100), 
                    1.00: neutralColor   
                }, 
                'cursor': QC.Qt.PointingHandCursor,
                'enabled': True                           
            },

            'fatality': {
                'baseColor': (0, 0, 0),
                'colorAnimation': {
                    0.00: neutralColor,
                    0.30: (255, 100, 100),
                    0.50: (255, 180, 100),
                    1.00: neutralColor      
                }, 
                'cursor': QC.Qt.PointingHandCursor, 
                'enabled': True                
            },

            'disabled': {
                'baseColor': neutralColor,
                'colorAnimation': None, 
                'cursor': QC.Qt.ArrowCursor, 
                'enabled': False
            },

            'success': {
                'baseColor': (0, 0, 0),
                'colorAnimation': {
                    0.00: neutralColor,
                    0.30: (100, 155, 100),
                    0.50: (200, 255, 120),
                    1.00: neutralColor   
                },  
                'cursor': QC.Qt.PointingHandCursor, 
                'enabled': True
            }            
        }
        

        if status not in visualStatusData:
            MC.error('[FATAL] The status "{0}" is unknown!\nPossible choices: {1}!'.format(status, ', '.join(visualStatusData)))

        self._status = status
        statusData = visualStatusData[status]

        if self._pulsation:
            # There's already an animation object; by using the start policy
            # 'QC.QAbstractAnimation.DeleteWhenStopped' when stopped it should be destroyed
            self._pulsation.stop()
            self._pulsation = None


        # Set the cursor
        self.setCursor(statusData['cursor'])
        
        # Enable/disable
        self.setEnabled(statusData['enabled'])

        if statusData['colorAnimation']:
            # The status requires a color pulsation
            self._pulsation = QC.QPropertyAnimation(self, '_pulsationProperty')  

            animationCurve = statusData['colorAnimation']      
            for key in animationCurve:
                self._pulsation.setKeyValueAt(key, QG.QColor(*animationCurve[key]))

            self._pulsation.setDuration(1000)
            self._pulsation.setLoopCount(-1)
            #??? self._pulsation.setEasingCurve(QC.Qt.QEasingCurve.Linear)
            self._pulsation.start(policy=QC.QAbstractAnimation.DeleteWhenStopped)
        
        else:
            # No color pulsation: set the base color
            colorString = str(QG.QColor(*statusData['baseColor']).getRgb())
            self.setStyleSheet('background-color: rgb' + colorString)


    def _pulsationPropertyGetter(self):
        return self.palette().color(QG.QPalette.Window)



    def _pulsationPropertySetter(self, color):
        #pal = self.palette()
        #pal.setColor(QG.QPalette.Window, color)
        #self.setPalette(pal)
        
        #print self.styleSheet()
        #print pal.color(QG.QPalette.Button)
        #print pal.color(QG.QPalette.Base)
        
        self.setStyleSheet("""
            border-radius: 12px; 
            border-width: 0px; 
            background-color: rgb""" + str(color.getRgb()) + """;
            margin: 0px;
            padding: 0px;
        """)


    _pulsationProperty = QC.Property(QG.QColor, _pulsationPropertyGetter, _pulsationPropertySetter)        




    #-----------------------------
    # SLOTS
    #-----------------------------
    def _clicked(self):
        print 'CLICKED', self.status()




    #-----------------------------
    # METHODS
    #-----------------------------
    def setDefaultStatus(self):
        self.setStatus('default')


    def setWaitingStatus(self):
        self.setStatus('waiting')


    def setDisabledStatus(self):
        # '.setDisabled' is a method of QPushButton...
        self.setStatus('disabled')


    def setWarningStatus(self):
        self.setStatus('warning')


    def setSuccessStatus(self):
        self.setStatus('success')


    def setFatalityStatus(self):
        self.setStatus('fatality')


    def status(self):
        return self._status

    def destroyIcon(self):
        MC.deleteUI(self._iconName)




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

