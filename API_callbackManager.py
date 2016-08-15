"""
MODULE DOC (Guido Pollini)
"""

"""
import os
if r'C:\Users\guido.pollini\Desktop\MuTools' not in os.sys.path:
    os.sys.path.append(r'C:\Users\guido.pollini\Desktop\MuTools')
import API_callbackManager as CM
reload(CM)

print '\n[OK] Module{0}!'.format(__name__)
print '[MODULE GLOBALS]'
for g in sorted(globals().keys()):
  print ' ', g

"""


import maya.cmds     as MC
import maya.OpenMaya as OM
"""
<PyObject>
All object types are extensions of this type. This is a type which contains the information Python needs to treat a pointer to an object as an object. 
(it contains only the object's reference count and a pointer to the corresponding type object)


OM.MSceneMessage.addCallback(...) returns  a <PyCObject> (<MCallbackid> in C++)
OM.MMessage.removeCallback(...)   requires a <PyCObject> (<MCallbackid> in C++)

<PyCObject>
This subtype of PyObject represents an opaque value, useful for C extension modules who need to pass an opaque value 
(as a void* pointer) through Python code to other C code. It is often used to make a C function pointer defined in one
 module available to other modules, so the regular import mechanism can be used to access C APIs defined in dynamically loaded modules.
"""

def annihilateTurtle_callback(*args):
    result = '[CALLBACK] "kBeforeNew"'
    if MC.pluginInfo('Turtle', query=True, loaded=True):
        MC.unloadPlugin('Turtle', force=True)
        result += ': Turtle annihilated:)'
    print result    

print '\n[OK] Module "{0}" imported from "{1}"!'.format(__name__, __file__)
A_suckyVar  = 'globale?'
A_fuckyVar  = 'globale?'
A_shittyVar = 'globale?' 
print '[MODULE GLOBALS]'
for g in sorted(globals().keys()):
  print '  {0:>20.20s}  {1}'.format(g, globals()[g])

#id = OM.MSceneMessage.addCallback(OM.MSceneMessage.kBeforeNew, annihilateTurtle_callback)
#OM.MMessage.removeCallback(id)



"""
for x in sorted(globals()):
  name = None
  fromWhere = None
  try:
      name = globals()[x].__name__
      fromWhere = globals()[x].__file__
  except:
      pass    
  print '{0:>20.20}'.format(x), name, fromWhere
  
print x, name  
"""

"""
import os
if r'C:\Users\guido.pollini\Desktop\MuTools' not in os.sys.path:
    os.sys.path.append(r'C:\Users\guido.pollini\Desktop\MuTools')
import API_callbackManager as CM
reload(CM)
"""