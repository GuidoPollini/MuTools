__version__ = '1.0.2'
print '--> Executing MuUI...', __version__



import MuTools.MuUtils as Utils

import maya.cmds       as MC
import maya.mel        as MM
import maya.OpenMayaUI as OMUI

import PySide.QtCore   as QC
import PySide.QtGui    as QG
import shiboken

from math import clamp # Monkey patched in MuUtils

#------------------------------------------------------------------------------
# Loading module...
Utils.moduleLoadingMessage()
#------------------------------------------------------------------------------















                          











"""
-------------------------------------------------------------------------------
   ____  _                                                   
  / __ \| |                                                  
 | |  | | |_  __      ___ __ __ _ _ __  _ __   ___ _ __ ___  
 | |  | | __| \ \ /\ / / '__/ _` | '_ \| '_ \ / _ \ '__/ __| 
 | |__| | |_   \ V  V /| | | (_| | |_) | |_) |  __/ |  \__ \ 
  \___\_|\__|   \_/\_/ |_|  \__,_| .__/| .__/ \___|_|  |___/ 
                                 | |   | |                   
                                 |_|   |_| 

-------------------------------------------------------------------------------
"""



class Color(QG.QColor):
    """
    I derive from QG.QColor only to parasite the conversions RGB <=> HSL.
    - Components will be clamped to [0, 255], not floored to 0 as in QColor;
    - The alpha component will always be 255;
    """
    

    #-----------------------------
    # INITIALIZER
    #-----------------------------
    def __init__(self, r, g, b):
        # Clamp interval: [0, 255]
        clampedColor = [clamp(x, 0, 255) for x in [r, g, b]]
        super(Color, self).__init__(*clampedColor)
        self.setAlpha(255)
        


    #-----------------------------
    # MAGIC METHODS
    #-----------------------------
    def __add__(self, otherColor):
        # 'otherColor' can be a <Color>, a <3-list> or <3-tuple>
        # ("it quacks/moves/shits like a duck, hence it's a duck")
        result = [self[i] + otherColor[i] for i in [0, 1, 2]]
        return Color(*result)


    def __getitem__(self, colorIndex):
        colorGetters = [self.red, self.green, self.blue]
        return colorGetters[colorIndex]()      


    def __iadd__(self, otherColor):
        self = self + otherColor
        return self


    def __repr__(self):
        """
        Return the string 'rgb(#,#,#)', compatible with Qt styleSheets
        """
        colorString = 'rgb({},{},{})'.format(self[0], self[1], self[2])
        return colorString


    def __setitem__(self, colorIndex, value):
        colorSetters = [self.setRed, self.setGreen, self.setBlue]
        colorSetters[colorIndex](clamp(value, 0, 255))


    def __str__(self):
        return self.__repr__()  



    #-----------------------------
    # METHODS
    #----------------------------- 
    def addToValue(self, addend):
        hsva = list(self.getHsv()) #hsva
        hsva[2] = clamp(hsva[2] + addend, 0, 255)
        self.setHsv(*hsva)

    def lighten(self, factor):
        pass


    def darken(self, factor):    
        pass




class VerticalLayout(QG.QVBoxLayout):
    """
    Reset spacing and content margins
    """
    def __init__(self, *args, **kwargs):
        super(VerticalLayout, self).__init__(*args, **kwargs)
        self.setSpacing(0)
        self.setContentsMargins(0, 0, 0, 0)




class HorizontalLayout(QG.QHBoxLayout):
    """
    Reset spacing and content margins
    """
    def __init__(self, *args, **kwargs):
        super(HorizontalLayout, self).__init__(*args, **kwargs)
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
            self.isHover = False

            # PROVA A  USARE QPAINTER fuori dal paintEvent per manipolare un image e 
            # schiarirla con i compositionMode, poi salvala...

        if parentObject:
            parentObject.addWidget(self)
    

    def enterEvent(self, event):
        self.isHover = True
        self.update()                # <== force a call to .paintEvent
        event.accept()               # No idea :(


    def leaveEvent(self, event):
        self.isHover = False        
        self.update()
        event.accept()

    def paintEvent(self, event):
        painter = QG.QPainter()
        painter.begin(self)
        if self.isHover:
            #painter.setCompositionMode(QG.QPainter.CompositionMode_Plus)   
            painter.drawImage(-1, -1, self.imageHover)
        else:
            painter.drawImage(0, 0, self.imageNeutral)
      
        painter.end()




