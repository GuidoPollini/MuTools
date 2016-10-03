import sys
sys.__stdout__.write('\n- [MuTools] __init__.py (nothing to do)')






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
import os 
MuToolsPath = "C:/Users/guido.pollini/Desktop/MuTools/"
if MuToolsPath not in os.sys.path:
    os.sys.path.append(MuToolsPath)
"""



"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                  POSITIONAL                KEYWORDED              EXTRA_POSITIONAL      EXTRA KEYWORDED
def FUNCTION(  a0, a1, ..., am,      k0=d0, k1=d1, ..., kn=dn,          *args,               **kwargs     ):...

When called with FUNCTION(PASSED_POSITIONAL, PASSED_KEYWORDED):
 - POSITIONAL is filled with the first items in PASSED_POSITIONAL, and what's left is put in EXTRA_POSITIONAL
 - each item of PASSED_KEYWORDED which is not in KEYWORDED is put in EXTRA_KEYWORDED

Put it simply: POSITIONAL and KEYWORDED rule; what's left goes into *args (list) or **kwargs (dict).
Note that the order here IS fundamental: *args and **kwargs must be the latter ones!
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


