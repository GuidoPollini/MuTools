import maya.cmds as MC

def connect(nodeList):
    if MC.objExists("__pointerHolder"):
        MC.delete("__pointerHolder")
    
    numberOfItems = len(nodeList)    
    MC.createNode("transform", n="__pointerHolder")
    for i, node in enumerate(nodeList):
        MC.addAttr("", longName="holder_" + str(i), attributeType="message")
        MC.addAttr(node, longName="__copyHolder_" + str(i), attributeType="message")
        MC.connectAttr("__pointersHolder.holder_" + str(i), node + ".__copyHolder_" + str(i))
nodeList = MC.ls(sl=True)    
connect(nodeList)    


import maya.cmds as MC


""" STA ROBA DEVE ESSERE PERFETTA... e sono due match differenti che alterano il significato quando utilizzi
    pivot non banali...
"""
match() --> the final position; pivots forgotten
pivotalMatch() --> pivots and all stuff (you need to rotate!)

def perfectMatch(slave="", master=""):
    if master == "" and slave == "":
        sel = MC.ls(sl=True)
        slave = sel[0]
        master = sel[1]
    rt = MC.xform(master, query=True, rt=True, ws=True)
    rp = MC.xform(master, query=True, rp=True, ws=True)
    ra = MC.xform(master, query=True, ra=True, ws=True)
    ro = MC.xform(master, query=True, ro=True, ws=True)
    t  = MC.xform(master, query=True, t=True, ws=True)

    MC.xform(slave, ro=ro, ws=True)
    MC.xform(slave, ra=ra, ws=True)
    MC.xform(slave, rt=rt, ws=True)
    MC.xform(slave, rp=rp, ws=True)
    MC.xform(slave, t=t, ws=True)

def basicMatch(slave="", master=""):
    if master == "" and slave == "":
        sel = MC.ls(sl=True)
        slave = sel[0]
        master = sel[1]    
    mat = MC.xform(master, query=True, matrix=1, ws=1)
    MC.xform(slave, matrix=mat, ws=1)

#perfectMatch()
basicMatch()



"""
=================================================================================================================================================================
 _    _                                     
| |  | |                                    
| |  | |_ __ __ _ _ __  _ __   ___ _ __ ___ 
| |/\| | '__/ _` | '_ \| '_ \ / _ \ '__/ __|
\  /\  / | | (_| | |_) | |_) |  __/ |  \__ \
 \/  \/|_|  \__,_| .__/| .__/ \___|_|  |___/
                 | |   | |                  
                 |_|   |_|    

=================================================================================================================================================================                 
"""

""""""""""""""""""""
""" WORKING CODE """
""""""""""""""""""""
import maya.cmds as MC

def _getWorldT(object):
    """
    object = STRING, LIST of STRINGS
    return = 3LIST, LIST of 3LIST
    """
    if isinstance(object, list):
        # "massive" _getWorldT
        t = []
        for node in object:
            t.append(MC.xform(node, query=True, translation=True, worldSpace=True))
    if isinstance(object, str):
        # single object "string version"  
        t = MC.xform(object, query=True, translation=True, worldSpace=True)
    return t 
    
def _getLocalT(objectName):
    t = MC.xform(self.name, query=True, translation=True, objectSpace=True)
    return t             
       
class Transform(object):
    def __init__(self, name):
        self.name = name
    
    """ setWorld """    
    def setWorldT(self, *args):
        translationValue = None
        if len(args) == 3:
            # 3 simple values
            translationValue = [args[0], args[1], args[2]]
        if len(args) == 1:
            argument = args[0]
            if isinstance(argument, list) or isinstance(argument, tuple):
                # 3list or 3tuple
                translationValue = [argument[0], argument[1], argument[2]]               
            elif isinstance(argument, str):
                # Match another object ("string")
                translationValue = _getWorldT(argument)
            elif isinstance(argument, Transform):
                # Mathc another object ("Transform")
                translationValue = _getWorldT(argument.name)    
        try:
            MC.xform(self.name, translation=translationValue, worldSpace=True)    
        except Exception as exc:
            MC.error("[FATALITY] " + str(exc))
            
        # allows concatenation
        return self
    
    """ getWorld """   
    def getWorldT(self):
        # Return a list, to allow something like this:
        #  object.getWorldT()[1] = 0    
        t =  _getWorldT(self.name)
        return t      
    def getWorldTx(self):
        return self.getWorldT()[0]      
    def getWorldTy(self):
        return self.getWorldT()[1]      
    def getWorldTz(self):
        return self.getWorldT()[2]     
    def getLocalT(self):
        t = _getLocalT(self.name)
        return t      
    def getLocalTx(self):
        return self.getLocalT()[0]      
    def getWorldTy(self):
        return self.getLocalT()[1]      
    def getWorldTz(self):
        return self.getLocalT()[2]                        
                      