class TitleBar(QG.QFrame):
    def __init__(self, title='...', parentObject=None):
        # NOTE: at this point, self has already the structure of a QG.QFrame...
        super(TitleBar, self).__init__(parentObject)
        
        self.setFrameStyle(QG.QFrame.NoFrame)
        self.setFixedHeight(24)
        self.setStyleSheet("""
            background-color:rgb(115, 192, 255); 
            font-size:18px;
            padding: 0px 6px 0px 4px;
            border-radius: 2px;         
        """)
        self.layout = HorizontalLayout(self)
        
        # MU ICON
        #----------------------
        self.muIcon =ToolButton(
            iconPath='C:/Users/guido.pollini/Desktop/mu_icon.png', 
            size=12,
            clicked_slot=self._muIconClicked,
            parentObject=self.layout
        )

        """
        # OPTIONS ICON
        #----------------------
        self.optionsIcon = ToolButton(
            iconPath='C:/Users/guido.pollini/Desktop/options_icon.png', 
            size=16,
            clicked_slot=self._optionsIconClicked,            
            parentObject=self.layout
        )
        """

        # LABEL
        #----------------------
        self.label = QG.QLabel(title)
        self.label.setFixedHeight(24)
        self.label.setStyleSheet("""
            color:rgb(30,30,30);
            padding: 0px;
            margin: 0px;
        """)
        self.label.setAlignment(QC.Qt.AlignHCenter)
        self.layout.addWidget(self.label)
        
        """
        # DOCK ICON
        #----------------------
        self.dockIcon = ToolButton(
            iconPath='C:/Users/guido.pollini/Desktop/dockIcon.png', 
            size=16,
            clicked_slot=self._dockIconClicked,            
            parentObject=self.layout
        )
        """

        # CLOSE ICON
        #----------------------
        self.closeIcon = ToolButton(
            iconPath='C:/Users/guido.pollini/Desktop/closeIcon.png', 
            size=16,
            clicked_slot=self._closeIconClicked,            
            parentObject=self.layout
        )


        # PARENTING
        #----------------------
        """
        try:
            parentObject.addWidget(self)
        except:
            self.setParent(parentObject)

        
        """
        #self.show()

    def _muIconClicked(self):
        muDict = Utils.inspectMuTools()
        text = ''
        for key in muDict:
            if muDict[key] is not None:
                text += '<b><font color="#22FF22" size="4">' + key + '</font></b>'                
                text += '<ul>'
                for info in muDict[key]:
                    text += '<li>' + info + ': ' + muDict[key][info] + '</li>'
                text += '</ul>'
            else:
                text += '<b><font color="#FF5522">' + key + '</font></b>'                                
            text += '<br><br>'      
        
        if MC.control('_muInfoWindow', query=True, exists=True):
            MC.deleteUI('_muInfoWindow')
        self.muInfoWndow = InfoWindow('_muInfoWindow', text, self.parent())

    def _optionsIconClicked(self):
        print 'OPTIONS'

    def _dockIconClicked(self):
        print 'DOCK'

    def _closeIconClicked(self):
        # A bare Maya deleteUI...
        """ --> Is it enough??? <-- """

        # The TitleBar should be a direct child of the QDockWidget
        MC.deleteUI(self.parent().objectName())




