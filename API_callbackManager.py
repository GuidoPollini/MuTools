"""
import os
if r'C:\Users\guido.pollini\Desktop\MuTools' not in OS.sys.path:
    OS.sys.path.append(r'C:\Users\guido.pollini\Desktop\MuTools')
import API_callbackManager as CM
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

shittyVar = 'Can you read this?' 
#id = OM.MSceneMessage.addCallback(OM.MSceneMessage.kBeforeNew, annihilateTurtle_callback)
#OM.MMessage.removeCallback(id)