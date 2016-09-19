import inspect
import os
import sys
import time




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


