import MuTools.MuUtils as MUT
reload(MUT)

"""
import maya.cmds         as MC
import maya.OpenMaya     as OM
import maya.api.OpenMaya as OM2
"""

"""
import functools
import inspect
import os
import time
import types
"""



#------------------------------------------------------------------------------
# Loading module...
MUT.moduleLoadingMessage()
#------------------------------------------------------------------------------



"""""""""""""""""""""""""""""""""""
CLASS STRUCTURE
-----------------------------------
STATIC METHODS (@SORTED)
CLASS METHODS  (@SORTED)
CONSTRUCTOR/INITIALIZER
    __new__
    __init__
MAGIC METHODS  (@SORTED)
    __magicA__
    __magicB__
    __magicC__
    ...
METHODS        (@SORTED)
    methodA()
    methodB()
    methodC()
    ...

"""""""""""""""""""""""""""""""""""


"""""""""""""""""""""""""""""""""""
CLASS HIERARCHY
-----------------------------------
Bundle            [MASSIVES]
MuNode            [FACTORY]
DGNode          
  DAGNode         [ABSTRACT]
    Mesh
    Transform
      Joint
  ObjectSet  
  RenderLayer
Scene             [GLOBALS]    

"""""""""""""""""""""""""""""""""""

print 'fuckYou'






#------------------------------------------------------------------------------
# Module loaded!
MUT.moduleLoadedMessage()
#------------------------------------------------------------------------------