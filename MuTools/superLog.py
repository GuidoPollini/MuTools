import tempfile
##################################################################################################
##################################################################################################
##################################################################################################


"""


x = 71 PYTHON (names bound to objects)
  ||
int x_ = 71; C++
int& x = x_; (but in this case x cant point to an object of another type so this is WRONG)

"""

""" Apparently there are:
 QT(C++) SIGNALS/SLOTS
 PYTHON  SIGNALS/SLOTS
 
 For more details, look for 'Mark Summerfield', 
 "Introduction to GUI programming with Python and Qt"
""" 
# SIGNAL AS A CALLBACKS CONTAINER (INTERFACE)
#-------------------------------------------------------------------
# A 'Signal' is simply a 'callback container'!
# It allows to add callback from the outside of the object.
# Then, something inside may 'emit' it and the <SignalInstance>
# calls all the added callbacks
#
# YOU CAN ADD/REMOVE CALLBACKS FROM OUTSIDE
# (but somebody inside the object must ask the container to execute)
#
# It's "reason d'etre" is the ability to add callbacks from the 
# outside. When you wanna react to an event occurring in an object
# (implemented, by a cutom signal and the proper emission) you just
# do:
#  
#  (OUTSIDE) myObj.customSignal.connect(myCallback)
#   (INSIDE) myObj.customSignal.emit()
#
#  myObject.visibilityChanged.connect(interestedObj1.setVisibility)
#  myObject.visibilityChanged.connect(interestedObj2.setVisibility)
#
#  Inside myObject, somebody will call 
#  
#  self.visibilityChanged.emit(True)
#  self.visibilityChanged.emit(True)
#  
#  The methods put into .connect(...) can be predefined slots or 
#  whatever is callable and respect the signal signature
# DOC: 
# mySignal() --> emitted when the object does...

# It belongs to the object interface and you don't need to know
# its inner implementation (but don't forget that something inside
# the object will have to talk to the callback container, 
# i.e. 'emit' the 'signal')


#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------



class MuSignal(object):
    """
    RULES
    - if an object 'myObj' has a MuSignal 'mySignal' you can connect outside it with:
        myObj.mySignal.connect(callback)
        myObj.mySignal.connect(callback, isGeneric=False)
      The first sintax is a 'generic' connect; the callback can't recover myObj;
      with the secon syntax, mySignal will call (when myObj emit mySignal) the callback
      by adding a new kwarg 'MuEmitter=myObj'. Thus the callback must have a signature
      that accepts it, ex:
        myCallback(...., MuEmitter=None)

    - inside myObj there are two ways to emit a MuSignal:
        self.mySignal.emit(...)
        self.mySignal.emit(..., MuEmitter=self)
      It's up to the .connect to specify with the 'isGeneric' if the callback 
      desires to receive the caller object. 
      A callback who wanna know the emitter object, must add to its signature:
        def curiousCallback(*args, MuEmitter=None, **kwargs): ...

    """



    def __init__(self):
        # self._callbackList = [
        #     {'funcObj': <funcObj>,      'isGeneric': <bool>},
        #     {'funcObj': myCallbackObj1, 'isGeneric': True}, 
        #     {'funcObj': myCallbackObj2, 'isGeneric': False}, 
        #     ...
        # ]
        self._callbackList = []



    def emit(self, *args, **kwargs):
        for callback in self._callbackList: 
            # Check if the emitter has to be sent
            if callbackPair['isGeneric']:
                kwargs.pop('MuEmitter')

            callback(*args, **kwargs)


            
    def connect(self, funcObj, isGeneric=True):
        self._callbackList.append({'funcObj': funcObj, 'isGeneric': isGeneric})



    def listConnections(self):
        ...



    def hasCallback(self, callbackId):
        callbackFound = False
        for callback in self._callbackList.keys():
            callbackObj = callback['funcObj']
            # Check if the funcObj is found, by obj or by name
            if callbackId in (callbackObj, callbackObj.__name__):
                callbackFound = True
                break
        
        return callbackFound                



    def disconnect(self, callbackId):
        """
        ----------------------------------------------------------
        DESCRIPTION


        ARGUMENTS
          callbackId <funcObj>|<str>
            myObj.mySignal.disconnect(funcObj)
            myObj.mySignal.disconnect('funcName')    
        ---------------------------------------------------------
        """
        if self.hasCallback(callbackId):
            self._callbackList.pop(callback)








