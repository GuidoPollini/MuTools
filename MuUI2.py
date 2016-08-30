import maya.cmds       as MC
import maya.OpenMayaUI as OMUI

import PySide.QtGui    as QG
import PySide.QtCore   as QC
import shiboken

import functools
import os
import time





print '[{0}.py] Loading module from "{1}"...'.format(__name__, __file__)


"""
def visitQObject(qObj, depth):
    objectName = qObj.objectName()
    tipo = str(qObj).lstrip('<').split(' ')[0]
    print '  '*depth, ('"' + objectName + '"' if objectName != '' else "...", tipo
            
    for c in qObj.children():
        visitQObject(c, depth + 1)    
    
    
visitQObject(getMayaWindow(), 0) 
"""

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
        """.format(borderRadius=12, baseColor=baseColor, hoverColor=hoverColor, pressedColor=pressedColor)        
        self.setStyleSheet(styleSheet)





"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
---------------------------------------------------------------------------------------------------
QtCore.QObject
---------------------------------------------------------------------------------------------------
__init__([parent=None])


  .objectName()             <str>
  .setObjectName(<str>)     <>
  --------------------------------------------------------------
  The objectName is only a property of a QObject; by default it's "" and can be not unique 


  .parent()                 <QObject>
  .setParent(<QObject>)     <>


  .children()                               <list of <QObject>>
  .findChild(<PyTypeObject> [, <str>])      <QObject>
  .findChildren(<PyTypeObject> [, <str>])   <list of <QObject>>
  .findChildren(<PyTypeObject> [, REGEXP])  <list of <QObject>>
  ---------------------------------------------------------------
  Example: found = self.findChildren(QG.QWidget)


  .isWidgetType()           <bool>
  (C++) .isWindowType()     <bool>


  .inherits(<class>)        <bool>





---------------------------------------------------------------------------------------------------
QtGui.QWidget
---------------------------------------------------------------------------------------------------
__init__([parent=None[, windowFlags=0]])

   
  .geometry()                      <QC.QRect>
  .setGeometry(x, y, w, h)
  ----------------------------------------------------
  It's still relative, but no window offset...


  .setMinimumSize(<int>, <int>)
  .setMaximumSize(<int>, <int>)
  .setFixedSize(<int>, <int>)
  .resize(<int>, <int>)
  .size()                          <QC.QSize>
  ----------------------------------------------------
  Ex: w, h = self.size().width(), self.size().height()


  .move(<int>, <int>)
  .pos()                    <QPoint>
  .x()                      <int>
  .y()                      <int>
  ----------------------------------------------------
  Position relative to its widget parent; for a window, relative to the desktop!
  They are NOT relative coordinates!!! So you need Maya window's position to relativize!
  Moreover, when Maya window is maximized, pos is wrong:
  mayaPosition = getMayaWindow().pos()
  self.move(mayaPosition) # Bad when maximized!!!  
  

  .parentWidget()           <QWidget>
  .window()                 <QWidget> 
  

  .setWindowFlags(<QC.Qt.WindowFlags>)
  .windowFlags()                         <QC.Qt.WindowFlags>
  ----------------------------------------------------
  It's just a wrap for a bitField; use '{0:b}'.format(int(...)) to recover the bits. Ex: 
  QC.Qt.Window | QC.Qt.CustomizeWindowHint --> 10000000000000000000000001
  QC.Qt.Window                             --> 00000000000000000000000001
  QC.Qt.CustomizeWindowHint                --> 10000000000000000000000000



---------------------------------------------------------------------------------------------------
Alignments
---------------------------------------------------------------------------------------------------
  QC.Qt.AlignLeft    
       .AlignRight   
       .AlignHCenter 
       .AlignJustify  

       .AlignTop 
       .AlignBottom  
       .AlignVCenter 

       .AlignCenter  


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""




class Window(QG.QWidget):
    #-----------------------------
    # INITIALIZER
    #-----------------------------          
    def __init__(self, windowName):
        #-----------------------------------------------------------------------
        # Creation
        #-----------------------------------------------------------------------        
        # 'windowName' is the unique name
        if MC.control(windowName, query=True, exists=True):
            MC.deleteUI(windowName)
        super(Window, self).__init__(getMayaWindow())
        #self.setParent(getMayaWindow())
        

        #-----------------------------------------------------------------------
        # Window
        #-----------------------------------------------------------------------
        # Maya name of the QWidget
        self.setObjectName(windowName)
        # It's a top level Widget with no titleBar
        self.setWindowFlags(QC.Qt.Window | QC.Qt.CustomizeWindowHint)
        # Name appearing when in the system tray (usually invisible)
        self.setWindowTitle(windowName)


        #-----------------------------------------------------------------------
        # Geometry
        #-----------------------------------------------------------------------
        # Origin
        mayaPosition = getMayaWindow().pos()
        self.move(mayaPosition + QC.QPoint(100, 100))
        # Size
        self.setMinimumSize(300, 300)
        self.resize(300, 600)


        #-----------------------------------------------------------------------
        # Style
        #-----------------------------------------------------------------------
        self.setStyleSheet('background-color:rgb(49, 49, 49);')


        #-----------------------------------------------------------------------
        # Layout
        #-----------------------------------------------------------------------
        mainLayout = QG.QVBoxLayout(self)
        mainLayout.setSpacing(0)
        mainLayout.setContentsMargins(0, 0, 0, 0)

        #-----------------------------------------------------------------------
        # Content
        #-----------------------------------------------------------------------
        titleBar = QG.QLabel('Alembic export')
        titleBar.setObjectName('_windowTitleBar')
        titleBar.setAlignment(QC.Qt.AlignHCenter)

        titleBar.setFixedHeight(26)
        titleBar.setStyleSheet("""
            background-color:rgb(49,160,180); 
            color:rgb(30,30,30);
            font-size:20px;
        """)
        mainLayout.addWidget(titleBar)

        
        horizontalShit = QG.QWidget()
        #horizontalShit.setFixedHeight(20)
        mainLayout.addWidget(horizontalShit)

        horizontalLayout = QG.QHBoxLayout(horizontalShit)
        horizontalLayout.setSpacing(2)
        horizontalLayout.setContentsMargins(2, 2, 2, 2)

        for i in range(5):
            shit = QG.QPushButton()
            shit.setFixedSize(20, 20)
            shit.setStyleSheet('background-color:rgb(49,160,180);') 
            horizontalLayout.addWidget(shit)
        horizontalLayout.addStretch(1)
        
        shit = QG.QPushButton()
        shit.setFixedSize(20, 20)
        shit.setStyleSheet('background-color:rgb(255,160,180);') 
        horizontalLayout.addWidget(shit)        


        browser = QG.QTextBrowser()
        #browser.setFixedHeight(200)
        mainLayout.addWidget(browser)

        for i in range(5):
            button = Button(text='XXX' + str(i), baseColor=Color(100, 100 + i * 5, 100))
            mainLayout.addWidget(button)
                

        
        # Show it:)
        self.show()
        


        
    #-----------------------------
    # METHODS
    #-----------------------------  
    def minimize(self):
        self.showMinimized()


    def inspect(self):
        print 'geo:', self.geometry()
        print 'pos:', self.pos()





    #-----------------------------
    # OVERRIDES OF C++ VIRTUALS
    #-----------------------------  
    def mousePressEvent(self, event):
        self.isDragged = False
        clickedObject = self.childAt(event.pos())
        if clickedObject and clickedObject.objectName() == '_windowTitleBar':
            if event.button() == QC.Qt.LeftButton:
                self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
                self.isDragged = True
                event.accept()
        else:
            event.ignore()
            
    def mouseMoveEvent(self, event):
        if self.isDragged and event.buttons() == QC.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()        
    
    def mouseReleaseEvent(self, event):
        self.isDragged = False      




def run(*args):            
    myWin = Window(windowName='TEST') 
    myWin.inspect() 
    #myWin.minimize()      




t = os.path.getmtime(__file__) # Seconds passed between Epoch and last modification 
formattedTime = time.strftime("%d/%m/%y, %H:%M:%S", time.localtime(t))
print '[{0}.py] SUCCESS: module loaded! Last update {1}.'.format(__name__, formattedTime)

