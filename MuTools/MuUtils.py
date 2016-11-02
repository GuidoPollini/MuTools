__version__ = '1.0.5' 


import maya.cmds     as MC
import maya.OpenMaya as OM

import inspect
import os
import sys
import tempfile
import time





def isMayaStandalone():
    """ 
    ---------------------------------------------------------------------------          
    DESCRIPTION
      Detect if the current Maya instance was invoked in 'standalone' mode:
      - C++ core loaded;
      - commandEngine MEL/Python wrappers loaded;
      - No UI available;
      - No 'commandPort' available.

      Note that 'mayapy.exe' creates just a Python 2.7 interpreter with paths 
      pointing to the maya main folders, but that's NOT a Maya standalone! 
      To load the core you need these:

        import maya.standalone
        maya.standalone.initialize()
      
      Now you have a functional core and you can import safely the commandEngine
      and C++ API wrappers (BUT NOT QT WRAPPERS!!!)


    RETURN <bool>
      True  --> The UI is available
      False --> No UI, hence avoid completely Qt wrappers
    ---------------------------------------------------------------------------            
    """

    
    # MGlobal.mayaState() results
    #-------------------------------------------------
    #  0 --> OM.MGlobal.kInteractive  (full UI)
    #  1 --> OM.MGlobal.kBatch        (standalone as in mayabatch.exe)
    #  2 --> OM.MGlobal.kLibraryApp   (standalone as in mayapy.exe)
    #  3 --> OM.MGlobal.kBaseUIMode   (standalone ???)

    return True if OM.MGlobal.mayaState() != 0 else False





def muToolsPath():
    """ UGLY """
    # __file__  -->  C:\Users\guido.pollini\Desktop\MuTools\MuTools\MuUtils.py
    #  return   -->  C:\Users\guido.pollini\Desktop\MuTools\MuTools
    tokens = __file__.split('\\')
    path = '\\'.join(tokens[:-1])
    return path





#---------------------------------------------------------------------------------------------------
# <math> monkey patching
# There's no 'clamp' function... ouch
#---------------------------------------------------------------------------------------------------
#
# Note: "Lambda is q simplified alternative to def to create <function> objects"
#
#   lambda ARGUMENTS: EXPRESSION
#             ||
#             || (synonyms)
#             ||
#   def funcObj(ARGUMENTS): return EXPRESSION
#
# - 'lambda' return a <function> as 'def' does: same semantic and arg rules 
#   (but the code object must be composed of one line, only 1 expression and no statements)!
# 
# ----------------------------------------------------------------------------
# - Of course, comething like this (func1(), func2(), ...) is an expression
#   (every function/method returns something, None if no explicit return is there)
#   SO YOU CAN CONCATENATE CALLBACKS:)
# ----------------------------------------------------------------------------
# - EXPRESSION can involve function/method calls (they return always something, by default None)
# 
#                 lambda: EXPRESSION  -->  'def ?(): return EXPRESSION'
#                                          only for collateral effects of EXPRESSION
#
# lambda *args, **kwargs: EXPRESSION  -->  'def ?(*args, **kwargs): return EXPRESSION'
#                                          exactly as a function

import math
math.clamp = lambda value, minValue, maxValue: max(min(value, maxValue), minValue)




"""
USER SETUP
    if not os.environ.has_key('MAYA_SKIP_USERSETUP_PY'):
        try:
            for path in sys.path[:]:
                scriptPath = os.path.join( path, 'userSetup.py' )
                if os.path.isfile( scriptPath ):
                    import __main__
                    execfile( scriptPath, __main__.__dict__ )
"""