class MyShit(...):
    def __init__(self, ...):
        ....
        ....
        ....
        self.signal1 = MuSignal() # How to force 'signature'? i.e. MuSignal(str, int) ?
        self.signal2 = MuSignal()

    def update(self):
        ...
        self.signal1.emit(0, 0, MuEmitter=self)
        self.signal2.emit('pippo')    

def fuck(a, b):
    return 'shit', a, b

def cock(mess, MuEmitter=None):
    print mess

ms = MyShit()
ms.signal1.connect(fuck)
ms.signal2.connect(cock, cock2, isGeneric=False) # If 'isGeneric' send also the caller reference


"""
*************************************************************************************


****************************************************************************************
"""

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------




class GayWhore(QC.QObject):
    orgasm = QC.Signal()
    cum = QC.Signal()
    def fucked(self):
        #-----------------------------------------------------------------------------
        # WHAT DOES HAPPEN HERE???
        # Apparently, only QObject derived can manage a 'CALLBACKS CONTAINER'
        #
        # print type(GayWhore.orgasm) # Signal         (no interesting method)
        # print type(self.orgasm)     # SignalInstance (with emit, connect, disconnect)
        #-----------------------------------------------------------------------------
        self.orgasm.emit()
        self.cum.emit()

def a():
    print 'deeper'             
def b():
    print 'cumming'
    
g = GayWhore()

for i in range(10):
    g.orgasm.connect(a)
    g.cum.connect(b)
g.fucked()    

##################################################################################################
##################################################################################################
##################################################################################################








""" TIENILO EMPRE APERTO... E' PIU RAPIDO, PARECCHIO"""
""" Potresti attaccare un 'fileLog.close()' alla chousura dell'interfaccia grafica"""
""" o al try/except/finally per uno cript seza UI... """


import inspect

def logModuleCaller():
    # This works with CPython (Maya) and you can't use the generic 'getCaller'
    # because in this case, OR YOU CAN??? CHECK IT BETTER


    # Get the list of outer frames <6-uples>
    outerFrames = inspect.getouterframes(inspect.currentframe())
    # Frame 6-uple:
    # 0 --> <frame object at 0x000000012D1DEB88>
    # 1 --> <str> module caller path 
    # 2 --> <int>
    # 3 --> <module> module caller obj
    # 4 --> <list> caller Name, 
    # 5 --> <int>

    # Actual outer frames in the stack (in this special case, we need item 2)
    #     (0) logModuleCaller   (Here)
    #     (1) Log.__init__      (Here)
    # ==> (2) the caller module (The caller module, where Log(...) was called)
    #     (3) ...                                       ...
    #     ...
    callerStackIndex = 2 
    moduleName = inspect.getmodulename(outerFrames[callerStackIndex][1])
    del outerFrames

    return moduleName

import tempfile
import os

