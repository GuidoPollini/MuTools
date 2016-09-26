__version__ = '1.0.1' # 'MAJOR.MINOR.PATCH'

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Version 'MAJOR.MINOR.PATCH'

- 'PATCH' must be incremented if only backwards compatible bug fixes are 
  introduced. A bug fix is defined as an internal change that fixes incorrect 
  behavior.

- 'MINOR' must be incremented if new, backwards compatible functionality is 
  introduced to the public API. It MUST be incremented if any public API 
  functionality is marked as deprecated. It may be incremented if substantial
  new functionality or improvements are introduced within the private code. 
  It MAY include patch level changes. Patch version MUST be reset to 0 when 
  minor version is incremented.

- 'MAJOR' must be incremented if any backwards incompatible changes are 
  introduced to the public API. It MAY include minor and patch level changes.
  Patch and minor version MUST be reset to 0 when major version is 
  incremented.

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



"""
import os 
muToolsPath = r'C:\Users\Guido\Desktop\MuTools'
if muToolsPath not in os.sys.path:
    os.sys.path.append(muToolsPath)
import MuTools.MuUtils
reload(MuTools.MuUtils)
from MuTools.MuUtils import *
"""




"""
#---------------------------------------------------------------
# Reload all MuTools modules (by just applying it to 'MuTools')
#---------------------------------------------------------------
def reloadMuTools2():
    import sys
    loadedMods = sys.modules
    # All MuTools modules have "MuTools" as prefix (or namespace), no exception!
    MuToolsModObjs = [loadedMods[x] for x in loadedMods if x.startswith('MuTools')]
    for modObj in MuToolsModObjs:
        try:
            reload(modObj)
        except ImportError:
            # Module exists in memory but it was deleted: swallow the exception.
            print '[WARNING] The module object "{}" exists in memory but the ' \
                  'corresponding .py/.pyc is missing!'.format(modObj.__name__)
        except:
            # Module compile error: reraise!
            raise  

"""



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
        'MuTools.MuUI'
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