"""
#=====================================================================================
              _        _____             
             | |      |  __ \            
   __ _ _   _| |_ ___ | |  | | ___   ___ 
  / _` | | | | __/ _ \| |  | |/ _ \ / __|
 | (_| | |_| | || (_) | |__| | (_) | (__ 
  \__,_|\__,_|\__\___/|_____/ \___/ \___|
                                         
#=====================================================================================                                         

#--------------------------------------------------------------------------------
# Notes:
# - 'open' is a built-in function that returns a <file> object;
# - a <file> object has __enter__ and __exit__: hence it's a contextManager;
# - a <file> object is an iterable+iterator that iterates on lines.
#--------------------------------------------------------------------------------




filePath = 'C:\Users\guido.pollini\Desktop\MuTools\MuTools\MuScene.py'

def getProperName(name):
    # REGEXP here please
    temp = name.lstrip()
    temp = temp.split(' ')[1]
    temp = temp.split('(')[0]
    return temp
    
with open(filePath, 'r') as fileObj:
    # <file> is an iterable+iterator: the iterator returns a line...
    
    isInsideClass = False
    
    for line in fileObj:
        if line.startswith('def '):
            isInsideClass = False
            print '\ndef {}()'.format(getProperName(line))
        
        if isInsideClass and line.startswith('    def '):
            print '  {}'.format(getProperName(line))
                
        if line.startswith('class '):
            print '\n<{}>'.format(getProperName(line))
            isInsideClass = True    
                  
#=====================================================================================
"""



""" TIENILO EMPRE APERTO... E' PIU RAPIDO, PARECCHIO"""
""" Potresti attaccare un 'fileLog.close()' alla chousura dell'interfaccia grafica"""
""" o al try/except/finally per uno cript seza UI... """



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
            print '[LOG SUCCESS] Created the logFile "{}"!'.format(logFilePath)
        except Exception as exc:
            print '[ERROR] Something went wrong: can\'t create the log!', exc
            return



    @staticmethod
    def _stringifyArgs(*args):
        # For <str> use str(), for another type of object use repr()
        #    str('soleil')  -->  soleil
        #   repr('soleil')  -->  'soleil' (useless)
        return ' '.join([str(x) if type(x) == str else repr(x) for x in args])


    def __call__(self, *args):
        """
        Easy to call:
        log('Wonderful message incoming...')
        """

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
    
        message = Log._stringifyArgs(*args)
        try:
            self._logFileObj.write(message + '\n')
        except:
            # Log failed
            pass   

    def debug(self, *args):
        """
        Standard 'debugging' message (informative but not too much).
        >>> It should output NOT on the scriptEditor, but elsewhere!!!
        """
        
        self(*args)
        '''
        if self.verbosity in (Log.DEBUG, Log.HARD_DEBUG):
            message = '[D] ' + Log._stringifyArgs(args)
            print message
        '''



    def hardDebug(self, *args):
        """
        HardDebug shows everything, function calls, internals...
        >>> Again, DON'T pollute the scriptEditor with this shit!
        """
        
        self(*args)
        '''
        if self.verbosity == Log.HARD_DEBUG:
            message = '[H] ' + Log._stringifyArgs(args)
            print message
        '''


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











def getFolders(dirName, fullName=False):
    dirContent = os.listdir(dirName)
    prefix = dirName + '/' if fullName else ''        
    folders = [prefix + x for x in dirContent if os.path.isdir(dirName + '/' + x)]
    return folders





def getFiles(dirName, fullName=False):
    dirContent = os.listdir(dirName)
    prefix = dirName + '/' if fullName else ''        
    files = [prefix + x for x in dirContent if os.path.isfile(dirName + '/' + x)]
    return files



""""""""""""""""""""""""""""" 
'MuTools' recursive reloader

  import MuUtils
  reload(MuUtils)

  import myModule    
  MuUtils.muReload(myModule)
"""""""""""""""""""""""""""""
def muReload(modObj): 
    muModuleNames = ['Utils', 'Core', 'Scene', 'UI']
    
    def _recursiveMuReload(actualModObj, historyStr):
        innerModuleNames = dir(actualModObj)
        for modName in muModuleNames:
           if modName in innerModuleNames:
               modObj = getattr(actualModObj, modName)
               reload(modObj)
               
               # [myMod.Scene.Core.Utils]
               thisHistoryStr = historyStr + '.' + modName  
               print '[{}] Reloaded!'.format(thisHistoryStr)
               _recursiveMuReload(modObj, thisHistoryStr)
               
    _recursiveMuReload(modObj, modObj.__name__)
    
    # The monkey-patching module MUST be the last one, otherwise
    # a monkey-patched class will be revert to the original after
    # a reload (i.e. the classObj destroyed then rebuilt)
    reload(modObj)
    



