__version__ = '1.0.0' 



import inspect
import os
import sys
import time







"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                  POSITIONAL                KEYWORDED              EXTRA_POSITIONAL      EXTRA KEYWORDED
def FUNCTION(  a0, a1, ..., am,      k0=d0, k1=d1, ..., kn=dn,          *args,               **kwargs     ):...

When called with FUNCTION(PASSED_POSITIONAL, PASSED_KEYWORDED):
 - POSITIONAL is filled with the first items in PASSED_POSITIONAL, and what's left is put in EXTRA_POSITIONAL
 - each item of PASSED_KEYWORDED which is not in KEYWORDED is put in EXTRA_KEYWORDED

Put it simply: POSITIONAL and KEYWORDED rule; what's left goes into *args (list) or **kwargs (dict).
Note that the order here IS fundamental: *args and **kwargs must be the latter ones!
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""





"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
STRING OUTPUT (print, debug, fileLog)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Log(object):
    pass



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



























"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
===================================================================================
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

NO IDEA

___________________________________________________________________________________
===================================================================================
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


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



class Module(object):
    def loadingLog():
        pass
    def loadedLog():
        pass    



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
    sys.__stdout__.write('\n#[{0}.py] Loading module from "{1}"...'.format(moduleName, moduleFile))



def moduleLoadedMessage():
    moduleName, moduleFile = _getModuleCallerInfo()
    lastModification = os.path.getmtime(moduleFile) # Seconds passed between Epoch and last modification 
    formattedLastModification = time.strftime('%d/%m/%y, %H:%M:%S', time.localtime(lastModification))
    sys.__stdout__.write('\n#[{0}.py] Module loaded! Last update {1}.'.format(moduleName, formattedLastModification))



def genericMessage(message):
    moduleName, moduleFile = _getModuleCallerInfo()
    sys.__stdout__.write('\n#[{0}.py] {1}'.format(moduleName, message))



moduleLoadingMessage()

#
# ...
#
moduleLoadedMessage()