class InfoWindow(QG.QMainWindow):
    def __init__(self, windowName, text='...', parentObject=None):
        #if MC.control(windowName, query=True, exists=True):
        #    MC.deleteUI(windowName)
        
        super(InfoWindow, self).__init__(MayaWindow.instance() if parentObject is None else parentObject)
        self.setObjectName(windowName)
        self.setWindowTitle(windowName)
        self.centralWidget = QG.QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = VerticalLayout(self.centralWidget)

        self.textEdit = QG.QTextEdit()
        self.textEdit.setAcceptRichText(True)
        self.textEdit.setReadOnly(True)
        self.textEdit.setStyleSheet("""
            background-color: rgb(42, 42, 42);
            color:rgb(200,200,200);
            font-size: 13px;
        """)
        self.textEdit.setText(text)
        self.setFixedSize(500, 600)
        self.layout.addWidget(self.textEdit)
        self.show()
    



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

        layout = HorizontalLayout(self)

        comboBox = QG.QComboBox()
        comboBox.setCursor(QC.Qt.PointingHandCursor) # It's clickable:)  
        if comboBoxFixedWidth:
            comboBox.setFixedWidth(comboBoxFixedWidth)


        label = QG.QLabel(text)
        layout.addWidget(label)
        possibleAligns = {'left':   QC.Qt.AlignLeft,
                          'center': QC.Qt.AlignHCenter,
                          'right':  QC.Qt.AlignRight
        }
        label.setAlignment(QC.Qt.AlignVCenter | possibleAligns[align])
        if labelFixedWidth:
            label.setFixedWidth(labelFixedWidth)
        layout.addWidget(comboBox)
        

        # Attach to the object
        self._layout   = layout
        self._label    = label
        self._comboBox = comboBox
        self.setItemList(itemList)


        # Selection changed   
        self.currentIndexChanged_slot = currentIndexChanged_slot
        """ Note the [] (__getitem__) used on the signal to choose the needed C++ overload """                     
        self._comboBox.currentIndexChanged[str].connect(self._currentIndexChanged_slot)

        # Add to a layout
        if parentObject is not None:
            parentObject.addWidget(self)
    
    def _currentIndexChanged_slot(self, message):
        if self.currentIndexChanged_slot is not None:
            self.currentIndexChanged_slot(message)


    def setCurrentIndexChangedCallback(self, callback):
        self.currentIndexChanged_slot = callback
    

    def setLabel(self, text):
        self._label.setText(text)
        return self


    def setItemList(self, itemList):
        self._comboBox.clear()
        self._comboBox.addItems(itemList) 
        return self    




class PushButton(QG.QPushButton):
    def __init__(self, text='',
                       fontSize=20,
                       borderRadius=6,
                       fontWeight='normal',
                       baseColor=Color(98, 98, 98),
                       fixedWidth=None,
                       fixedHeight=None,
                       clicked_slot=None, 
                       parentObject=None):

        super(PushButton, self).__init__()
        self.setText(text)
        self.setCursor(QC.Qt.PointingHandCursor)
        
        baseGradient = """
            qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 {color0}, stop:0.5 {color1}, stop:1.0 {color2});
        """.format(color0=baseColor + (10, 10, 10), color1=baseColor, color2=baseColor + [-10, -10, -10])

        hoverGradient = """
            qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 {color0}, stop:0.2 {color1}, stop:1.0 {color2});
        """.format(color0=baseColor + (20, 30, 80), color1=baseColor + (20, 20, 20), color2=baseColor)
       
        pressedGradient = """
            qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 {color0}, stop:0.2 {color1}, stop:1.0 {color2});
        """.format(color0=baseColor + (30, 50, 120), color1=baseColor + (40, 40, 40), color2=baseColor + (10, 10, 10))

        styleSheet = """
            QPushButton{{
                margin: 0px;
                padding: 0px;
                font-size: {fontSize}px; 
                font-weight: {fontWeight};
                border-radius: {borderRadius}px; 
                background: {baseGradient};
                border-style: outset;
                border-width: 1px;
                border-color: rgb(35, 35, 35);
            }}
            
            QPushButton:hover{{
                background: {hoverGradient}
            }}      
            
            QPushButton:pressed{{
                background: {pressedGradient}
                padding: 0px;
            }}
        """.format(baseGradient=baseGradient, hoverGradient=hoverGradient, pressedGradient=pressedGradient, fontSize=fontSize, fontWeight=fontWeight, borderRadius=borderRadius)     

        self.setStyleSheet(styleSheet)

        if fixedWidth:
            self.setFixedWidth(fixedWidth)

        if fixedHeight:
            self.setFixedHeight(fixedHeight)

        if clicked_slot:
            self.clicked.connect(clicked_slot)

        if parentObject:
            parentObject.addWidget(self)



"""
----------------------------------------------------------------------------
  __  __ _      _            
 |  \/  (_)    (_)           
 | \  / |___  ___ _ __  ___  
 | |\/| | \ \/ / | '_ \/ __| 
 | |  | | |>  <| | | | \__ \ 
 |_|  |_|_/_/\_\_|_| |_|___/ 

----------------------------------------------------------------------------                            
"""  



