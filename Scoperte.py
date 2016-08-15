"""
NOTA: apparenteente Maya salva le posizioni dei vertici/normali in FLOAT, non DOUBLE...
pero i dati del transform reggnon i valori DOUBLE...

e' vero???
---------------------------------------------------------------------

This method returns a pointer to the internal vertex list for this mesh. The points 
are in local space.
The points are stored in a single contiguous array of floats, first by coordinate, 
then by element (xyzxyz...) There are three coordinate values, so each vertex is 
stored in 12 bytes of data, and the total array length is 12*numVertices() bytes.

This method is useful where performance is critical or memory resources are limited, 
as it avoids having to make a copy of the points as is done by getVertices. 
Care must be taken however as the returned pointer may become invalid if any 
changes are made to the mesh.
"""


"""
========================================================================================
W H A T   D O E S   " G L O B A L "   O B J E C T   M E A N   ?
========================================================================================
 - Don't pollute the userSetup.py ('cause it generates true globals)
 - if an object it's defined inside a module, isn't it automatically not global ?
   (i.e. protected by a namespace???)

"""


"""
========================================================================================
M A Y A  2 0 1 5     P Y T H O N      C L E A N     G L O B A L S
========================================================================================
        __builtins__ __builtin__ None
             __doc__ None        None
            __name__ None        None
         __package__ None        None
                cmds maya.cmds   C:\Program Files\Autodesk\Maya2015\Python\lib\site-packages\maya\cmds\__init__.py
                 mel maya.mel    C:\Program Files\Autodesk\Maya2015\Python\lib\site-packages\maya\mel\__init__.py

Note that [maya.cmds] and [maya.mel] are already imported...
"""





"""
========================================================================================
M O D U L E   A L I A S I E S
========================================================================================

Even if you have nested modules and each one perform the import of a module XXX, 
we end with JUST ONE module XXX, only with a lot of names bound to it.
Ex:

Different names bound to the module [maya.cmds]

print __cmds__.ls('persp')
print cmds.ls('persp')
print CM.MC.ls('persp')
print prodMenu.MC.ls('persp')
print prodMenu.validateMeshes.MC.ls('persp')
print prodMenu.YKR_renderTools.cmds.ls('persp')

The bound names are different than the "true name" (.__name__)
print WOW.__name__
print cmds.__name__
print CM.MC.__name__
print prodMenu.MC.__name__
print prodMenu.validateMeshes.MC.__name__

And if you check their id (memory addresses in CPython) they're the same:)

-----------------------------------------------------------------------------------
HENCE: import multiple times a module where you wish: you'll get a useful aliasing!
??? What happens if the module has some "code"???
-----------------------------------------------------------------------------------
"""