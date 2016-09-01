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

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
C++ version (SIGNAL and SLOT are macro?):
  QObject::connect(comboObj, SIGNAL(currentIndexChanged(QString)), labelObj, SLOT(setText(QString)));

Python (first form)
  obj.signalName.connect(callableName_default)
  obj.signalName[type1].connect(callableName_type1)
  obj.signalName[type2].connect(callableName_type2)


NOTE:
  'Signals' are indeed <PySide.QtCore.SignalInstance> objects, apparently related to QC.Signals;
  they implement (if needed) 'getitem', useful to resolve C++ overloads.
  In cas of overloads, chose the right Python type and:

    obj.overloadedSignal(PYTHON_TYPE).connect(whatever)
    comboBox.currentIndexChanged[int].connect(changed_int)
    comboBox.currentIndexChanged[str].connect(changed_str)

  Note that .connect is a method of QC.Signal, exceptional to 'signals', not to other bounds methods  
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""




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
   


class PushButton(QG.QPushButton):
    def __init__(self, text='',
                       fontSize=20,
                       baseColor=Color(98, 98, 98),
                       fixedWidth=None,
                       fixedHeight=None,
                       clicked_slot=None, 
                       parentObject=None):

        super(PushButton, self).__init__()
        self.setText(text)
        self.setCursor(QC.Qt.PointingHandCursor)

        hoverColor   = baseColor + [20, 20, 20]
        pressedColor = baseColor + [40, 40, 40]
       
        styleSheet = """
            QPushButton{{
                margin: 0px;
                padding: 0px;
                font-size: {fontSize}px; 
                border-radius: {borderRadius}px; 
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(98, 98, 98),  stop:1.0 rgb(94, 94, 94));
                border-style: outset;
                border-width: 1px;
                border-color: rgb(35, 35, 35);
            }}
            
            QPushButton:hover{{
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(110, 130, 180), stop:0.2 rgb(110, 110, 110),  stop:1.0 rgb(98, 98, 98));
            }}      
            
            QPushButton:pressed{{
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(110, 150, 200), stop:0.2 rgb(130, 130, 130),  stop:1.0 rgb(110, 110, 110));
                padding: 0px;
            }}
        """.format(fontSize=fontSize, borderRadius=4, baseColor=baseColor, hoverColor=hoverColor, pressedColor=pressedColor)     

        self.setStyleSheet(styleSheet)

        if fixedWidth:
            self.setFixedWidth(fixedWidth)

        if fixedHeight:
            self.setFixedHeight(fixedHeight)

        if clicked_slot:
            self.clicked.connect(clicked_slot)

        if parentObject:
            parentObject.addWidget(self)



class CheckBox(QG.QCheckBox):
    def __init__(self, text='',
                       initialChecked=False,
                       stateChanged_slot=None,
                       parentObject=None):

        super(CheckBox, self).__init__(text)
        self.setChecked(initialChecked)
        self.setCursor(QC.Qt.PointingHandCursor) # It's clickable:)       

        if parentObject:
            parentObject.addWidget(self)

        if stateChanged_slot:
            self.stateChanged.connect(stateChanged_slot)