class MayaQWidgetBaseMixin(object):
    '''
        Inheritance ordering: This class must be placed *BEFORE* the Qt class for proper execution
        This is needed to workaround a bug where PyQt/PySide does not call super() in its own __init__ functions
    Example:
        class MyQWidget(MayaQWidgetBaseMixin, QPushButton):
            def __init__(self, parent=None):
                super(MyQWidget, self).__init__(parent=parent)
                self.setText('Push Me')
        myWidget = MyQWidget()
        myWidget.show()
        print myWidget.objectName()
    '''
    def __init__(self, parent=None, *args, **kwargs):
        print '-->', args, kwargs
        super(MayaQWidgetBaseMixin, self).__init__(parent=parent, *args, **kwargs) 
        # Init all baseclasses (including QWidget) of the main class
        self._initForMaya(parent=parent)


    def _initForMaya(self, parent=None, *args, **kwargs):
        # Set parent to Maya main window if parent=None
        if parent == None:
            self._makeMayaStandaloneWindow()


    def _makeMayaStandaloneWindow(self):
        '''Make a standalone window, though parented under Maya's mainWindow.
        The parenting under Maya's mainWindow is done so that the QWidget will not
        auto-destroy itself when the instance variable goes out of scope.
        '''
        origParent = self.parent()
                
        # Parent under the main Maya window
        self.setParent(MayaWindow.instance())
        
        # Make this widget appear as a standalone window even though it is parented
        if isinstance(self, QG.QDockWidget):
            self.setWindowFlags(QC.Qt.Dialog|QC.Qt.FramelessWindowHint)
        else:
            self.setWindowFlags(QC.Qt.Window)       
        
        # Delete the parent QDockWidget if applicable
        if isinstance(origParent, QG.QDockWidget):
            origParent.close()
            
         


class MayaQDockWidget(MayaQWidgetBaseMixin, QG.QDockWidget):
    '''QDockWidget tailored for use with Maya.
    Mimics the behavior performed by Maya's internal QMayaDockWidget class and the dockControl command

    :Signals:
        closeEventTriggered: emitted when a closeEvent occurs
    
    :Known Issues:
        * Manually dragging the DockWidget to dock in the Main MayaWindow will have it resize to the 'sizeHint' size
          of the child widget() instead of preserving its existing size.
    '''
    # Custom Signals
    closeEventTriggered = QC.Signal()   # Qt Signal triggered when closeEvent occurs


    def __init__(self, parent=None, *args, **kwargs):
        super(MayaQDockWidget, self).__init__(parent=parent, *args, **kwargs) # Init all baseclasses (including QWidget) of the main class

        # == Mimic operations performed by Maya internal QmayaDockWidget ==
        self.setAttribute(QC.Qt.WA_MacAlwaysShowToolWindow)
        
        # WORKAROUND: The mainWindow.handleDockWidgetVisChange may not be present on some PyQt and PySide systems.
        #             Handle case if it fails to connect to the attr.
        try:
            self.visibilityChanged.connect(MayaWindow.instance().handleDockWidgetVisChange)
        except AttributeError, e: 
            # Error connecting visibilityChanged trigger to mainWindow.handleDockWidgetVisChange. 
            # Falling back to using MEL command directly.
            MM.eval('evalDeferred("updateEditorToggleCheckboxes()")')  # Currently mainWindow.handleDockWidgetVisChange only makes this updateEditorToggleCheckboxes call


    def setArea(self, area):
        # Skip setting the area if no area value passed in
        if area == QC.Qt.NoDockWidgetArea:
            return

        # Mimic operations performed by Maya dockControl command
        mainWindow = MayaWindow.instance()
        childrenList = mainWindow.children()
        foundDockWidgetToTab = False
        for child in childrenList:
            # Create Tabbed dock if a QDockWidget already at that area
            if (child != self) and (isinstance(child, QG.QDockWidget)):
                if  not child.isHidden() and  not child.isFloating():
                    if mainWindow.dockWidgetArea(child) == area:
                        mainWindow.tabifyDockWidget(child, self)
                        self.raise_()
                        foundDockWidgetToTab = True
                        break
        # If no other QDockWidget at that area, then just add it
        if not foundDockWidgetToTab:
            mainWindow.addDockWidget(area, self)
    
    
    def resizeEvent(self, evt):
        '''Store off the 'savedSize' property used by Maya's QMainWindow to set the
        size of the widget when it is being docked.
        '''
        self.setProperty('savedSize', self.size()) 
        return super(MayaQDockWidget, self).resizeEvent(evt)


    def closeEvent(self, evt):
        '''Hide the QDockWidget and trigger the closeEventTriggered signal
        '''
        # Handle the standard closeEvent()
        super(MayaQDockWidget, self).closeEvent(evt)

        if evt.isAccepted():
            # Force visibility to False
            self.setVisible(False) # since this does not seem to have happened already

            # Emit that a close event is occurring
            self.closeEventTriggered.emit()




