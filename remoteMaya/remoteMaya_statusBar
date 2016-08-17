import PySide.QtGui as QG
import PySide.QtCore as QC
import shiboken
import maya.cmds as MC
import maya.OpenMayaUI as OMUI

class RemoteMayaStatusBar(QG.QLabel):
    def __init__(self, name):
        super(RemoteMayaStatusBar, self).__init__()
        
        if MC.control(name, query=True, exists=True):
            MC.deleteUI(name)
        
        # Apparently, this is the MayaName of the widget 
        # (the one you can use to kill it via the commandEngine)
        self.setObjectName(name)
        
        mayaWindowQWidget = shiboken.wrapInstance(long(OMUI.MQtUtil.mainWindow()), QG.QWidget)
        self.setParent(mayaWindowQWidget)
        
        width = 350
        self.setFixedSize(width, 14)
        self.move(mayaWindowQWidget.width() - width, 2)
        self.show()
 
        
    def setStatus(self, status, message):
        # The standard operation is 'clickMe' (except for waiting)
        cursor = QG.QCursor(QC.Qt.PointingHandCursor)
        
        if status == 'waiting':
            cursor = QG.QCursor(QC.Qt.WaitCursor) # In this case, you can't click!                        
            color           = (40, 40, 40)
            backgroundColor = (180, 180, 180) 
            message = '[waiting] ' + message
            
        elif status == 'success':
            color           = (0, 50, 0)
            backgroundColor = (150, 255, 150) 
            message = '[success] ' + message
            
        elif status == 'warning':
            color           = (50, 50, 0)
            backgroundColor = (255, 255, 150) 
            message = '[warning] ' + message
                 
        elif status == 'fatality':
            color           = (50, 0, 0)
            backgroundColor = (255, 150, 150) 
            message = '[fatality] ' + message
        
        styleSheet = 'margin:0px;' +\
                     'padding:0px 0px 0px 2px;' +\
                     'border-top-left-radius:7px;' +\
                     'border-bottom-left-radius:7px;' +\
                     'background-color: rgb' + str(backgroundColor) + ';' +\
                     'color: rgb' + str(color) + ';'
        
        self.setStyleSheet(styleSheet)             
        self.setText('<b>remoteMaya</b> ' + message)              
        self.setCursor(cursor)
        
shit = RemoteMayaStatusBar(name='XXX')
shit.setStatus('success', '...')