class LabelComboBox(QG.QWidget):
    """
    |QLabel QComboBox|
    """
    def __init__(self, text='', 
                       itemList=[], 
                       align='left', 
                       comboBoxFixedWidth=None,
                       labelFixedWidth=None,
                       currentIndexChanged_slot=None, 
                       parentObject=None):

        super(LabelComboBox, self).__init__()

        layout = QG.QHBoxLayout(self)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        comboBox = QG.QComboBox()
        comboBox.setCursor(QC.Qt.PointingHandCursor) # It's clickable:)  
        if comboBoxFixedWidth:
            comboBox.setFixedWidth(comboBoxFixedWidth)
        comboBox.addItems(itemList)


        label = QG.QLabel(text)
        layout.addWidget(label)
        possibleAligns = {'left':   QC.Qt.AlignLeft,
                          'center': QC.Qt.AlignHCenter,
                          'right':  QC.Qt.AlignRight
        }
        label.setAlignment(possibleAligns[align])
        if labelFixedWidth:
            label.setFixedWidth(labelFixedWidth)
        layout.addWidget(comboBox)
        
        # Attach to the object
        self.label    = label
        self.comboBox = comboBox

        # Selection changed   
        if currentIndexChanged_slot:
            """ Note the [] (getitem) used on the signal to choose the needed C++ overload """                     
            self.comboBox.currentIndexChanged[str].connect(currentIndexChanged_slot)

        # Add to a layout
        if parentObject:
            parentObject.addWidget(self)



    def setLabel(self, newLabel):
        self.label.setText(newLabel)
        return self

    def setItems(self, itemList):
        self.comboBox.clear()
        self.comboBox.addItems(itemList) 
        return self    

    def closeEvent(self, event):
        print 'closeEvent for', self
        event.accept()