print _getWorldT("shit")
print _getWorldT(["fuck", "ass", "cock", "shit"])











import maya.cmds as MC

def _getWorldT(object):
    """
    object = STRING, LIST of STRINGS
    return = 3LIST, LIST of 3LIST
    """
    if isinstance(object, list):
        # <string> list
        t = []
        for node in object:
            t.append(MC.xform(node, query=True, translation=True, worldSpace=True))
    if isinstance(object, str):
        # single <string>  
        t = MC.xform(object, query=True, translation=True, worldSpace=True)
    return t 
    
def _getLocalT(objectName):
    t = MC.xform(self.name, query=True, translation=True, objectSpace=True)
    return t             
       
class Transform(object):
    def __init__(self, name):
        self.name = name
    
    """ setWorld """    
    # CONTROLLA SE REGISCE BENE AI PIVOT SCAZZATI
    # ... deve!
    
    # FALLISCE MISERAMENTE:)
    # (buon inizio)
    def setWorldT(self, *args):
        translationValue = None
        if len(args) == 3:
            # <1, 2, 3>
            translationValue = [args[0], args[1], args[2]]
        if len(args) == 1:
            argument = args[0]
            if isinstance(argument, list) or isinstance(argument, tuple):
                # <3tuple> or <list>
                translationValue = [argument[0], argument[1], argument[2]]               
            elif isinstance(argument, str):
                # Match a <string>
                translationValue = _getWorldT(argument)
            elif isinstance(argument, Transform):
                # Mathc a <Transform>
                translationValue = _getWorldT(argument.name)    
        try:
            MC.xform(self.name, translation=translationValue, worldSpace=True)    
        except Exception as exc:
            MC.error("[FATALITY] " + str(exc))
            
        # Return <self> to allow <.>-concatenation
        return self
    
    """ getWorld """   
    def getWorldT(self):
        # Return a <list> to allow maths    
        t =  _getWorldT(self.name)
        return t      
    def getWorldTx(self):
        return self.getWorldT()[0]      
    def getWorldTy(self):
        return self.getWorldT()[1]      
    def getWorldTz(self):
        return self.getWorldT()[2]     
    def getLocalT(self):
        t = _getLocalT(self.name)
        return t      
    def getLocalTx(self):
        return self.getLocalT()[0]      
    def getWorldTy(self):
        return self.getLocalT()[1]      
    def getWorldTz(self):
        return self.getLocalT()[2]                        
                      
A = Transform("A")
B = Transform("B")

A.setWorldT(B)                      
          










"""
=================================================================================================================================================================
     _     _ _   
    | |   (_) |  
 ___| |__  _| |_ 
/ __| '_ \| | __|
\__ \ | | | | |_ 
|___/_| |_|_|\__|

=================================================================================================================================================================
"""

fuck = ... a transform
fuck.setWorldTRS("DEFAULT")\
    .setIdentityTRS()\
    .setLocalT(0, 0, 0)\
    .setLocalRx(12)\
    .setLocalSy(2.1)\
    \
    .matchWorldTRS("nodoDelCazzo")\
    .matchLocalT("farewell")\
    \
    .lockAttr("tx", "ty", "rx")\
    .unlockAttr("T", "R", "S")\
    .hideAttr("fava", "none", "die")\
    .showAttr("fuck")\
    \
    .addAttr("style", ["IK", "FK", "HYBRID", "NONE"])\
    .lockAttr("style")
    .setAttr("style", "FK")
    \
    .setOverrides(enable=1, displayType="REFERENCE", lod="bb", color=12)\
    .setOverrides(e=1, dt="REFERENCE", lod="bb", c=12)\
    .enableOverrides(1)\
    .overrideDisplayType("REFERENCE")\
    .overrideColor(13)\
    .overrideVisibility(1)\
    \
    .setVisibility(1)\
    .setInheritTransform(0)\
    .setRotateOrder("xzy")\
    .setDisplayHandle(1)\
    .displayLocalAxis(1)\
    \
    .connectOutputPlug("attribFuck", ["pippo.associazioneone", "obj2.pip", "obj3.ppp"])\
    .connectInputPlug("cazzone.size", "poppolo")







