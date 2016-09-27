import sys
sys.__stdout__.write('#[__init__.py] MuTools (nothing to do)')









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



"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Developer's tools 

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""

=========================================
LITTLE MINOR DETAIL:)

        try:
            reload(modObj)
        except ImportError:
            # Module exists in memory but it was deleted: swallow the exception.
            print '[WARNING] The module object "{}" exists in memory but the ' \
                  'corresponding .py/.pyc is missing!'.format(modObj.__name__)
        except:
            # Module compile error: reraise!
            raise  
=========================================



import os 
MuToolsPath = "C:/Users/guido.pollini/Desktop/MuTools/"
if MuToolsPath not in os.sys.path:
    os.sys.path.append(MuToolsPath)


def reloadMuTools():
    import sys
    loadedModules = sys.modules
    MuToolsModules = [x for x in loadedModules if x.startswith('MuTools')]
    for mod in MuToolsModules:
        modObj = loadedModules[mod]
         
        # Some modules 'MuTools.' have None as moduleObject (why???)
        if modObj is not None:
            print '[{0}] Reloading from "{1}"...'.format(mod, modObj.__file__)
            reload(modObj)
            print '[{0}] Reloaded!'.format(mod)



import MuTools.XXXXXX
reloadMuTools()

"""