class Log(QG.QGroupBox):
    """
    |   QLabel   |
    |QTextBrowser|
    """

    def __init__(self, title='...', 
                       parentObject=None):
        super(Log, self).__init__()
        self.setTitle('Log')   
        self.setStyleSheet("""
            color:rgb(140,140,140);
            font-size: 12px;
        """)

        layout = QG.QVBoxLayout(self)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        self.textEdit = QG.QTextEdit()
        self.textEdit.setAcceptRichText(True)
        self.textEdit.setReadOnly(True)
        self.textEdit.setStyleSheet("""
            background-color: rgb(48, 48, 48);
            color:rgb(200,200,200);
            font-size: 13px;
        """)
        self.textEdit.setText('Ready to go...')

        layout.addWidget(self.textEdit)

        if parentObject:
            parentObject.addWidget(self) 
    
    def _appendText(self, message):
        message += ""
        self.textEdit.append(message)

    def normal(self, message):
        self.textEdit.append(message)

    def success(self, message):
        message = '<b><font color="#CCFFCC">Success </font></b><font color="#AAFFAA">' + message + '</font>'
        self.textEdit.append(message)

    def warning(self, message):
        message = '<b><font color="#FFFFCC">Warning </font></b><font color="#FFFFAA">' + message + '</font>'
        self.textEdit.append(message)

    def fatality(self, message):
        message = '<b><font color="#FFCCCC">Fatality </font></b><font color="#FFAAAA">' + message + '</font>'
        self.textEdit.append(message)


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
        self.setWindowFlags(QC.Qt.Window)#| QC.Qt.CustomizeWindowHint)
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
        # Generic style
        #-----------------------------------------------------------------------
        self.setStyleSheet('font-size:14px;')


        #-----------------------------------------------------------------------
        # Layout
        #-----------------------------------------------------------------------
        mainLayout = QG.QVBoxLayout(self)
        mainLayout.setSpacing(0)
        mainLayout.setContentsMargins(0, 0, 0, 0)

        #-----------------------------------------------------------------------
        # TitleBar
        #-----------------------------------------------------------------------
        titleBar = QG.QLabel('Alembic export')
        titleBar.setObjectName('_windowTitleBar')
        titleBar.setAlignment(QC.Qt.AlignHCenter)

        titleBar.setFixedHeight(24)
        titleBar.setStyleSheet("""
            background-color:rgb(115, 192, 255); 
            color:rgb(30,30,30);
            font-size:18px;
            padding: 0px 0px 2px 0px;
        """)
        mainLayout.addWidget(titleBar)

    
    

        #-----------------------------------------------------
        # Episode selector
        #-----------------------------------------------------
        episodeList = ['...', 'YKR000', 'YKR666', 'YKR123', 'YKRfuck', 'YKR999', 'YKRNope', 'YKRWow', 'YKRKY']        
        self.episodeSelector = LabelComboBox(
            text='Select an <b>episode</b>:', 
            itemList=episodeList, 
            align='right', 
            labelFixedWidth=140,             
            comboBoxFixedWidth=86,           
            currentIndexChanged_slot=self.currentEpisodeChanged_slot, 
            parentObject=mainLayout
        ) 


        #-----------------------------------------------------
        # Shot selector
        #-----------------------------------------------------        
        shotList = []
        self.shotSelector = LabelComboBox(
            text='Select a <b>shot</b>:', 
            itemList=shotList, 
            align='right', 
            labelFixedWidth=140,             
            comboBoxFixedWidth=86,             
            currentIndexChanged_slot=None, #self.currentShotChanged_slot,
            parentObject=mainLayout
        )
        self.shotSelector.setDisabled(True)



        self.checkMe = CheckBox(
            text='Check me hard:)',
            initialChecked=True,
            stateChanged_slot=None,
            parentObject=mainLayout
        )
        self.checkMe.setDisabled(True)


        self.exportButton = PushButton(
            text='EXPORT',
            #baseColor=Color(100, 100, 100),
            fixedWidth=100,
            fixedHeight=24,
            #clicked_slot=None, 
            parentObject=mainLayout)
        self.exportButton.setDisabled(True)


        self.fixAllButton = PushButton(
            text='Fix all',
            #baseColor=Color(100, 100, 100),
            fixedWidth=100,
            fixedHeight=24,
            #clicked_slot=None, 
            parentObject=mainLayout)
        self.fixAllButton.setDisabled(True)


        self.fixAllButton = PushButton(
            text='Fix all',
            #baseColor=Color(100, 100, 100),
            fixedWidth=100,
            fixedHeight=24,
            #clicked_slot=None, 
            parentObject=mainLayout)
        self.fixAllButton.setDisabled(True)
        
        
        self.selectAllButton = PushButton(
            text='Select all',
            fontSize=16,
            fixedWidth=100,
            fixedHeight=24,
            #clicked_slot=None, 
            parentObject=mainLayout)
        self.selectAllButton.setDisabled(True)

        self.deselectAllButton = PushButton(
            text='Deselect all',
            fontSize=16,
            fixedWidth=100,
            fixedHeight=24,
            #clicked_slot=None, 
            parentObject=mainLayout)
        self.deselectAllButton.setDisabled(True)



        splitter = QG.QSplitter()
        splitter.setOrientation(QC.Qt.Vertical)
        
        edit = QG.QTextEdit()
        splitter.addWidget(edit)


        self.consoleLog = Log(
            parentObject=splitter
        )

        for i in range(40):
            self.consoleLog.normal('Just fuck you... ' + str(i))
            self.consoleLog.success('Just fuck you... ' + str(i))
            self.consoleLog.warning('Just fuck you... ' + str(i))
            self.consoleLog.fatality('Just fuck you... ' + str(i))
        mainLayout.addWidget(splitter)




                

        
        # Show it:)
        self.show()
        


        
    #-----------------------------
    # METHODS
    #----------------------------- 
    def currentEpisodeChanged_slot(self, newEpisode):
        if newEpisode != '...':

            # Semantically this is wrong: add a 'firstTime' flag and do ONCE this check!
            i = self.episodeSelector.comboBox.findText('...')
            if i != -1:
                self.episodeSelector.comboBox.removeItem(i)

            # Reenable everything
            self.shotSelector.setDisabled(False)
            self.checkMe.setDisabled(False) 
            self.selectAllButton.setDisabled(False)
            self.exportButton.setDisabled(False)

            array = range(10)
            strArray = [newEpisode + '_' + str(x) for x in array]
            self.shotSelector.setItems(strArray)



    def currentShotChanged_slot(self, textItem):
        print 'current shot:', textItem
    


    def dock(self):
        if MC.dockControl('alembicExportDock', query=True, exists=True):
            MC.deleteUI('alembicExportDock')

        """ 
        THIS DON'T MAKE ANY FUCKING SENSE...
        The first time it works without ths SHIT window; the second time it fails...
        The paneLayout is a layout which must be attached to something... A REFRESH NEEDED???
         FUCK YOU SO HARD...
        """    

        if MC.window('SHIT', ex=True):
            MC.deleteUI('SHIT')    
        MC.window('SHIT')
        floating = MC.paneLayout(configuration='single', width=400, height=300)
        MC.dockControl('alembicExportDock', area='right', allowedArea=['right', 'left'], content='SHIT', label='Alembic export')
        
        MC.control('TEST', e=True, p=floating)
        
        MC.refresh()
        MC.dockControl('alembicExportDock', e=True, r=True) # Raise


    def minimize(self):
        self.showMinimized()


    def inspect(self):
        print 'geo:', self.geometry()
        print 'pos:', self.pos()





    #-----------------------------
    # OVERRIDES OF C++ VIRTUALS
    #-----------------------------  
    """
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
    """