---------------------------------------------------------------------------
---------------------------------------------------------------------------
---------------------------------------------------------------------------
RIG PATTERNS

EASY CODE (WRAPPERS)
- esattamente IDENTICO a cosa ottieni manualmente con maya
- e' la pratica di cio che serve e si fa, che guida la sintassi e la semantica

ABSTRACT MODEL
- qua devi andare per forza OOP e QT
- UI PARAMETERS (not necessarily visual)
- VISUAL (guide)

--> devi salvare i dati che identificano il RIG PATTERN 
--> agganciarci opzioni in piu, e.g. simmetria
--> se possibile memorizzare connessioni
---------------------------------------------------------------------------
---------------------------------------------------------------------------
----------------------------------------------------------------------------


"""
#################################################à
NOTA BENE:
lo scopo non e' di rifare PYMEL, ma di avere un linguaggino che copia 
ESATTAMENTE quello che faresti in MAYA durante la cotruzione di un cuteRig

RICONOSCI PATTERN --> code it (with a PROCEDURAL easy to write and SPELLED OUT minilanguage)

- il wrap deve essere amichevole al massimo e ridurre i FLAG in favore di metodi usati spesso
  (i.e. 
   cubo.getWorldTR()

   pos = xxx.getWorldT("pisello")
   pos[2] += 99
   cazzo.setWorldT(pos)

   rot = pallina.getParent().getWorldR()
   VS
   rot = getWorldR(getParent(pallina))

   sfera.setLocalTRS(cubo.getLocalTRS())
   sfera.setWorldS(1, 1, 1)


   cubo.lockAttr("pippo", "cazzo", "fuffa")\
       .keyableAttr("shit", "die", "never")\
       .hideAttr("visibility")\
       \
       .addAttr("integer", 12)\
       .addAttr("float", =.9)\
       .addAttr("string", "dioporco")\
       .addAttr("boolean", True)\
       \
       .lockAttr("extreme")\
       .connectAttr("pippo", "shit.fava")
       \
       .addAttr("mode", ["IK", "FK", "HYBRID"])
    
    .addAttr determina il tipo passato e crea il troiaio corrispondente... se lo usi senza troppe cazzate, e' sicuro

    VS

    setAttr(cubo + ".pippo", e=1, l=1)
    setAttr(cubo + ".shit", e=1, unk=0)
    setAttr(cubo + ".die", e=1, unk=0)
    setAttr(cubo + ".never", e=1, unk=0)
    addAttr(cubo, "string", type="string")

   connectOutputPlug("source", "dest1", "dest2", "dest3"...)
   
   setParent("son1", "son2", "son3", "parent")
   ["son1", "shit1", "boa", "sss"].setParent("genitore")
   
   ["shit", "fuck", "dilco", "die"].addAttr("pippolo", v=20, locked=1)...
   
   scazzo.setVisibility(0)\
         .setWorldT(0, 0, 0)\
         .drawingOverrides(1)\
         .colorOverride(13)\
         .setparent("ciaspo")

- USA LA PRATICA DI RIG per la sintassi
- la semantica deve essere ESATTAMENTE CIO CHE FAI IN MAYA, senza merda in piu
- PYMEL wrappa MMatrix, MPoint, MVector MQuaternion, MEuler... puoi sfuttarlo se vuoi
##################################################
"""



def connectAttr( source, destination, **kwargs ):
    """
    Maya Bug Fix: even with the 'force' flag enabled, the command would raise an error if the connection already existed.
    """
    if kwargs.get('force', False) or kwargs.get('f', False):
        try:
            cmds.connectAttr( source, destination, **kwargs )
        except RuntimeError, e:
            if str(e) != 'Maya command error':
                # we only want to pass on a certain connection error.  all others we re-raise
                raise e
    else:
        cmds.connectAttr( source, destination, **kwargs )
def disconnectAttr( source, destination=None, inputs=None, outputs=None,
                    **kwargs ):
def getAttr( attr, default=None, **kwargs ):
    """
Maya Bug Fix:maya pointlessly returned vector results as a tuple wrapped in a list ( ex.  '[(1,2,3)]' ). This command unpacks the vector for you.
def setAttr( attr, *args, **kwargs):
    """
Maya Bug Fix:
  - setAttr did not work with type matrix.