class Log(object):
    """
    Se un applicazione e decomposta in tanti pezzettini, vorrei un modo per ragruppare i log dei moduli chiamati
    Insomma... se diverse applicazioni usano lo stesso modulo, vorrei un log ciascuno
    Ex: hai un superShit.py e un superFuck.py che usano entrambi XXX.py
       superShit.log
       superFuck.log
       XXX_superShit.log (e qua un log() generico)
       XXX.superFuck.log (e qua un log generico)
    """


    def __init__(self, logFilePath=None, logInFile=True):
        """
        DESCRIPTION
          Each module should instance Log and use the instance to replace 'print':
          - log = Log() # TEMP
          - log(a, b, 'incredibile', d) # --> as replacement for 'print'
          - debug = log.debug
          - debug('Arg passed:', args, kwarg) # Log it only if the script is in debug omde
          - hard = log.hard
          - hard('Very verbose, function call, caller, ...') # Log only if in hardDebug mode
          This way, your script can choose if or not enter debug mode and everything
          is managed automatically (no verbose if not debug/hardDebug mode).
          It should provide a function hook to allow to connect log to another output

        ARGUMENTS
          logFilePath=None <str>
            A full path, ex 'C:\Users\Guido\Desktop\myLog.txt'.
            If None set the path to 'TEMP/MuLogs_MODULENAME/MODULENAME.txt'

          logInFile=True<bool>
            In case you don't wanna try to log also in a file. Note that
            in case of a bad 'logFileName' or without the proper right
            access to TEMP there'll be no logFile.


        RETURN
        """

        # In case of 'logInFile'==False or impossibility to open a logFile 
        self._logFileObj = None 
        self._mode       = 'normal' # 'normal', 'debug', extreme'
        # 'normal'  --> scriptEditor (output window is no UI)
        # 'debug'   --> logFile only (nowhere if logFile failed!)
        # 'extreme' --> function calls, etc etc (nowhere if logFile failed)
                
        if not logInFile:
            # No logFile needed; skip the entire part that follows
            return


        if logFilePath is None:            
            # The preferred solution: TEMP
            #--------------------------------------------------------
            # Auto hierarchy for log (preferred)
            #
            # [TEMP]
            #   |
            #   +-- [MULOGS]
            #   |      |
            #   |      +-- [ellipse_badgersMenu.log]
            #   |      +-- [alembicExporter_client.log]
            #   |      +-- [MODULE_NAME.log]
            #   |      +-- ...
            #   |      |
            #   |     ...
            #  ...
            #--------------------------------------------------------


            # logFilePath --> TEMP/muLogsFolderNames/logName
            muLogsFolderName = 'MULOGS'
            moduleCallerName = logModuleCaller()
            if moduleCallerName is None:
                # In the exceptional case that Log is instanciated in __main__
                # (the root interpreter, akak scriptEditor)
                moduleCallerName = 'MayaScriptEditor'
            logName = moduleCallerName + '.log'


            # Check for existence the Windows TEMP folder
            tempFolderPath = tempfile.gettempdir()
            if not os.path.isdir(tempFolderPath):
                # TEMP doesn't exist (this shouldn't be possible)
                print '[ERROR] no TEMP'
                return
            

            # Check if we have enough rights in TEMP
            try:

                # Create a test folder
                testFolderPath = os.path.join(tempFolderPath, 'testFolder')
                os.makedirs(testFolderPath)

                # Create a test file inside the test folder
                testFilePath = os.path.join(testFolderPath, 'testFile.txt')
                testFileObj  = file(testFilePath, 'a+', 0)
                testFileObj.write('Testing access rights...')
                testFileObj.seek(0)
                testFileObj.read()
                testFileObj.close()

                # Delete file and folder
                os.remove(testFilePath)
                os.rmdir(testFolderPath)      
               
                # If we get here with no exceptions, we have the right to 
                # create the folder/log

            except:
                # An exception il the latter operations means we have
                # not enough rights in TEMP
                print '[ERROR] Not enough rights!'
                return
            

            # Check/create the MULOGS folder
            muLogsFolderPath = os.path.join(tempFolderPath, muLogsFolderName)
            if not os.path.isdir(muLogsFolderPath):
                # No folder, create one
                os.makedirs(muLogsFolderPath)
            
            # The path for the TEMP log is ready
            logFilePath = os.path.join(muLogsFolderPath, logName)


        #---------------------------------------------------------------------------------
        # NOTE: at this point, 'logFilePath' has the proper TEMP path or the original path
        #---------------------------------------------------------------------------------
        # Open the log file and keep it constantly open (it's faster)
        # (append + read, buffer=0 --> no flush required)
        try:
            self._logFileObj = file(logFilePath, 'a+', 0) 
        except Exception as exc:
            print '[ERROR] Something went wrong: can\'t create the log!', exc
            return