def run(*args):
    myWin = Window(windowName='TEST')
    myWin.dock()

    #myWin.minimize()      




t = os.path.getmtime(__file__) # Seconds passed between Epoch and last modification 
formattedTime = time.strftime("%d/%m/%y, %H:%M:%S", time.localtime(t))
print '[{0}.py] SUCCESS: module loaded! Last update {1}.'.format(__name__, formattedTime)


"""
import os
muPath = r"C:\Users\guido.pollini\Desktop\MuTools"
if muPath not in os.sys.path:
    os.sys.path.append(muPath)

import MuUI2
reload(MuUI2)
MuUI2.run()

"""


"""
# DOCK AND UNDOCK, you get this shit
   "alembicExportDock" PySide.QtGui.QDockWidget
     "alembicExportDock" PySide.QtGui.QLayout
     "qt_dockwidget_floatbutton" PySide.QtGui.QAbstractButton
     "qt_dockwidget_closebutton" PySide.QtGui.QAbstractButton
     ... PySide.QtCore.QObject
     ... PySide.QtGui.QAction
     "floating" PySide.QtGui.QWidget
       "floating" PySide.QtGui.QVBoxLayout
       "mayaLayoutInternalWidget" PySide.QtGui.QSplitter
         "TEST" MuUI2.Window
           ... PySide.QtGui.QVBoxLayout
           "_windowTitleBar" PySide.QtGui.QLabel
           ... PySide.QtGui.QWidget
             ... PySide.QtGui.QHBoxLayout
             ... PySide.QtGui.QPushButton
             ... PySide.QtGui.QPushButton
             ... PySide.QtGui.QPushButton
             ... PySide.QtGui.QPushButton
             ... PySide.QtGui.QPushButton
             ... PySide.QtGui.QPushButton
           ... PySide.QtGui.QTextBrowser
             "qt_scrollarea_viewport" PySide.QtGui.QWidget
             "qt_scrollarea_hcontainer" PySide.QtGui.QWidget
               ... PySide.QtGui.QScrollBar
               ... PySide.QtGui.QBoxLayout
             "qt_scrollarea_vcontainer" PySide.QtGui.QWidget
               ... PySide.QtGui.QScrollBar
               ... PySide.QtGui.QBoxLayout
             ... PySide.QtCore.QObject
               ... PySide.QtGui.QTextDocument
                 ... PySide.QtGui.QAbstractTextDocumentLayout
                   ... PySide.QtCore.QObject
                 ... PySide.QtGui.QTextFrame
           ... MuUI2.Button
           ... MuUI2.Button
           ... MuUI2.Button
           ... MuUI2.Button
           ... MuUI2.Button
         "qt_splithandle_TEST" PySide.QtGui.QSplitterHandle
       "mayaLayoutInternalWidget" PySide.QtGui.QWidget
         "mayaLayoutInternalWidget" PySide.QtGui.QSplitter
         "mayaLayoutInternalWidget" PySide.QtGui.QSplitter

"""