class MayaDockableMixin(MayaQWidgetBaseMixin):
    '''
    Handle Maya dockable actions controlled with the show() function.
    
    Integration Notes:
        Inheritance ordering: This class must be placed *BEFORE* the Qt class for proper execution
        This is needed to workaround a bug where PyQt/PySide does not call super() in its own __init__ functions
    
    Example:
        class MyQWidget(MayaQWidgetDockableMixin, QPushButton):
            def __init__(self, parent=None):
                super(MyQWidget, self).__init__(parent=parent)
                self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred )
                self.setText('Push Me')
        myWidget = MyQWidget()
        myWidget.show(dockable=True)
        myWidget.show(dockable=False)
        print myWidget.showRepr()
    '''
    def setDockableParameters(self, dockName=None, title='TEST', dockable=None, floating=None, area=None, allowedArea=None, width=None, height=None, x=None, y=None, *args, **kwargs):
        '''
        Set the dockable parameters.
        
        :Parameters:
            dockable (bool)
                Specify if the window is dockable (default=False)
            floating (bool)
                Should the window be floating or docked (default=True)
            area (string)
                Default area to dock into (default='left')
                Options: 'top', 'left', 'right', 'bottom'
            allowedArea (string)
                Allowed dock areas (default='all')
                Options: 'top', 'left', 'right', 'bottom', 'all'
            width (int)
                Width of the window
            height (int)
                Height of the window
            x (int)
                left edge of the window
            y (int)
                top edge of the window
                
        :See: show(), hide(), and setVisible()
        '''
        if (dockable == True) or (dockable == None and self.isDockable()): # == Handle docked window ==
            # Conversion parameters (used below)
            dockAreaStrMap = {
                'left'   : QC.Qt.LeftDockWidgetArea,
                'right'  : QC.Qt.RightDockWidgetArea,
                'top'    : QC.Qt.TopDockWidgetArea,    
                'bottom' : QC.Qt.BottomDockWidgetArea,
                'all'    : QC.Qt.AllDockWidgetAreas,  
                'none'   : QC.Qt.NoDockWidgetArea,   # Note: Not currently supported in maya dockControl command
            }

            # Create dockControl (QDockWidget) if needed
            if dockable == True and not self.isDockable():
                # Retrieve original position and size
                # Position
                if x == None:
                    x = self.x()
                if y == None:
                    y = self.y()
                # Size
                unininitializedSize = QC.QSize(640,480)  # Hardcode: (640,480) is the default size for a QWidget
                if self.size() == unininitializedSize:
                    # Get size from widget sizeHint if size not yet initialized (before the first show())
                    widgetSizeHint = self.sizeHint()
                else:
                    widgetSizeHint = self.size() # use the current size of the widget
                if width == None:
                    width = widgetSizeHint.width()
                if height == None:
                    height = widgetSizeHint.height()
                

                """ 
                HERE'S THE FUCKING MAGIC:
                it creates a QDockWidget and put self inside him;
                nothing more, nothing less...
                """
                # Create the QDockWidget
                dockWidget = MayaQDockWidget()

                # IF YOU TOUCH THE 'BORDER' HERE, you'll destroy
                # all the button presets...
                # remember, it's CSS-like
                dockWidget.setStyleSheet("""
                    padding: 2px;
                    margin: 0px;
                """)


                #background:qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(54, 91, 120), stop:.15 rgb(68,68,68));              

                """ --> THIS IS MAGIC: it replaces the OS window bar and still 
                        detects the dragging... woaaaaaaaaah"""   
                #titleBar = QG.QLabel('NOOOOOOOOPE') #TitleBar('ALEMBICCCC', dockWidget)
                
                self.titleBar = TitleBar(title, self)                
                dockWidget.setTitleBarWidget(self.titleBar)


                dockWidget.setWindowTitle(dockName.split('_')[0])
                dockWidget.setWidget(self)

                dockWidget.setObjectName(dockName)


                # By default, when making dockable, make it floating
                #   This addresses an issue on Windows with the window decorators
                #   not showing up.  Setting this here will cause setFloating() to be called below.
                if floating == None:
                    floating = True

                # Hook up signals
                dockWidget.topLevelChanged.connect(self.floatingChanged)
                dockWidget.closeEventTriggered.connect(self.dockCloseEventTriggered)
            else:
                if floating == True:
                    # Retrieve original position (if floating)
                    pos = self.parent().mapToGlobal(QC.QPoint(0,0))
                    if x == None:
                        x = pos.x()
                    if y == None:
                        y = pos.y()

                # Retrieve original size
                if width == None:
                    width = self.width()
                if height == None:
                    height = self.height()

            # Get dock widget identifier
            dockWidget = self.parent()
            
            # Update dock values
            if area        != None:
                areaValue = dockAreaStrMap.get(area, QC.Qt.LeftDockWidgetArea)
                dockWidget.setArea(areaValue)
            if allowedArea != None:
                areaValue = dockAreaStrMap.get(allowedArea, QC.Qt.AllDockWidgetAreas)
                dockWidget.setAllowedArea(areaValue)
            if floating    != None:
                dockWidget.setFloating(floating)
                
            # Position window
            if dockWidget.isFloating() and ((x != None) or (y != None)):
                dockPos = dockWidget.mapToGlobal(QC.QPoint(0,0))
                if x == None:
                    x = dockPos.x()
                if y == None:
                    y = dockPos.y()
                dockWidget.move(x,y)

            if (width != None) or (height != None):
                if width == None:
                    width = self.width()
                if height == None:
                    height = self.height()
                # Perform first resize on dock, determine delta with widget, and resize with that adjustment
                # Result: Keeps the content widget at the same size whether under the QDockWidget or a standalone window
                dockWidget.resize(width, height) # Size once to know the difference in the dockWidget to the targetSize
                dockWidgetSize = dockWidget.size() + QC.QSize(width,height)-self.size() # find the delta and add it to the current dock size
                # Perform the final resize (call MayaQDockWidget.resize() which also sets the 'savedSize' property used for sizing when docking to the Maya MainWindow)
                dockWidget.resize(dockWidgetSize)
                
        else:  # == Handle Standalone Window ==
            # Make standalone as needed
            if dockable == False and self.isDockable():
                # Retrieve original position and size
                dockPos = self.parent().mapToGlobal( QPoint(0,0) )
                if x == None:
                    x = dockPos.x()
                if y == None:
                    y = dockPos.y()
                if width == None:
                    width = self.width()
                if height == None:
                    height = self.height()
                # Turn into a standalone window and reposition
                currentVisibility = self.isVisible()
                self._makeMayaStandaloneWindow() # Set the parent back to Maya and remove the parent dock widget
                self.setVisible(currentVisibility)
                
            # Handle position and sizing
            if (width != None) or (height != None):
                if width == None:
                    width = self.width()
                if height == None:
                    height = self.height()
                self.resize(width, height)
            if (x != None) or (y != None):
                if x == None:
                    x = self.x()
                if y == None:
                    y = self.y()
                self.move(x,y)


    def show(self, *args, **kwargs):
        '''
        Show the QWidget window.  Overrides standard QWidget.show()
        
        :See: setDockableParameters() for a list of parameters
        '''
        # Update the dockable parameters first (if supplied)
        if len(args) or len(kwargs):
            self.setDockableParameters(*args, **kwargs)
        
        # Handle the standard setVisible() operation of show()
        QG.QWidget.setVisible(self, True) # NOTE: Explicitly calling QWidget.setVisible() as using super() breaks in PySide: super(self.__class__, self).show()
        # INFINITE RECURSION... but somethign is bad in this mixin... SIMPLIFY IT!!!
        # super(MayaDockableMixin, self).show()
        
        # Handle special case if the parent is a QDockWidget (dockControl)
        parent = self.parent()
        if isinstance(parent, QG.QDockWidget):
            parent.show()


    def hide(self, *args, **kwargs):
        '''Hides the widget.  Will hide the parent widget if it is a QDockWidget.
        Overrides standard QWidget.hide()
        '''
        # Update the dockable parameters first (if supplied)
        if len(args) or len(kwargs):
            self.setDockableParameters(*args, **kwargs)
        
        # Handle special case if the parent is a QDockWidget (dockControl)
        parent = self.parent()
        if isinstance(parent, QG.QDockWidget):
            parent.hide()

        QG.QWidget.setVisible(self, False) # NOTE: Explicitly calling QWidget.setVisible() as using super() breaks in PySide: super(self.__class__, self).show()


    def setVisible(self, makeVisible, *args, **kwargs):
        '''
        Show/hide the QWidget window.  Overrides standard QWidget.setVisible() to pass along additional arguments
        
        :See: show() and hide()
        '''
        if (makeVisible == True):
            return self.show(*args, **kwargs)
        else:
            return self.hide(*args, **kwargs)


    def raise_(self):
        '''Raises the widget to the top.  Will raise the parent widget if it is a QDockWidget.
        Overrides standard QWidget.raise_()
        '''
        # Handle special case if the parent is a QDockWidget (dockControl)
        parent = self.parent()
        if isinstance(parent, QG.QDockWidget):
            parent.raise_()
        else:
            QG.QWidget.raise_(self)  # NOTE: Explicitly using QWidget as using super() breaks in PySide: super(self.__class__, self).show()


    def isDockable(self):
        '''Return if the widget is currently dockable (under a QDockWidget)
        
        :Return: bool
        '''
        parent = self.parent()
        return isinstance(parent, QG.QDockWidget)


    def isFloating(self):
        '''Return if the widget is currently floating (under a QDockWidget)
        Will return True if is a standalone window OR is a floating dockable window.
        
        :Return: bool
        '''
        parent = self.parent()
        if not isinstance(parent, QG.QDockWidget):
            return True
        else:
            return parent.isFloating()


    def floatingChanged(self, isFloating):
        '''Triggered when QDockWidget.topLevelChanged() signal is triggered.
        Stub function.  Override to perform actions when this happens.
        '''
        pass


    def dockCloseEventTriggered(self):
        '''Triggered when QDockWidget.closeEventTriggered() signal is triggered.
        Stub function.  Override to perform actions when this happens.
        '''
        pass


    def dockArea(self):
        '''Return area if the widget is currently docked to the Maya MainWindow
        Will return None if not dockable
        
        :Return: str
        '''
        dockControlQt = self.parent()

        if not isinstance(dockControlQt, QDockWidget):
            return None
        else:
            mainWindow = MayaWindow.instance()

            dockAreaMap = {    
                QC.Qt.LeftDockWidgetArea   : 'left',
                QC.Qt.RightDockWidgetArea  : 'right',
                QC.Qt.TopDockWidgetArea    : 'top',
                QC.Qt.BottomDockWidgetArea : 'bottom',
                QC.Qt.AllDockWidgetAreas   : 'all',
                QC.Qt.NoDockWidgetArea     : 'none',   # Note: 'none' not supported in maya dockControl command
            }    
            dockWidgetAreaBitmap = mainWindow.dockWidgetArea(dockControlQt)
            return dockAreaMap[dockWidgetAreaBitmap]


    def setWindowTitle(self, val):
        '''Sets the QWidget's title and also it's parent QDockWidget's title if dockable.

        :Return: None
        '''
        # Handle the standard setVisible() operation of show()
        QG.QWidget.setWindowTitle(self, val) # NOTE: Explicitly calling QWidget.setWindowTitle() as using super() breaks in PySide: super(self.__class__, self).show()
        
        # Handle special case if the parent is a QDockWidget (dockControl)
        parent = self.parent()
        if isinstance(parent, QG.QDockWidget):
            parent.setWindowTitle(val)








