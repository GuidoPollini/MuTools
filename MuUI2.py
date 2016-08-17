import maya.OpenMayaUI as OMUI
import maya.cmds       as MC
import PySide.QtGui    as QG
import PySide.QtCore   as QC
import shiboken
import functools



def getMayaWindow():
    pointer = OMUI.MQtUtil.mainWindow()
    return shiboken.wrapInstance(long(pointer), QG.QWidget)
    

class Color(object):
    def __init__(self, r, g, b):
        self.RGB = [r, g, b]
        self._clamp()
    
    def __getitem__(self, index):
        return self.RGB[index]
        
    def __setitem__(self, index, value):
        self.RGB[index] = value
        self._clamp()
    
    def _clamp(self):
        self.RGB = [max(min(x, 255), 0) for x in self.RGB]
        return self
                
    def __str__(self):
        # Reprentation compatible with styleSheets    
        return "rgb" +str(tuple(self.RGB))

    def __add__(self, otherColor):
        # Accept: <Color>, <list>, <tuple>
        return Color(self.RGB[0] + otherColor[0], 
                     self.RGB[1] + otherColor[1],
                     self.RGB[2] + otherColor[2])          
              
              
class Button(QG.QPushButton):
    def __init__(self, name=None, parent=None, text="...", 
                       click_callback=None, baseColor=Color(100, 100, 100)):
        super(Button, self).__init__(parent=parent)
        if name:
            self.setObjectName(name)
        self.setText(text)
        self.setCursor(QC.Qt.PointingHandCursor)
        if click_callback:
            print "connected"
            self.clicked.connect(click_callback)
        hoverColor   = baseColor + [30, 30, 30]
        pressedColor = baseColor + [80, 80, 80]
        styleSheet = """
            QPushButton{
                margin: 0px;
                padding: 0px;
                font-size: 20px; 
                border-radius: """ + str(int(self.height()/2.0)) + """px; 
                background-color: """ + str(baseColor) + """;
            }
            
            QPushButton:hover{
                background-color: """ + str(hoverColor) + """;
            }      
            
            QPushButton:pressed{
                background-color: """ + str(pressedColor) + """;
                padding: 0px;
            }
        """            

        # ==> ALTERNATIVE <==

        styleSheet = """
            QPushButton{{
                margin: 0px;
                padding: 0px;
                font-size: 20px; 
                border-radius: {borderRadius}px; 
                background-color: {baseColor};
            }}
            
            QPushButton:hover{{
                background-color: {hoverColor};
            }}      
            
            QPushButton:pressed{{
                background-color: {pressedColor};
                padding: 0px;
            }}
        """.format(borderRadius=int(self.height()/2.0), baseColor=baseColor, hoverColor=hoverColor, pressedColor=pressedColor)        
        self.setStyleSheet(styleSheet)

    

    
class Window(QG.QWidget):
    #-----------------------------
    # CONSTRUCTOR
    #-----------------------------          
    def __init__(self, windowName):
        # 'windowName' is the unique name
        if MC.control(windowName, query=True, exists=True):
            MC.deleteUI(windowName)
            
        super(Window, self).__init__()
        self.setParent(getMayaWindow())
        
        
        # Maya name of the QWidget
        self.setObjectName(windowName)
        
        
        # It's a top level Widget with no titleBar
        self.setWindowFlags(QC.Qt.Window | QC.Qt.CustomizeWindowHint)
        
        
        # Geometry
        self.setMinimumSize(200, 100)
        self.resize(400, 200)
        self.setStyleSheet('background-color:rgb(49, 49, 49);')
        
        mainLayout = QG.QVBoxLayout(self)
        mainLayout.setSpacing(0)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        
        
        button1 = QG.QPushButton("ONE")
        button2 = QG.QPushButton("ONE")
        button3 = QG.QPushButton("ONE")
        button4 = QG.QPushButton("ONE")

        mainLayout.addWidget(button1)
        mainLayout.addWidget(button2)
        mainLayout.addWidget(button3)
        mainLayout.addWidget(button4)
        
        button = Button(text="fuck you")
        mainLayout.addWidget(button)        
        
        # Name appearing when in the system tray (usually invisible)
        self.setWindowTitle(windowName)
        
        
        # Show it:)
        self.show()
        
        
        
    #-----------------------------
    # METHODS
    #-----------------------------  
    def minimize(self):
        self.showMinimized()



    #-----------------------------
    # OVERRIDES OF C++ VIRTUALS
    #-----------------------------  
    def mousePressEvent(self, event):
        if event.button() == QC.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
            
            
    def mouseMoveEvent(self, event):
        if event.buttons() == QC.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()        
            
myWin1 = Window(windowName='TEST')  
#myWin1.minimize()      
