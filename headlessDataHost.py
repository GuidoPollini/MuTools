#
#    ngSkinTools
#    Copyright (c) 2009-2015 Viktoras Makauskas. 
#    All rights reserved.
#    
#    Get more information at 
#        http://www.ngskintools.com
#    
#    --------------------------------------------------------------------------
#
#    The coded instructions, statements, computer programs, and/or related
#    material (collectively the "Data") in these files are subject to the terms 
#    and conditions defined by
#    Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License:
#        http://creativecommons.org/licenses/by-nc-nd/3.0/
#        http://creativecommons.org/licenses/by-nc-nd/3.0/legalcode
#        http://creativecommons.org/licenses/by-nc-nd/3.0/legalcode.txt
#         
#    A copy of the license can be found in file 'LICENSE.txt', which is part 
#    of this source code package.
#    

from ngSkinTools.ui.layerDataModel import LayerDataModel
from ngSkinTools.utils import Utils
from maya import cmds
from ngSkinTools.ui.events import MayaEvents, restartEvents, scriptJobs
from ngSkinTools.doclink import SkinToolsDocs
from ngSkinTools.log import LoggerFactory


log = LoggerFactory.getLogger("HeadlessDataHost")


class RefCountedHandle:
    '''
    reference counted handle to a dynamically allocated instance;
    
    creates reference after first addReference() call, and destroys it 
    when last reference is removed via removeReference()
    '''
    
    def __init__(self,instantiator):
        self.instantiator=instantiator
        self.instance = None
        self.references = set()
    
    def getCurrentInstance(self):
        '''
        returns handle to currently created instance
        '''
        return self.instance

    def addReference(self,refSource):
        if refSource in self.references:
            return
        
        if len(self.references)==0:
            self.instance = self.instantiator()
            self.instance.initialize()
            
        self.references.add(refSource)
        
        
    def removeReference(self,refSource):
        '''
        returns false, if provided reference was not found in the stack
        '''
        
        if refSource not in self.references:
            return False
        
        self.references.remove(refSource)
        if len(self.references)==0:
            self.instance.cleanup()
            self.instance=None
            
        return True
            
        
class HeadlessDataHost:

    '''
    A singleton of this object is created when at least one UI window is opened,
    and performs a cleanup once all objects are closed
    '''
    
    HANDLE = None
    
    @staticmethod
    def get():
        return HeadlessDataHost.HANDLE.getCurrentInstance() 
    
    def __init__(self):
        self.documentation = SkinToolsDocs
        
        
    def initialize(self):
        log.debug("creating headless data host")
        
        LayerDataModel.reset()
        restartEvents()

        Utils.loadPlugin()

        MayaEvents.registerScriptJobs()
        
        LayerDataModel.getInstance()
        
    def cleanup(self):
        '''
        cleanup any acquired resources
        '''
        scriptJobs.deregisterScriptJobs()
            
        log.debug("headless data host cleanup")


HeadlessDataHost.HANDLE = RefCountedHandle(HeadlessDataHost)        
    
#
#    ngSkinTools
#    Copyright (c) 2009-2015 Viktoras Makauskas. 
#    All rights reserved.
#    
#    Get more information at 
#        http://www.ngskintools.com
#    
#    --------------------------------------------------------------------------
#
#    The coded instructions, statements, computer programs, and/or related
#    material (collectively the "Data") in these files are subject to the terms 
#    and conditions defined by
#    Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License:
#        http://creativecommons.org/licenses/by-nc-nd/3.0/
#        http://creativecommons.org/licenses/by-nc-nd/3.0/legalcode
#        http://creativecommons.org/licenses/by-nc-nd/3.0/legalcode.txt
#         
#    A copy of the license can be found in file 'LICENSE.txt', which is part 
#    of this source code package.
#    

from maya import cmds
from ngSkinTools.utils import Utils
from ngSkinTools.log import LoggerFactory


log = LoggerFactory.getLogger("events")