Modifications:
  - No need to set type, this will automatically be determined
  - Adds support for passing a list or tuple as the second argument for datatypes such as double3.
  - When setting stringArray datatype, you no longer need to prefix the list with the number of elements - just pass a list or tuple as with other arrays
  - Added 'force' kwarg, which causes the attribute to be added if it does not exist.
        - if no type flag is passed, the attribute type is based on type of value being set (if you want a float, be sure to format it as a float, e.g.  3.0 not 3)
        - currently does not support compound attributes
        - currently supported python-to-maya mappings:

            python type  maya type
            ============ ===========
            float        double
            ------------ -----------
            int          long
            ------------ -----------
            str          string
            ------------ -----------
            bool         bool
            ------------ -----------
            Vector       double3
            ------------ -----------
            Matrix       matrix
            ------------ -----------
            [str]        stringArray
            ============ ===========
    Modifications:
  - If no destination is passed, then all inputs will be disconnected if inputs
      is True, and all outputs will be disconnected if outputs is True; if
      neither are given (or both are None), both all inputs and all outputs
      will be disconnected

                            # stringName should be a valid mel name, ie
                            #   cmds.select(stringName)
                            # should work
        


        >>> cam.attr('visibility')
        Attribute(u'persp.visibility')

    Unlike the shorthand syntax, this method is capable of being passed attributes which are passed in as variables:

        >>> for axis in ['scaleX', 'scaleY', 'scaleZ']:
        ...     cam.attr( axis ).lock()

def _patchMVector() :
    def __len__(self):
        """ Number of components in the Maya api Vector, ie 3 """
        return 3
    type.__setattr__(_api.MVector, '__len__', __len__)
    def __iter__(self):
        """ Iterates on all components of a Maya api Vector """
        for i in xrange(len(self)) :
            yield _api.MVector.__getitem__(self, i)
    type.__setattr__(_api.MVector, '__iter__', __iter__)


###############################################àà
    def lock(self, checkReference=CHECK_ATTR_BEFORE_LOCK):
        "setAttr -locked 1"
        return self.setLocked(True, checkReference=checkReference)

    def unlock(self, checkReference=CHECK_ATTR_BEFORE_LOCK):
        "setAttr -locked 0"
        return self.setLocked(False, checkReference=checkReference)

    def setLocked(self, locked, checkReference=CHECK_ATTR_BEFORE_LOCK):
        '''
        Sets the locked state for this plug's value. A plug's locked state determines whether or not the plug's value can be changed.

        :Parameters:
            locked : `bool`
                True if this plug's value is to be locked
            checkReference : `bool`
                Set True to raise errors on referenced attributes.

                By default pymel and the maya api do not check if the node is referenced before
                setting the locked state. This is unsafe because changes to the locked state on
                referenced nodes are not saved with the scene.
        '''


    def insertInput(self, node, nodeOutAttr, nodeInAttr ):
        """connect the passed node.outAttr to this attribute and reconnect
        any pre-existing connection into node.inAttr.  if there is no
        pre-existing connection, this method works just like connectAttr.

        for example, for two nodes with the connection::

            a.out-->b.in

        running this command::

            b.insertInput( 'c', 'out', 'in' )

        causes the new connection order (assuming 'c' is a node with 'in' and 'out' attributes)::

            a.out-->c.in
            c.out-->b.in
        """

#########################################

    def inputs(self, **kwargs):
        """
        ``listConnections -source 1 -destination 0``

        see `Attribute.connections` for the full ist of flags.

        :rtype: `PyNode` list
        """

        kwargs['source'] = True
        kwargs.pop('s', None )
        kwargs['destination'] = False
        kwargs.pop('d', None )

        return listConnections(self, **kwargs)

    def outputs(self, **kwargs):
        """
        ``listConnections -source 0 -destination 1``

        see `Attribute.connections` for the full ist of flags.


   def isConnectedTo(self, other, ignoreUnitConversion=False, checkLocalArray=False, checkOtherArray=False ):
        """
        Determine if the attribute is connected to the passed attribute.

        If checkLocalArray is True and the current attribute is a multi/array, the current attribute's elements will also be tested.

        If checkOtherArray is True and the passed attribute is a multi/array, the passed attribute's elements will also be tested.

        If checkLocalArray and checkOtherArray are used together then all element combinations will be tested.

        """

        if cmds.isConnected( self, other, ignoreUnitConversion=ignoreUnitConversion):
            return True

def uniqueObjExists( name ):
    '''Returns True if name uniquely describes an object in the scene.
    '''
    all = cmds.ls(name)
    # in case result is None...
    return all and len(all) == 1

####################################
CONTROLLA COSA FA SUL DUPLICATE... maya scazza clamorosamente sui nomi delle copie
####################################
def rename( obj, newname, **kwargs):
    """