class _Log(object):
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    'log.debug' and 'log.hardDebug' shouldn't pollute the 
    scriptEditor. Save the info elsewhere and make it accessible
    at ease!
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


    """
    LEADING CHARACTERS
    -  Nothing to say
    !  Something important or warning
    >  Success
    ?  Error/fatality
    @  Debug
     
    Ex:
    ! [MuTools.MuCore] Trying to reload from "C:/Users/guido.pollini/Desktop/MuTools/MuTools\MuCore.pyc"...
    """

    """
    WISHLIST

      from MuTools.MuUtils import Log
      log = Log('globalLogId')
      ...
      log.fileOutput = 'C:/blahblahblah.log'
      log.verbosity = Log.DEBUG
      ...
      log('Working on asset XXX...')
      log.debug('Data', data, lista, dico)
      log.('Completed')
   
    Probably a singleton for each logName (ex: MuCoreLog, MuSceneLog, MuToolsGlobalLog,...)
    """


    SILENT     = None
    STANDARD   = 0
    DEBUG      = 1
    HARD_DEBUG = 2
    

    @staticmethod
    def _stringifyArgs(args):
        # For <str> use str(), for another type of object use repr()
        #    str('soleil')  -->  soleil
        #   repr('soleil')  -->  'soleil' (useless)
        return ' '.join([str(x) if type(x) == str else repr(x) for x in args])



    def __init__(self, globalLogId=None, verbosity=None):
        self.verbosity = verbosity or Log.STANDARD



    def __call__(self, *args):
        """
        Easy to call:
        log('Wonderful message incoming...')
        """
        if self.verbosity is None:
            return

        #-----------------------------------------------------------------------------------------
        # NOTE
        #
        # I want something like this:
        # - log('The object', obj, 'is broken')  -->  The object "fuck"<reference> is broken!  
        # - namespace = str(ref.namespace())
        #
        # Hence:
        # - repr(obj)  -->  the 'developer' informative string
        # - str(obj)   -->  the replacement for 'objAsStr()', 'obj.stringify()', 'obj.name()', ...
        #
        #-----------------------------------------------------------------------------------------
        # As usual, forget the 'PYTHONIC IDEOLOGICAL SHIT': except for trivial cases (ex <str>, 
        # built-in containers of built-in types, ...) __repr__ NEVER even attempts to recover the 
        # original object via an eval() as if it was a perfect serialization/pickling/json...
        #
        # __repr__ exists only for my log/debug as developer!!!
        #  __str__ to avoid ugly 'xxx.object().asString()'  
        #-----------------------------------------------------------------------------------------
    
        message = Log._stringifyArgs(args)
        print message




    def debug(self, *args):
        """
        Standard 'debugging' message (informative but not too much).
        >>> It should output NOT on the scriptEditor, but elsewhere!!!
        """

        if self.verbosity in (Log.DEBUG, Log.HARD_DEBUG):
            message = '[D] ' + Log._stringifyArgs(args)
            print message




    def hardDebug(self, *args):
        """
        HardDebug shows everything, function calls, internals...
        >>> Again, DON'T pollute the scriptEditor with this shit!
        """

        if self.verbosity == Log.HARD_DEBUG:
            message = '[H] ' + Log._stringifyArgs(args)
            print message

    


    def iterable(self, iterable, title=None):
        """
        A simple prettyPrint for a generic iterable:
        TITLE 
          item1
          item2
          item3
          ...
        """
        print
        if title:
            print title
        
        if issubclass(type(iterable), list): 
            # Don't sort a <List>
            stringifiedIterable = [repr(x) for x in iterable]            
        else:    
            # Sort a <Set>
            stringifiedIterable = sorted([repr(x) for x in iterable])
        
        if len(stringifiedIterable) > 0:
            for s in stringifiedIterable:
                print ' ', s
        else:
            print '  NONE'  

    
    """
    ---------------------------------------------------------------------------------------------------
    WISHLIST

    'MuTools.MuScene': {'path':             'C:/Users/guido.pollini/Desktop/MuTools/MuTools/MuScene.py'
                        'version':          '1.0.4'
                        'lastModification': '05/10/16, 13:35:15'}
    'MuTools.MuCore':  {'path':             'C:/Users/guido.pollini/Desktop/MuTools/MuTools/MuCore.pyc'
                        'version':          '1.0.4'
                        'lastModification': '05/10/16, 14:56:19'}
    'MuTools.MuUI':    ['item0'
                        'item1'
                        'item2']
    ---------------------------------------------------------------------------------------------------
    """
    def dictionary(self, dico, title=None):
        def _recurse(actualDico, actualIndent=0):
            partialText = ''

            longestKey = max([len(repr(x) + ': ') for x in actualDico.keys()])

            for i, key in enumerate(actualDico.keys()):
                if i == 0:
                    newToAdd = (repr(key) + ': ').ljust(longestKey)
                    partialText += newToAdd
                    newIndent = actualIndent + len(newToAdd)
                else:
                    newToAdd = '\n' + ' ' * actualIndent + (repr(key) + ': ').ljust(longestKey)
                    partialText += newToAdd
                    newIndent = len(newToAdd)
                            
                if issubclass(type(actualDico[key]), dict):
                    partialText = partialText + '{' + _recurse(actualDico[key], newIndent) + '}'
                else:
                    partialText += repr(actualDico[key])
            
            return partialText 
            
        print '\n' + (title + '\n' if title else '') + _recurse(dico)