""" 
--> It's TOO COMPLEX AND CONVOLUTED!!!
    I just need a docking Qt window, not a generic QWidget
    AVOID MIXINS if a simpler solution exists!!!

-----------------------------------------------------------------------
DOCKABLE WINDOW: 
  QDockWidget
      ||
      \/
    QWidget

A window to be dockable must be child of another widget of type 'QDockWidget'.
So we'll have 2 widgets:
 - alembicExporter_window_CHILD <class 'MuTools.MuUI.Window'>
 - alembicExporter_window <class 'MuTools.MuUI.MayaQDockWidget'>

To kill the window you need to touch the QDockWidget...

--> To avoid useless complexities, always make a window dockable; then disbale
    the docking areas...

"""    


class Window(MayaDockableMixin, QG.QWidget):
    #-----------------------------
    # INITIALIZER
    #-----------------------------          
    def __init__(self, title, mayaName, isDocked=False, startingPosition=None):
        """ --> mayaName should be internal; i.e. convert 'title' in a valid maya name and add
                _WIN and _DOCK """

        if MC.control(mayaName, query=True, exists=True):
            MC.deleteUI(mayaName)
        
        super(Window, self).__init__(parent=None)
        self.setSizePolicy(QG.QSizePolicy.Preferred, QG.QSizePolicy.Preferred)
        
        self.setObjectName(mayaName + '_CHILD')

        self.setStyleSheet("""
            padding: 0px;
            margin: 0px;
            font-size:14px;
        """)

        #self.layout = HorizontalLayout(self)


        #for i in range(10):
        #    self.layout.addWidget(QG.QLabel('xxx'))
        
        """
        # FAR BETTER
        self.createDockWrapper(title=title, dockName=mayaName, dockableAreas=None)
        self.dock('left')
        self.show()
        """

        self.resize(0, 0)  
        self.show(dockName=mayaName, title=title, dockable=True)
        #self.parent().resize(0, 0)  
    def name(self):
        return self.objectName()

    def dockName(self):
        return self.parent().objectName()    


    def __str__(self):
        return '"{0}"(dock:"{1}")<Window>'.format(self.name(), self.dockName())
    

    def shrink(self):
        # HEIN???
        self.parent().resize(0, 0)  
        self.parent().show()                                    