Modifications:
    - if the full path to an object is passed as the new name, the shortname of the object will automatically be used
    """
    import nodetypes, other
    # added catch to use object name explicitly when object is a Pymel Node
    if isinstance( newname, nodetypes.DagNode ):
        newname = newname.nodeName()
    else:
        newname = other.DagNodeName(newname).nodeName()

    return PyNode( cmds.rename( obj, newname, **kwargs ) )
def group( *args, **kwargs ):
    """
Modifications
  - if no objects are passed or selected, the empty flag is automatically set
Maya Bug Fix:
  - corrected to return a unique name
    """
    if not args and not cmds.ls(sl=1):
        kwargs['empty'] = True

    newGroup = cmds.group(*args, **kwargs)

    if cmds.versions.current() >= cmds.versions.v2014:
        # bug was fixed in 2014, so we can just cast to a PyNode and return...
        return PyNode(newGroup)
    else:
        # found an interesting bug. group does not return a unique path, so the following line
        # will error if the passed name is in another group somewhere:
        # Transform( cmds.group( name='foo') )
        # luckily the group command always selects the last created node, so we can just use selected()[0]
        return selected()[0]

def listRelatives( *args, **kwargs ):
    """
Maya Bug Fix:
  - allDescendents and shapes flags did not work in combination
  - noIntermediate doesn't appear to work

Modifications:
  - returns an empty list when the result is None
  - returns an empty list when the arg is an empty list, tuple, set, or
        frozenset, making it's behavior consistent with when None is passed, or
        no args and nothing is selected (would formerly raise a TypeError)
  - returns wrapped classes
  - fullPath is forced on to ensure that all returned node paths are unique

    :rtype: `DependNode` list
    """      
def listConnections(*args, **kwargs):
    """
Modifications:
  - returns an empty list when the result is None
  - returns an empty list (with a warning) when the arg is an empty list, tuple,
        set, or frozenset, making it's behavior consistent with when None is
        passed, or no args and nothing is selected (would formerly raise a
        TypeError)
  - When 'connections' flag is True, the attribute pairs are returned in a 2D-array::

        [['checker1.outColor', 'lambert1.color'], ['checker1.color1', 'fractal1.outColor']]

  - added sourceFirst keyword arg. when sourceFirst is true and connections is also true,
        the paired list of plugs is returned in (source,destination) order instead of (thisnode,othernode) order.
        this puts the pairs in the order that disconnectAttr and connectAttr expect.
  - added ability to pass a list of types

    """
    # translate dict or list for enumName
    enums = kwargs.pop('en', kwargs.pop('enumName', None))
    if enums is not None:
        kwargs['enumName'] = _toEnumStr(enums)


setAttr with tuples and lists
            elif datatype in ['Int32Array', 'doubleArray']:
                # int32 and double arrays:
                #   actually fairly sane
                # ex:
                #     setAttr('loc.doubleArray',[1,2,3] )
                # becomes:
                #     cmds.setAttr('loc.doubleArray',[1,2,3],type='doubleArray')
                args = (tuple(arg),)
            else:
                # others: short2, short3, long2, long3, float2, etc...
                #    args must be expanded
                # ex:
                #     setAttr('loc.foo',[1,2,3] )
                # becomes:
                #     cmds.setAttr('loc.foo',1,2,3 )
                args = tuple(arg)


""" OTTIMA COSA....
    quando devi tottcare diversi parametri di un nodo, puoi fare cosi:
    e' rapido, amichevole e meno codice. poi piu intiutivo perche e come
    "CLICCARE I BOTTONI"
"""  
cubbo.setWorldTRS(0,0,0,0,0,0,1,1,1)\
     .setVisibility(True)\
     .addAttr("pippo", "shit")\
     .lockAttr("pippo")
     .setSize(12)\
     \
     .overrides(True)\
     .colorOverride("red")
     \
     .setVisibility(True)\
     .addAttr("pippo", "shit")\
     .lockAttr("pippo")
     .setSize(12)  

####################################################################################################à
""" ARGUMENT ALIASES """
####################################################################################################
def getParent(self, **kwargs):
    
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """ THIS BREAKS IF NONE IS USED AS AN ARGUMENT... IS IT? """
    """ ... probably not. None is Python, MEL shouldn't have a corresponding value passed"""
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    # USE "is not" to compare to None...
    # "is" compares the identity, the other evaluater a method __eq__
    # ... se ci pensi, in una classe == a priori non significa nulla... va definito
    # None e una classe con un solo oggetto... cambia poco ma e piu veloce 

    # "fullDAGPath" argument
    fullDAGPathFlag = _getArgumentValue("fullDAGPath", "f", **kwargs)
    if fullDAGPathFlag is not None:
        # it's present and recovered; otherwise nnothing to do
        pass
        
    # "noIntermediates" argument
    noIntermediatesFlag = _getArgumentValue("noIntermediates", "ni", **kwargs)
    if noIntermediatesFlag is not None:
        # it's present and recovered; otherwise nnothing to do
        pass
        
