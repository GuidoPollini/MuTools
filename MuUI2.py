import maya.cmds       as MC
import maya.OpenMayaUI as OMUI

import PySide.QtGui    as QG
import PySide.QtCore   as QC
import shiboken

import functools
import os
import time

# To per-object override a method:
#  def _override(self, ...): ...
#  myObj.methodToOverride = types.MethodType(_override, myObj) 
import types    





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




class VBoxLayout(QG.QVBoxLayout):
    """
    Reset spacing and content margins, nothing more:)
    """
    def __init__(self, *args, **kwargs):
        super(VBoxLayout, self).__init__(*args, **kwargs)
        self.setSpacing(0)
        self.setContentsMargins(0, 0, 0, 0)




class HBoxLayout(QG.QHBoxLayout):
    """
    Reset spacing and content margins, nothing more:)
    """
    def __init__(self, *args, **kwargs):
        super(HBoxLayout, self).__init__(*args, **kwargs)
        self.setSpacing(0)
        self.setContentsMargins(0, 0, 0, 0)

        


class ToolButton(QG.QToolButton):
    def __init__(self, iconPath=None, 
                       size=20,
                       clicked_slot=None,
                       parentObject=None):
        super(ToolButton, self).__init__()
        self.setStyleSheet("""
            border-radius: 0px;         
            padding: 0px;
            margin: 0px;
        """)
        
        self.setFixedSize(size, size)
        self.setCursor(QC.Qt.PointingHandCursor)

        if clicked_slot:
            self.clicked.connect(clicked_slot)

        if iconPath:
            # Store the neutral/hover/clicked images and a "message" to .paintEvent
            self.imageNeutral = QG.QImage(iconPath).scaled(size, size, QC.Qt.IgnoreAspectRatio, QC.Qt.SmoothTransformation)
            self.imageHover = QG.QImage(iconPath).scaled(size * 1.2, size * 1.2, QC.Qt.IgnoreAspectRatio, QC.Qt.SmoothTransformation)
            self.image = self.imageNeutral # Info used by .paintEvent to choose the brightness of the icon
            self.isHover = False

            # PROVA A  USARE QPAINTER fuori dal paintEvent per manipolare un image e 
            # schiarirla con i compositionMode, poi salvala...

        if parentObject:
            parentObject.addWidget(self)
    

    def enterEvent(self, event):
        """
        When the mouse enter the widget, this is called; we save the relevant info 
        (the icon must be higlighted) and we force the redraw (i.e. we call 
        indirectly .paintEvent, which can read the extra info needed!)
        """
        self.isHover = True
        self.image = self.imageHover # Save the info needed to .paintEvent to draw properly
        self.update()                # <== force a call to .paintEvent
        event.accept()               # No idea :(


    def leaveEvent(self, event):
        self.isHover = False        
        self.image = self.imageNeutral
        self.update()
        event.accept()

    def paintEvent(self, event):
        # NO, il paintEvent NON e' ovviamente triggerato quando ci passi sopra... just fuck you!!!
        #print self.underMouse()
        #print self.isDown()

        painter = QG.QPainter()
        painter.begin(self)
        painter.drawImage(0, 0, self.imageNeutral)   
        if self.isHover:
            painter.setCompositionMode(QG.QPainter.CompositionMode_Plus)   
            painter.drawImage(0, 0, self.imageNeutral)             
        painter.end()