def inspectMuTools():
    """
    {'MuTools.MuCore':  {'lastModification': '21/09/16, 16:15:05',
                         'path':             '.../MuCore.pyc',
                         'version':          '1.0.0'}, ...}
    """

    loadedModules = sys.modules 
    muModules = [
        'MuTools.MuUtils',
        'MuTools.MuCore',
        'MuTools.MuScene',
        'MuTools.MuUI', 
        'MuTools.MuMayaRemote'
    ]  
    
    muModulesDict = {}
    for modName in muModules:
        muModulesDict[modName] = None
        if modName in loadedModules:
            moduleObject              = loadedModules[modName]
            version                   = moduleObject.__version__
            path                      = moduleObject.__file__
            lastModification          = os.path.getmtime(path)  
            formattedLastModification = time.strftime('%d/%m/%y, %H:%M:%S', time.localtime(lastModification))

            muModulesDict[modName] = {
                'version':          version,
                'path':             path,
                'lastModification': formattedLastModification
            }
               
    return muModulesDict





def _getModuleCallerInfo():
    # This works with CPython (Maya); I don't give a fuck if it doesn't
    # work with other Python implementations! Seriously... 'Portable' my ass!

    # Frame object example (tuple)
    # ------------------------------------------------------------------
    # (<frame object at 0x000000012D1DEB88>, 
    #  'C:\\Users\\guido.pollini\\Desktop\\MuTools\\MuTools\\MuCore.py', 
    #  223, 
    #  '<module>', 
    #  ['reload(MuTools.MuUtils)\n'], 
    #  0
    # )
    #
    # Note that item [1] is the module path! 

    outerFrames = inspect.getouterframes(inspect.currentframe())

    # Actual stack (in this special case, we need item [2])
    # ---------------------------------------------------------------------
    #     (0) _getModuleCallerInfo                      (Here)
    #     (1) moduleLoadingMessage/moduleLoadedMessage  (Here)
    # ==> (2) the caller module                         (The caller module)
    #     (3) ...                                       (Irrelevant)
    #     (4) ...                                       ...
    #     ...

    callerStackIndex = 2 
    moduleName = inspect.getmodulename(outerFrames[callerStackIndex][1])
    moduleFile = outerFrames[callerStackIndex][1]
    del outerFrames

    return (moduleName, moduleFile)





def moduleLoadingMessage():
    # sys.__stdout__ is the original outputHandler, in this case the 'outputWindow' of Maya.
    # When the UI is available, 'print' outputs to sys.stdout!
    moduleName, moduleFile = _getModuleCallerInfo()
    sys.__stdout__.write('\n- [{0}.py] Loading module from "{1}"...'.format(moduleName, moduleFile))





def moduleLoadedMessage():
    moduleName, moduleFile = _getModuleCallerInfo()
    lastModification = os.path.getmtime(moduleFile) # Seconds passed between Epoch and last modification 
    formattedLastModification = time.strftime('%d/%m/%y, %H:%M:%S', time.localtime(lastModification))
    sys.__stdout__.write('\n> [{0}.py] Module loaded! Last update {1}.'.format(moduleName, formattedLastModification))





def genericMessage(message):
    moduleName, moduleFile = _getModuleCallerInfo()
    sys.__stdout__.write('\n- [{0}.py] {1}'.format(moduleName, message))


 











moduleLoadingMessage()

#
# ...
#
moduleLoadedMessage()