def _getArgumentValue(longName, shortName, **kwargs):    
    # or to make it faster, in case of ambiguity make "longName" always win    
    if longName in kwargs and shortName in kwargs:
        MC.error("function badly called! Use short or long name, not both")
    elif  longName in kwargs:
        return kwargs[longName]
    elif shortName in kwargs:
        return kwargs[shortName]
    else:
        return None

###################################################################################################à

""" SPLITTING^OPTIMIZIING COMMANDS """
#######################################################################################################################
listRelatives([objects], 
              [allDescendents=boolean], 
              [allParents=boolean], 
              [children=boolean],
              [fullPath=boolean], 
              [noIntermediate=boolean], 
              [parent=boolean], 
              [path=boolean], 
              [shapes=boolean], 
              [type=string]) 
#######################################################################################################################
def getParent(self, fullDAGPath=0, f=0):
    """
    fullDAGPath <f>: if 1, returns the fullDAGPath of the parent, otherwise the "minimal name" 
                     which identifies the parent (i.e. MEL-valid)
    return: DAGNode or None (if son of the world)
    """
def getChildren(self, fullDAGPath=0, f=0, noIntermediates=1, ni=1, type="", t=""):
def getChildrenShapes(self, fullDAGPath=0, f=0, noIntermediates=1, ni=1):

transss.getChildrenShapes()
... a Shape node or a list of Shape nodes or None    

cubbo.getParent(fullDAGPath=0)
cubbo.getParent(f=1)
cubbo.getParent()

cubo.insertTransform("name", t=, r=, s=)

class DAGNode(object):
    def getWorldT(self):
        print "SHIT"
        return self
    def setLocalR(self, x,y,z):
        print "merda"
        return self    

cubbo = DAGNode()    

disconnectPlug(plug1, plug2, ....)
disconnectInputPlug(plug1, ...)
disconnectOutputPlug(plug)

cylinder.addAttr(longName="fuffa", type="string", value="", defaultValue="", locked=0, keyable=0)
cylinder.addAttr(ln="fuffa", t="string", v="", dv="", l=1, k=0)


cubbo.getParent()

cubbo.getParent(fullDAGPath=1)
cubbo.getParent(f=1)

cubbo.getParent(minimalDAGPath=1)
cubbo.getParent(m=1)

trans.getShapes(fullDAGPath=1)

renameNode("old", "new") # CHECK ALWAYS NAME AMBIGUITY


""""""""""""""""""""""""""""""""""""""""""
""" WOOOOOOOOOOOOWWWW :)
"""""""""""""""""""""""""""""""""""""""""
cubbo.setWorldTRS(0,0,0,0,0,0,1,1,1)\
     .setVisibility(True)\
     .addAttr("pippo", "shit")\
     .lockAttr("pippo")
     .setSize(12)\
     \
     .overrides(True)\
     .colorOverride("red")
     \
     .setVisibility(True)\
     .addAttr("pippo", "shit")\
     .lockAttr("pippo")
     .setSize(12)
""""""""""""""""""""""""""""""""""""""""""

da confrontare con il corrispondente PyMel, MEL, python






"""
che forse possa usare dei DECORATORS per riciclare tutti sti troiai che si assomigliano???
FACTORIES???
"""