class MayaWindow(object):
    """
    Just a namespace to manipulate Maya window...
    """
    @staticmethod
    def mainWindow():
        pointer = OMUI.MQtUtil.mainWindow() # It's a QMainWindow, not simply a QWidget!
        return shiboken.wrapInstance(long(pointer), QG.QMainWindow)	    
    
    @staticmethod
    def instance():
        pointer = OMUI.MQtUtil.mainWindow() # It's a QMainWindow, not simply a QWidget!
        return shiboken.wrapInstance(long(pointer), QG.QMainWindow)     
  



def getMayaWindow():
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





















""" MIXINS
-------------------------------------------------------------------------------------
-------------------------------------------------------
>>> ShittyWidget.__init__(), selfId == 425634616
>>> Mixin.__init__(),        selfId == 425634616
>>> Widget.__init__(),       selfId == 425634616

MRO: ShittyWidget --> Mixin --> Widget --> object

! Note that 'self' is the same and super remember the
position in the MRO of (the class of) self; so, 
the super in Mixin doesn't get the super of the class
but the super of the class of self at the required 
level...

--> SUPER allows to move to the next class of the
    passed self... it's not really a superclass...
-------------------------------------------------------

class Mixin(object):
    def __init__(self):
        print '>>> Mixin.__init__(), selfId ==', id(self)
        super(Mixin, self).__init__()
        
class Widget(object):
    def __init__(self):
        print '>>> Widget.__init__(), selfId ==', id(self)  
        
class ShittyWidget(Mixin, Widget):
    def __init__(self):
        print '>>> ShittyWidget.__init__(), selfId ==', id(self)
        super(ShittyWidget, self).__init__()

s = ShittyWidget()
print 'MRO:', ' --> '.join([str(x.__name__) for x in ShittyWidget.mro()])
-------------------------------------------------------------------------------------
"""




""" -------> ---------> ----------------->         """
""" THIS ONE IS NOT IMPORTANT? REMOVE AND SIMPLIFY """
""" -------> ---------> ----------------->         """































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

