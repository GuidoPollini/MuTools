__version__ = '1.0.4' 


import maya.cmds as MC

import inspect
import os
import sys
import time








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
# - 'lambda' return a <function> as 'def': same syntax, same rules (but one line, no statements)!
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








class Log(object):
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



    """
    import logging

    logPath = 'C:/Users/guido.pollini/Desktop/MuTools/muLog.log'
    logger = logging.getLogger('spamApplication')

    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s  %(levelname)s - %(message)s')
    consoleHandler.setFormatter(formatter)
    #logger.addHandler(consoleHandler)
    logger.info('FUCK YOU')
    for x in logger.handlers:
        print x.get_name()
        #logger.removeHandler(x)


    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(message)s')
    fh = logging.FileHandler('C:/Users/guido.pollini/Desktop/MuTools/mySuperLog.txt', mode='w')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.debug('Just fuck you.')    
    """  





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