##############################
"""
NOTA BENE:
 deve essere un insieme di oggetti che copiano la costruzione in MAYA
 che e SEQUENZIALE... non OOP

 per cui anche se vorresti una cosina carina comme OOP, 
 serve una SEMPLIFICAZIONE ESTREMA E VERSATIVE DEL COMMANDENGINE

 - se tocchi un parametro di un oggetto, OOP (pippo.setVisibility(True))
 - se colleghi elementi, e' un OOP
 - ma serovono i cicli, comandi MASSIVI non OOP...

 l'obiettivo e' di avere un MINILINGUAGGIO DI PROGRAMMAZIONE
 che SIMULI ESATTAMENTE cio che faresti in pratica con maya... NULLA DI PIU...

 ## eccezionalmente fai un 
      from cuteRig.core import *
    cosi da poter utilizzare dei semplici e rapidi:
      createJoint(pippo).setVisibility(False)
      massiveConnectAttribute(obj1, obj2, obj3)
    DGWrap("shit") --> serve a sto punto???
    DAGWrap("shit")

    ------------------------------------------------------------------------------------------------------
    - FAI UN TEST DI COSTRUZIONE, ikfk, stretch, creazione nodi ausiliari, attributi etc eccezionalmente
    e giudica come vorresti il linguagio per "RECORD MACRO"
    ------------------------------------------------------------------------------------------------------

    NON BUTTARTI SULLA OOP O SULLE CLASSI.
    e' l'uso che ne vuoi fare che deve REPLICARE IL PIU FACILMENTE E FEDELMENTE POSSIBILE l'operato MAYA

    E' la pratica maya che determina la sintassi e la semantica (ibrido oop e procedurale)

"""


createJoint(name="xxx", t=(), r=(), s=(), jo=())


joint1 = createJoint("peppino", ...)
joint2 = joint1.addJoint("fuffa", offsetT=(0, 10, 10))
joint3 = joint2.addJoint("sega", offsetT=(0, 10, 10))

createJoint("peppino", ...).addJoint("fuffa", offsetT=(0,0,0)).addJoint("shit", offsetT=(20, 20, 20))
["peppino", "fuffa", "shit"].setVisibility(False).setDrawStyle("None")

CR.parentConstraint()

object.incapsulate(nameCapsule="fuck")
fuck
  object


node.addAttr(longName="shit", shortName="bof", type="float", value=999, default=0, max=999, min=123)
node.deleteAttr("name")
node.connectPlug(sourcePlug, destinationPlug)
node.massiveConnectPlug(sourcePlug, destinationPlugs)

import cuteRig as CR
CR.connectPlug(sourcePlug, destinationPlug)
CR.massiveConnectPlug(sourcePlug, destinationPlugs)
CR.setParent(obj1, obj2, obj3, parent)
CR.incapsulate()
CR.setWorldT(obj1, obj2, ...)
CR.getWorldT(obj)


obj1.setParent("shit")
[obj1, obj2, obj3].setParent("fuck")
CR.setParent(obj1, obj2, obj3, parent)


obj1.incapsulate()
[obj1, obj].incapsulate(...)
CR.incapsulate??? harder

""" POSSIBLE VARIATIONS OF THE SAME SHIT """
STATIC -->CR.setWorldT(obj1, obj2, ...)
LIST   -->[obj1, obj2, ...].setWorldT()
LOCAL  -->obj1.setWorldT()


-> this is define abstractly for a dagNode and reimplemented differently for a transform and a joint
joint.incapsulate() # DIFFERENT THAN A TRANSFORM

object.incapsulate(suffixCapsule="suff")
object_suff
  object