class PushButton(QG.QPushButton):
    def __init__(self, text='',
                       fontSize=20,
                       fontWeight='normal',
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
        
        #background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(98, 98, 98),  stop:1.0 rgb(94, 94, 94));
        styleSheet = """
            QPushButton{{
                margin: 0px;
                padding: 0px;
                font-size: {fontSize}px; 
                font-weight: {fontWeight};
                border-radius: {borderRadius}px; 
                background: {baseColor};
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
        """.format(fontSize=fontSize, fontWeight=fontWeight, borderRadius=4, baseColor=baseColor, hoverColor=hoverColor, pressedColor=pressedColor)     

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

        layout = HBoxLayout(self)

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
        self.setFlat(True) 
        self.setStyleSheet("""
            color:rgb(140,140,140);
            font-size: 12px;
        """)

        layout = VBoxLayout(self)

        self.textEdit = QG.QTextEdit()
        self.textEdit.setAcceptRichText(True)
        self.textEdit.setReadOnly(True)
        self.textEdit.setStyleSheet("""
            background-color: rgb(42, 42, 42);
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




class AssetsModel(object):
    pass




class AssetsView(object):
    pass



class CategoryFrameItem(QG.QFrame):
    def __init__(self, parentFrame=None, label='fuckYou', status='ok', parentObject=None):
        self.status = status
        
        print 'CategoryFrameItem:', label, '->', status

        super(CategoryFrameItem, self).__init__()


        #-----------------------------------
        # To talk with its parent frame
        self.parentFrame = parentFrame
        #-----------------------------------


        self.layout = HBoxLayout(self)

        self.setFrameStyle(QG.QFrame.NoFrame)
        self.setFixedHeight(22)

        
        # Choose color depending on status
        """
        if status == 'ok':
            backgroundColor = ''
        elif status == 'bad':
            backgroundColor = 'background-color:rgb(64, 48, 42);'
        elif status == 'fatal': 
            backgroundColor = 'background-color:rgb(255, 66, 47);'
        """
        backgroundColor = ''

        self.setStyleSheet(""" 
            QFrame{      
                padding: 0px 4px 0px 4px;
                """ + backgroundColor + """
            }
            QFrame:hover{
                background-color:rgb(81, 106, 126);   
            }    
        """)
        

        # SELECT CHECKBOX
        #----------------------
        if status == 'ok':
            self.selectCheckBox = QG.QCheckBox()
            self.selectCheckBox.setChecked(False)
            self.selectCheckBox.setCursor(QC.Qt.PointingHandCursor)
            self.selectCheckBox.setStyleSheet("""
                QCheckBox{
                    padding: 0px;
                    margin: 0px;
                    background-color:rgb(54, 54, 54);   
                    border-radius: 0px;
                }
                QCheckBox::indicator:checked{
                }
                QCheckBox:disabled{
                    background-color:rgb(40, 40, 40); 
                }             
            """)
            self.selectCheckBox.setFixedSize(12, 12)

            self.layout.addWidget(self.selectCheckBox)

        else:
            # BETTER: create a widget placeHodler and create or not the checkBox inside it!
            self.placeHolder = QG.QWidget()
            self.placeHolder.setFixedSize(12, 12)
            self.layout.addWidget(self.placeHolder)




        # LABEL
        #----------------------

        # Choose color depending on status
        if status == 'ok':
            color = 'color:rgb(210, 210, 210);'
        elif status == 'bad':
            color = 'color:rgb(250, 230, 180);'
        elif status == 'fatal': 
            color = 'color:red;'



        self.label = QG.QLabel(label)
        self.label.setStyleSheet("""
            QLabel{  
                padding: 4px 0px 0px 8px;
                margin: 0px 0px 0px 0px;
                """ + color + """
                font-size:12px;
            }    
        """)
        self.label.setAlignment(QC.Qt.AlignLeft)
        self.label.setCursor(QC.Qt.PointingHandCursor)

        self.layout.addWidget(self.label)

        if status == 'bad':
            self.fixButton = PushButton(text='FIX',
                fontSize=10,
                fontWeight='bold',
                baseColor=Color(117, 117, 117),
                fixedWidth=36,
                fixedHeight=15,
                clicked_slot=None, 
                parentObject=self.layout)

        # PARENTING
        #----------------------
        if parentObject:
            parentObject.addWidget(self)

    def select(self, state=True):
        if self.status == 'ok':     
            self.selectCheckBox.setChecked(state)
            print self.parentFrame.title




class CategoryFrame(QG.QFrame):
    def __init__(self, title='', parentObject=None):
        #------------------------------------------
        # Invece di infognarti nella table et delegates, stavolta
        # fai tutto manualmente...
        self.title = title
        


        """
        In questo caso forse non conta molto, ma se vuoi emettere un segnale
        ogni volta che la lista cambia dimensione (o semplicemente cambia),
        non puoi accedere direttamente a essa:
        - incapsulare i modifiers (append, delete, rebind, clear) in methods
        - ogni method che altera sensibilmente l'oggetto, emettera' il SIGNAL

        Altrimenti servirebbe un eventLoop che controlla periodicamente le modifiche
        !!! se non e' incapsulato e qualcuno accede ai dati privati senza
        passare per i setter, NESSUN SEGNALE SARA EMESSO

        SE QUALCUNO CAMBIA DI NASCOSTO IL VALORE, e' illegale 
        ... da qui la ragione di incapsulare in oggetti con parti "private"
        """
        
        # THIS ONE MUST BE PRIVATE... otherwise you can't emit SIGNALS and synchronize
        self._items = []
        
        #------------------------------------------


        super(CategoryFrame, self).__init__()
        self.setFrameStyle(QG.QFrame.StyledPanel | QG.QFrame.Plain)
        self.setStyleSheet("""
            QFrame{
                padding: 0px;
                margin: 0px;
                background-color: rgb(42, 42, 42);
            }
            QFrame:disabled{
                background-color: rgb(70, 70, 70);
            }
        """)

        # Don't set the minimumSize for the QFrame, otherwise what follows wont work:
        self.setSizePolicy(QG.QSizePolicy.Preferred, QG.QSizePolicy.Fixed)
        #

        self.mainLayout = VBoxLayout(self)

        

        #-----------------------------------------------------------------------------------------------------
        # HEADER
        #-----------------------------------------------------------------------------------------------------

        # HOLDER
        #----------------------
        header = QG.QFrame()
        header.setFrameStyle(QG.QFrame.NoFrame)
        header.setFixedHeight(24)
        header.setStyleSheet("""
            QFrame{
                background-color:rgb(60, 60, 60); 
                font-size:18px;
                padding: 0px 3px 0px 3px;
                border-radius: 0px;
            }
            QFrame:disabled{
                background-color:rgb(80, 80, 80); 
                color:rgb(40, 40, 40);
            }               
        """)
        header_layout = HBoxLayout(header)
        
        # SELECTALL CHECKBOX
        #----------------------
        self.selectAllCheckBox = QG.QCheckBox()
        self.selectAllCheckBox.setChecked(False)
        self.selectAllCheckBox.setCursor(QC.Qt.PointingHandCursor)
        self.selectAllCheckBox.setStyleSheet("""
            QCheckBox{
                padding: 0px;
                margin: 0px;
                background-color:rgb(48, 48, 48);   
                border-radius: 0px;
            }
            QCheckBox::indicator{
                width: 16px;
                height: 16px;
            }
            QCheckBox:disabled{
                background-color:rgb(40, 40, 40); 
            }             
        """)
        self.selectAllCheckBox.setFixedSize(16, 16)

        
        def _selectAllCheckBox_stateChanged_slot(state):
            # Again, it's a 'closure'
            print self.title, state
            if state == 0:
                self._deselectAllItems()
            if state == 2:
                self._selectAllItems()

        self.selectAllCheckBox.stateChanged.connect(_selectAllCheckBox_stateChanged_slot)
        

        header_layout.addWidget(self.selectAllCheckBox)



        # LABEL
        #----------------------
        header_label = QG.QLabel(title)
        header_label.setStyleSheet("""
            QLabel{  
                color:rgb(220, 220, 220);
                font-size:16px;
                padding: 0px 0px 0px 0px;
                margin: 0px 0px 0px 0px;
            }
            QLabel:hover{
                color: rgb(255, 255, 255);
            }
            QLabel:disabled{
                background-color:rgb(80, 80, 80); 
                color:rgb(40, 40, 40);
            }            
        """)
        header_label.setAlignment(QC.Qt.AlignLeft)
        header_label.setCursor(QC.Qt.PointingHandCursor)
        header_layout.addWidget(header_label)

        # Override the .mousePressEvent
        def _mousePressEvent(innerSelf, event):
            # Note: this is a closure (we need the 'outerSelf', not the 'innerSelf')
            self.selectAllCheckBox.toggle()
        header_label.mousePressEvent = types.MethodType(_mousePressEvent, header_label)


        
        # Add a spacer...
        header_layout.addStretch()



        PushButton(text='FIX ALL',
                       fontSize=12,
                       fontWeight='bold',
                       baseColor=Color(117, 117, 117),
                       fixedWidth=58,
                       fixedHeight=18,
                       clicked_slot=None, 
                       parentObject=header_layout)





        # PARENTING
        #----------------------
        self.mainLayout.addWidget(header)


        #mainLayout.addStretch()

        if parentObject:
            parentObject.addWidget(self)
        

        #-------------------------------------
        # Model
        #-------------------------------------
        self._modelDict = None



    """"""""""""""""""""""""""""""""""""""""""""""""""""""
    # QUESTI E' POTENZIALMENTE PERICOLOSO: modifica la lista
    # E se non emette un segnale opportuno sei fottuto

    def populate(self, itemList): 
        # Clear everything and redraw

        # Order = ok | bad | fatal
        orderedItems =      sorted([x for x in itemList if itemList[x] == 'ok'])
        orderedItems.extend(sorted([x for x in itemList if itemList[x] == 'bad']))
        orderedItems.extend(sorted([x for x in itemList if itemList[x] == 'fatal']))

        for item in orderedItems:
            self._items.append(CategoryFrameItem(parentFrame=self, label=item, status=itemList[item], parentObject=self.mainLayout))
    """"""""""""""""""""""""""""""""""""""""""""""""""""""


    def _selectAllItems(self):
        for item in self._items:
            item.select(True)
    def _deselectAllItems(self):
        for item in self._items:
            item.select(False)
   
    def __getitem__(self, index):
        # To allow something like:
        #   chFrame['pippoPippo'].isChecked()
        #   chFrame[4].setChecked()
        #   chFrame[4].disableFixButton()
        #   ... 
        pass


    def setModel(self, newModelDict):
        """
        There are equivalent:
          catFr.setModel(None)
          catFr.setModel({})
        """
          
        if newModelDict is None or len(newModelDict) == 0:
            self._modelDict = None
        else:    
            for item in newModelDict:
                print item




def callOne(*args, **kwargs):
    print 'callOne ', args, kwargs




def callTwo(*args, **kwargs):
    print 'callTwo ', args, kwargs




def callThree(*args, **kwargs):
    print 'callThree ', args, kwargs
    



class TitleBar(QG.QFrame):
    def __init__(self, title='...', parentObject=None):
        super(TitleBar, self).__init__()
        self = QG.QFrame()
        self.setFrameStyle(QG.QFrame.NoFrame)

        self.setFixedHeight(24)
        self.setStyleSheet("""
            background-color:rgb(115, 192, 255); 
            font-size:18px;
            padding: 0px 0px 0px 0px;
            border-radius: 2px;         
        """)
        self.layout = HBoxLayout(self)
        

        # LABEL
        #----------------------
        self.label = QG.QLabel(title)
        self.label.setStyleSheet("""
            color:rgb(30,30,30);
            padding: 0px;
            margin: 0px;
        """)
        self.label.setAlignment(QC.Qt.AlignHCenter)
        self.layout.addWidget(self.label)


        # MU ICON
        #----------------------
        self.muIcon =ToolButton(
            iconPath='C:/Users/guido.pollini/Desktop/mu_icon.png', 
            size=12,
            #clicked_slot=callOne,
            parentObject=self.layout
        )


        # OPTIONS ICON
        #----------------------
        self.optionsIcon = ToolButton(
            iconPath='C:/Users/guido.pollini/Desktop/options_icon.png', 
            size=16,
            #clicked_slot=callOne,            
            parentObject=self.layout
        )


        # PARENTING
        #----------------------
        if parentObject:
            parentObject.addWidget(self)




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
        self.setMinimumSize(200, 300)
        self.resize(200, 600)


        #-----------------------------------------------------------------------
        # Generic style
        #-----------------------------------------------------------------------
        self.setStyleSheet('font-size:14px;')


        #-----------------------------------------------------------------------
        # Layout
        #-----------------------------------------------------------------------
        mainLayout = VBoxLayout(self)




        #-----------------------------------------------------------------------------------------------------
        # TITLEBAR
        #-----------------------------------------------------------------------------------------------------
        TitleBar(title='Alembic Export', parentObject=mainLayout)





        #======================================================================
        # Working area
        #======================================================================
        workingArea_widget = QG.QWidget()
        workingArea_layout = VBoxLayout(workingArea_widget)




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
            parentObject=workingArea_layout
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
            parentObject=workingArea_layout
        )
        self.shotSelector.setDisabled(True)





        #-----------------------------------------------------------------------------------------------------
        # TOP BUTTON CONTAINER
        #-----------------------------------------------------------------------------------------------------        
        topButtonContainer = QG.QWidget()
        topButtonContainer_layout = HBoxLayout(topButtonContainer)

        self.exportButton = PushButton(
            text='EXPORT',
            fixedWidth=90,
            fixedHeight=24,
            #clicked_slot=None, 
            parentObject=topButtonContainer_layout
        )
        self.exportButton.setDisabled(True)


        topButtonContainer_layout.addStretch()


        self.fixAllButton = PushButton(
            text='Fix all',
            fixedWidth=74,
            fixedHeight=24,
            #clicked_slot=None, 
            parentObject=topButtonContainer_layout
        )
        self.fixAllButton.setDisabled(True)
        

        self.selectAllButton = PushButton(
            text='Select all',
            fontSize=16,
            fixedWidth=76,
            fixedHeight=24,
            #clicked_slot=None, 
            parentObject=topButtonContainer_layout
        )
        self.selectAllButton.setDisabled(True)


        self.deselectAllButton = PushButton(
            text='Deselect all',
            fontSize=16,
            fixedWidth=88,
            fixedHeight=24,
            #clicked_slot=None, 
            parentObject=topButtonContainer_layout
        )
        self.deselectAllButton.setDisabled(True)


        workingArea_layout.addWidget(topButtonContainer)


        #-----------------------------------------------------------------------------------------------------
        # CENTRAL CONTAINER
        #----------------------------------------------------------------------------------------------------- 
        mainContent_scroller = QG.QScrollArea()
        mainContent_scroller.verticalScrollBar().setStyleSheet("""
            QScrollBar:vertical{
                width: 16;
                margin: 0px 0px 0px 0px;
            }

            QScrollBar:handle:vertical{
                min-height: 10px;
            }

            QScrollBar:add-line:vertical{
                background: none;
                height: 99px;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
                background: cyan;

            }

            QScrollBar::sub-line:vertical {
                background: none;
                height: 45px;
                subcontrol-position: top;
                subcontrol-origin: margin;
            }

            QScrollBar::up-arrow:vertical { 
                image:url('./icons/up_48.png'); 
                height: 10px; 
            }

            QScrollBar::down-arrow:vertical {
                image:url('./icons/down_48.png'); 
                height: 10px; 
            }    
        """)
                          
        mainContent_scroller.setFrameStyle(QG.QFrame.NoFrame)
        mainContent_scroller.setHorizontalScrollBarPolicy(QC.Qt.ScrollBarAlwaysOff)
        mainContent_scroller.setWidgetResizable(True)




        mainContent_widget = QG.QFrame()
        mainContent_widget.setFrameStyle(QG.QFrame.StyledPanel | QG.QFrame.Plain)

        mainContent_widget.setStyleSheet("""
            background-color: rgb(42, 42, 42); 
            margin: 4px 0px 4px 0px;
        """)
        mainContent_layout = QG.QVBoxLayout(mainContent_widget)
        mainContent_layout.setSpacing(12)
        mainContent_layout.setContentsMargins(8, 8, 8, 8)





        #===============================================================================================
        # Category frames (CHPR, CAM, SS, ST, UNKNOWN)
        #===============================================================================================

        categories = ['Characters/props', 'Cameras', 'Subsets', 'Unknown'] # 'Sets',
        self.categoryFrames = {}   
        for category in categories:
            newFrame = CategoryFrame(
                title=category,
                parentObject=mainContent_layout)
            
            if category == 'Characters/props':
                chData = {
                    'ch_yakar': 'ok', 
                    'ch_guido': 'bad', 
                    'ch_nibel': 'bad', 
                    'ch_helly': 'fatal'
                }
                newFrame.populate(chData)

            if category == 'Subsets':
                ssData = {
                    'ss_shit1': 'ok',
                    'ss_fuck3': 'ok', 
                    'ss_infecte': 'ok',
                    'ss_bordello': 'bad',
                    'ss_woaaah': 'fatal', 
                    'ss_666': 'ok', 
                    'ss_guidoPollini': 'bad'
                }
                newFrame.populate(ssData)

            if category == 'Cameras':
                camData = {
                    'cam_proj': 'ok', 
                    'cam_hd': 'ok', 
                    'cam_extra': 'ok'
                }
                newFrame.populate(camData)

            if category == 'Unknown':
                unData = {
                    'spazzatura': 'ok', 
                    'immondizia': 'ok', 
                    'pattume': 'ok'
                }
                newFrame.populate(unData)

            self.categoryFrames[category] = newFrame

        #self.categoryFrames['Unknown'].setDisabled(True)
        #self.categoryFrames['Subsets'].setDisabled(True)


        mainContent_layout.addStretch()




        mainContent_scroller.setWidget(mainContent_widget)
        workingArea_layout.addWidget(mainContent_scroller)


        #-----------------------------------------------------------------------------------------------------
        # BOTTOM BUTTON CONTAINER
        #----------------------------------------------------------------------------------------------------- 
        bottomButtonContainer = QG.QWidget()
        bottomButtonContainer_layout = HBoxLayout(bottomButtonContainer)



        pushMeButton = PushButton(
            text='Push me',
            fixedWidth=90,
            fixedHeight=34,
            parentObject=bottomButtonContainer_layout
        )
        pushMeButton.clicked.connect(callOne)
        pushMeButton.clicked.connect(callTwo)
        pushMeButton.clicked.connect(callThree)



        bottomButtonContainer_layout.addStretch()

        PushButton(
            text='x',
            fixedWidth=24,
            fixedHeight=24,
            parentObject=bottomButtonContainer_layout
        )

        PushButton(
            text='?',
            fixedWidth=24,
            fixedHeight=24,
            parentObject=bottomButtonContainer_layout
        )


        workingArea_layout.addWidget(bottomButtonContainer)




        splitter = QG.QSplitter()
        splitter.setOrientation(QC.Qt.Vertical)
        
        splitter.addWidget(workingArea_widget)



        """ DISPLAY ALL AVAILABLE FONTS """
        #sss = QG.QFontComboBox()
        #splitter.addWidget(sss) 

        self.consoleLog = Log(
            parentObject=splitter
        )

        for i in range(40):
            self.consoleLog.normal('Just fuck you... ' + str(i))
            self.consoleLog.success('Just fuck you... ' + str(i))
            self.consoleLog.warning('Just fuck you... ' + str(i))
            self.consoleLog.fatality('Just fuck you... ' + str(i))


        mainLayout.addWidget(splitter)


        # At this point, the splitter's widget children are invisible;
        # thus, splitter.sizes() == [0, 0, 0, ...]
        
        # Show it:)
        self.show()
        

        """ FUCKING ATROCIOUS! Try sizePolicy/sizeHints... everything but this shit! """
        logHeight = 40
        sizes = splitter.sizes()
        totalHeight = sizes[0] + sizes[1]
        newSizes = [totalHeight - logHeight, logHeight]
        splitter.setSizes(newSizes)


        
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
        floating = MC.paneLayout(configuration='single', width=300, height=300)
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