class Signal:
    '''
    Signal class collects observers, interested in some particular event,and handles
    signaling them all when some event occurs. Both handling and signaling happens outside
    of signal's own code
    '''
    
    TOTAL_HANDLERS = 0
    
    def __init__(self,name=None):
        self.name = name
        self.reset();
        
    def reset(self):
        self.handlers = []
        self.executing = False
        
    
    def emitDeffered(self,*args):
        import maya.utils as mu
        mu.executeDeferred(self.emit,*args)
        
        
    def emit(self,*args):
        if self.executing:
            raise Exception,'Nested emit on %s detected' % self.name
        
        self.executing = True
        try:
            for i in self.handlers[:]:
                try:
                    i(*args)
                except Exception,err:
                    import traceback;traceback.print_exc()
        finally:
            self.executing = False
            

    class UiBoundHandler:
        '''
        Proxy wrapper for event handlers that has a method to deactivate 
        itself after when associated UI is deleted
        '''
        def __init__(self,handler,ownerUI,deactivateHandler):
            scriptJobs.scriptJob(uiDeleted=[ownerUI,self.deactivate])
            self.handler=handler
            self.deactivateHandler=deactivateHandler
        
        def deactivate(self):
            self.deactivateHandler(self)
            
            
        def __call__(self):
            self.handler()
            
            
    def addHandler(self,handler,ownerUI=None):
        if (ownerUI!=None):
            handler=self.UiBoundHandler(handler,ownerUI,self.removeHandler)
            
        self.handlers.append(handler)

    def removeHandler(self,handler):
        
        # if handler was wrapped, try finding the wrapper first
        for i in self.handlers:
            if isinstance(i, self.UiBoundHandler) and i.handler==handler:
                handler = i
                
        try:
            self.handlers.remove(handler)
        except ValueError:
            # not found in list? no biggie.
            pass
        


class EventsHost(object):
    def restart(self):
        for _, propertyValue in vars(self).iteritems():
            if isinstance(propertyValue, Signal):
                propertyValue.reset()

class LayerEventsHost(EventsHost):
    """
    layer system related events
    """
    
    def __init__(self):
        self.nameChanged = Signal('layerNameChanged')
        self.layerListModified = Signal('layerDataModified')
        self.currentLayerChanged = Signal('currentLayerChanged')
        self.currentInfluenceChanged = Signal('currentInfluenceChanged')
        self.layerSelectionChanged = Signal('layerSelectionChanged')
        self.layerListUIUpdated = Signal('layerListUIUpdated')
        self.layerAvailabilityChanged = Signal('layerAvailabilityChanged')
        self.influenceListChanged = Signal('influenceListChanged')
        self.mirrorCacheStatusChanged = Signal('mirrorCacheStatusChanged')


class MayaEventsHost(EventsHost):
    '''
    global maya-specific events
    '''
    def __init__(self):
        
        self.nodeSelectionChanged = Signal('nodeSelectionChanged')
        self.undoRedoExecuted = Signal('undoRedoExecuted')
        self.toolChanged = Signal('toolChanged')
        self.quitApplication = Signal('quitApplication')
        
    def registerScriptJob(self,jobName,handler):
        def mockHandler(*args,**kwargs):
            log.debug("running script job "+jobName)
            handler(*args,**kwargs)
            
        
        job = scriptJobs.scriptJob(e=[jobName,mockHandler if Utils.DEBUG_MODE else handler])
        

            
    def registerScriptJobs(self):
        self.registerScriptJob('SelectionChanged',self.nodeSelectionChanged.emit)
        self.registerScriptJob('Undo',self.undoRedoExecuted.emit)
        self.registerScriptJob('Redo',self.undoRedoExecuted.emit)
        self.registerScriptJob('ToolChanged',self.toolChanged.emit)        
        self.registerScriptJob('quitApplication',self.quitApplication.emit)    
        
    
    


def restartEvents():
    '''
    (re)creates signal holders in LayerEvents and MayaEvents  
    '''
    MayaEvents.restart()
    LayerEvents.restart()


class ScriptJobHost:
    def __init__(self):
        self.scriptJobs = []
        
    def scriptJob(self,*args,**kwargs):
        '''
        a proxy on top of cmds.scriptJob for scriptJob creation;
        will register a script job in a global created script jobs list
        '''
        job = cmds.scriptJob(*args,**kwargs)
        self.scriptJobs.append(job)
    
    def deregisterScriptJobs(self):
        for i in self.scriptJobs:
            try:
                cmds.scriptJob(kill=i)
            except:
                pass
        self.scriptJobs = []
        
scriptJobs = ScriptJobHost()

MayaEvents = MayaEventsHost()
LayerEvents = LayerEventsHost() 