for i in range(3):
    jointHandle = CR.createJoint("L_pippo" + str(i), t=(0,0,i*10), p=None)
    jointHandle.radius(12)
    jointHandle.preferredAngle(0,0,30)
    jointHandle.setVisibility(True)
    jointHandle.setDrawStyle("None")
    jointHandle.enableOverrides(True)
    jointHandle.displayType("reference")
    jointHandle.visibilityOverride(True)
    jointHandle.colorOverride(12)
    
    jointHandle.enableOverride(True).displayType(True).colorOverride(True)

    jointHandle.showLocalAxis(True)
    jointHandle.delete()

    jointHandle.setParent(None)
    jointHandle.unparent()

    fava = ["obj1", "obj2", "obj3", "obj4"] """ a DAGNode list """
    fava.setParent(parentObject)
    fava.setVisibility(True)

    [node1, node2].setVisibility(False)

    [x, y, z, w].

    jointHandle.setParent("xxx", respectOffset=False)

    jointHandle.localMoveTX(12)
    jointHandle.

    def getT      (self, space="world"):
    def getWorldT (self): #--> LIST? 3UPLE?
    def getLocalT (self):

    def setT      (self, value ,space="world",):
    should accept:
    node.setT(1, 2, 3) *args
    node.setT((1, 2, 3)) 3uple
    node.setT([2, 3, 4]) 3list
    
    def zeroT(self):
    def zeroR(self):
    def oneS (self):
    
    jointHandle.setT(0, 0, 0).setR(90, 0, 0)

    node1.matchWorldT(node2)
    node1.matchWorldR(node2)

    def setTRS(self, translation=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1), space="world"):
    def setTR (self, translation, rotation, space="world"):    
    def setT  (self, translation, space="world"):

    def setWorldTRS(self, translation, rotation, scale):
    def setWorldTR (self, translation, rotation):    
    def setWorldT  (self, translation):

    def setWorldT (self, value):
    def setLocalT (self, value):

    def getTX     (self, space="world"):
    def getWorldTX(self):
    def getLocalTX(self):

    def setTX     (self, space="world", tx=0):
    def setWorldTX(self, tx=0):
    def setLocalTX(self, tx=0):
    
    



    posX = jointHandle.getTX()
    
    posX = jointHandle.getWorldTX()
    posX = jointHandle.getLocalTX()
    posX = jointHandle.getTX(space=CR.localSpace)
    posX = jointHandle.getTX(space=CR.worldSpace)
    posX = jointHandle.getTX("local")
    
    pos  = jointHandle.getWorldT()
    pos  = jointHandle.getLocalT()    
    
    posX = jointHandle.getWorldTX()
    posX = jointHandle.getLocalTX()    posX = jointHandle.getWorldTX()
    posX = jointHandle.getLocalTX()    posX = jointHandle.getWorldTX()
    posX = jointHandle.getLocalTX()    
    rotY = jointHandle.getRY()
    
    
#########################################################################################################################################
#################################################################################################################################

    
    


def setLocalT(self, *args, **kwargs):
    """
    possible calls:
     MATCHING   
     - .setLocalT("pascal")
     VALUES        
     - .setLocalT(0, 1, 0)
     - .setLocal([1, 3, 0])
     - .setLocal((1, 2, 4))
     
    """
    if len(args) == 3:
        print "3 args"
    if len(args) == 1:
        if isinstance(args[0], list):
            print "list"
        elif isinstance(args[0], tuple):
            print "3ple"
        elif isinstance(args[0], str):
            print "target"
    
    # allows concatenation
    return self             

def getLocalT(self):
    """
    Returns a list! To make valid something like this:
    ((( FAI IL CONFRONTO ;) )))
        
    cubbo = Transform("porcoDio")
    trans = cubbo.getGlobalT()
    trans[1] += 10 
    sfera.setGlobalT(trans)
    
    trans = MC.xform("porcoDio", query=True, t=True, worldSpace=False)
    trans[1] += 10
    MC.xform(sfera, trans, edit=True, t=True, worldSpace=True)
    """
    
    translation = MC.xform(self, query=True, t=True, worldSpace=False)
    return list(translation) # Not sure here... I want a mutable (e.g. a list)    

    def matchWorldT(source, target):
    # a standard function

class DGNode(object):
    def __init__(self, name):
        pass
        
    def getAttr(self, ...):
        pass
        
    def createAttr(self, ...):
        pass
        
    def setAttr(self, ...):
        pass
        
    def lockAttr(self, attrList, **kwargs):
        # callable as:
        # obj.lockAttr("pippolo")
        # obj.lockAttr("attr1", "att2r", "attr3")
        # obj.lockAttr(attributeList)
        pass
                        
class AddDoubleLinear(DGNode):
    pass

class MultDoubleLinear(DGNode):    
    pass
    
class Reverse(DGNode):
    pass 

class DAGNode(DGNode):
    pass

class Transform(DAGNode):
    
    def __init__(self, name):
        DAGNode.__init__(self, name)
        pass
    
    def setLocalT(self, tx, ty, tz):
    def setLocalT(self, targetDAG):
    def setLocalT(self, [tx, ty, tz]):
    def setLocalT(self, ...)
    
    def setLocalTx(self, )            
    
    def getLocalT(self):
        translation = MC.xform(self, query=True, worldSpace=False)
        return translation
        
    def getWorldT(self):
        pass
            
    def getWorldR(self):
        pass
    def getWorldS(self):
        pass
        
    def getWorldTR(self):
        pass

    def getWorldTRS(self):             
        pass
        
    def getWorldR(self):
        pass
    def getWorldS(self):
        pass
    def getWorldTR(self):
        pass

    def getWorldTRS(self):             
        pass        
        
class Joint(Transform):
    pass    

class Locator(DAGNode):    
    pass
class Mesh(DAGNode):
    pass

class NurbsCurve(DAGNode):
    pass    
        