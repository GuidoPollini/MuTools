__version__ = '1.0.3' 



import maya.cmds as MC

import inspect
import os
import sys
import time







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
    

    def __init__(self, globalLogId=None, verbosity=Log.STANDARD):
        self.verbosity = verbosity




    def __call__(self, *args):
        """
        Easy to call:
        log('Wonderful message incoming...')
        """
        if self.verbosity is None:
            return

        message = ' '.join([str(x) for x in args])
        print message




    def debug(self, *args):
        """
        Standard 'debugging' message (informative but not too much).
        >>> It should output NOT on the scriptEditor, but elsewhere!!!
        """

        if self.verbosity in (Log.DEBUG, Log.HARD_DEBUG):
            message = '[D] ' + ' '.join([str(x) for x in args])
            print message




    def hardDebug(self, *args):
        """
        HardDebug shows everything, function calls, internals...
        >>> Again, DON'T pollute the scriptEditor with this shit!
        """

        if self.verbosity == Log.HARD_DEBUG:
            message = '[H] ' + ' '.join([str(x) for x in args])
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
            stringifiedIterable = [str(x) for x in iterable]            
        else:    
            # Sort a <Set>
            stringifiedIterable = sorted([str(x) for x in iterable])
        
        if len(stringifiedIterable) > 0:
            for s in stringifiedIterable:
                print ' ', s
        else:
            print '  NONE'  





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












class Module(object):
    def loadingLog():
        pass
    def loadedLog():
        pass 





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



"""
import sceneCorrector
def muReload(module):
    reload(module)
    muModules = ['Utils', 'Core', 'Scene', 'UI']
    innerModules = dir(module)
    for mod in muModules:
        if mod in innerModules:
            modObj = getattr(module, mod)
            reload(modObj)
            print '[{}] Reloaded!'.format(mod)
            
            muReload(mod)
        

muReload(sceneCorrector)
"""

def reloadMuTools():
    loadedModules = sys.modules
    MuToolsModules = [x for x in loadedModules if x.startswith('MuTools')]
    for mod in MuToolsModules:
        modObj = loadedModules[mod]
        # Some modules 'MuTools.' have None as moduleObject (why???)
        if modObj is not None:
            print '- [{0}] Trying to reload from "{1}"...'.format(mod, modObj.__file__)
            try:
                reload(modObj)
                print '> [{}] Module reloaded!'.format(mod)            
            except ImportError:    
                # The module name was changed or doesn't exist anymore: swallow it!
                print '? [{0}] Module reload failed! The file "{1}" can\'t be found.'.format(mod, modObj.__file__)





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

