"""
import os as OS
import maya.cmds as MC
muPath = "F:\\MuWrapper\\4_agosto"
if muPath not in OS.sys.path:
    OS.sys.path.append(muPath)

import MuCore
reload(MuCore)
MU = MuCore
"""

import maya.cmds         as MC
import maya.OpenMaya     as OM
import maya.api.OpenMaya as OM2
import maya.OpenMayaUI   as OMUI

import PySide.QtCore     as QC
import PySide.QtGui      as QG
import shiboken

import time
import inspect

print
print "+-------------------+"
print "|      MU CORE      |"
print "+-------------------+"
print "      08/08/16"
print 


DEBUG = False
def printDebug(text):
    if DEBUG:
        print text







#======================================================================================================
# DECORATORS
#======================================================================================================
def functionDebug(func):
    def wrappedFunction(*args, **kwargs):
        stack = inspect.stack()
        depth = len(stack) - 2 # ??? The stackBase is <module> ???
        visualOffset = ' ' * depth * 2
        print visualOffset + 'F: {0} (C: {1}, D: {2})'.format(func.__name__, stack[1][3], depth)
        
        """
        if len(inspect.stack()) == 2: 
            # directly called from UI or direct call
            print("FUNCTION CALL: " + inspect.stack()[1][3] + "\n[caller: UI]") 
        else:
            # INSPECT.stack() is a list, the function frames... [0]=actual, [1]=previous(i.e. orig func), [2]=caller of previous...
            print("FUNCTION CALL: " + inspect.stack()[1][3] + "\n[caller: " + inspect.stack()[2][3] + "]") 
        """
        #--------------------------
        # Pre function call
        #--------------------------
        try:
            print visualOffset + 'A:', args
        except:
            # If you call this shit before the base class __repr__ has been built
            print visualOffset + 'A: __repr__ not defined!' 

        try:       
            print visualOffset + 'K:', kwargs
        except:
            print visualOffset + 'K: __repr__ not defined!'

        # Now call it!
        result = func(*args, **kwargs)

        #--------------------------
        # Post function call
        #--------------------------
        #print visualOffset + "R:", result

        # Return result
        return result

    return wrappedFunction    
    
    """
    @functionDebug
    def justFuckYou(*args, **kwargs):
        ....

    It shows the args, kwargs, caller, etc etc    
    """









#======================================================================================================
# CONTEXT MANAGERS
#======================================================================================================
class DefaultViewport(object):
    def __enter__(self):
        # A "viewport" is a panel of type "modelPanel"
        modelPanels = MC.getPanel(type="modelPanel")
        self.oldViewportsConfiguration = {}
        for panel in modelPanels:
            # Save user viewport rendering preferences
            self.oldViewportsConfiguration[panel] = MC.modelEditor(panel, query=True, rendererName=True)
            MC.modelEditor(panel, edit=True, rendererName="base_OpenGL_Renderer")
    def __exit__(self, *args):
        for panel in self.oldViewportsConfiguration:
            MC.modelEditor(panel, edit=True, rendererName= self.oldViewportsConfiguration[panel])


class DefaultRenderLayerActive(object):
    def __enter__(self):
        self.originalLayer = MC.editRenderLayerGlobals(query=True, currentRenderLayer=True)
        MC.editRenderLayerGlobals(currentRenderLayer="defaultRenderLayer") 
    def __exit__(self, *args):
        MC.editRenderLayerGlobals(currentRenderLayer=self.originalLayer) 


class RenderLayerActive(object):
    """
    with MU.RenderLayerActive('layerName') as layer:
        # Here [layer] is the <RenderLayer> object, in case you need it!
    """

    def __init__(self, renderLayerName):
        self.originalRenderLayer = MC.editRenderLayerGlobals(query=True, currentRenderLayer=True)
        self.renderLayerToActivate = renderLayerName
        
    def __enter__(self):
        MC.editRenderLayerGlobals(currentRenderLayer=self.renderLayerToActivate)
        return MuNode(self.renderLayerToActivate)
        
    def __exit__(self, *args):
        MC.editRenderLayerGlobals(currentRenderLayer=self.originalRenderLayer) 


class Timer(object):
    def __enter__(self):
        self.startTime = time.clock()
    def __exit__(self, *args):
        print "-"*80
        print "Elapsed time:", time.clock() - self.startTime
        print "-"*80
        print  


class Profiler(object):
    """ A context for cProfile """
    pass









#======================================================================================================
# CUSTOM EXCEPTIONS
#======================================================================================================
class Fatality(Exception):
    def __init__(self, tag, mess):
        self.mess = mess       
        print "" 
        print "-"*80
        print "FATALITY [" + tag + "]"
        print mess
        print "-"*80
    def __str__(self):
        return self.mess


class AttributeFatality(Fatality):
    def __init__(self, attrName):
        tag = "attribute error"
        mess = "you just did shit \"" + attrName + "\" die!"        
        super(AttributeFatality, self).__init__(tag, mess)
            

class NameFatality(Fatality):
    def __init__(self, nodeName):
        tag = "name error"
        mess = "There's no DGNode named \"" + nodeName + "\" (or it's DAG-ambiguous)!"        
        super(NameFatality, self).__init__(tag, mess)
        









#======================================================================================================
# NODE METADATA
#======================================================================================================     
class Metadata(object):
    """
    obj = MU.MuNode("XXX")
    print obj.metadata.getValue("wow1")
    print obj.metadata.getValue("boolean2")
    print obj.metadata.getValue("testo2")
    print obj.metadata.getValue("enum2")

    #obj.createMetaAttr("META_listone", t="double", m=True, dv=999.999)
    #obj.createMetaAttr("META_testo2", t="string", dv="fuckYou")
    #obj.createMetaAttr("META_enum6", t="enum", dv="muori", enumName=["fava", "cazzo", "muori"])


    # AS A RULE, if a <metAttr> string rappresenta una list o un dict, 
    # deve essere gestita via JSON... 
    # ABSOLUTELY NO MANUAL PARSING (json does that for you)
    import json as JSON
    # ENCODING an object
    obj = [...]
    objEncoded = JSON.dumps(obj) # No indent implies separators=(", ", ": ")

    # DECODING a string
    try:
        result = JSON.loads(stringToDecode)
    except ValueError:
        print "[FATALITY] UNABLE TO DECODE THE STRING: ", stringToDecode 
        raise
    """

    """
    attrs = MC.listAttr(obj.name, userDefined=True, string="*")
    attrDict = {}
    for attr in attrs:
        try:
            tipo = MC.getAttr(obj.name + "." + attr, type=True)
            num = MC.attributeQuery(attr, n=obj.name, numberOfChildren=True)
            multi = MC.attributeQuery(attr, n=obj.name, multi=True)
        except:
            tipo = "FAILED"
            num = "X"
            multi = "X"
        if tipo not in attrDict:
               attrDict[tipo] = []
        attrDict[tipo].append((attr, num, multi))        

    for t in sorted(attrDict):
        print t
        for a in attrDict[t]:
            print "  ", a
    """

    """
    In the end it's just a collection of methods which point
    to the original node via an MObject pointer
    
    We get a nice sintax:
      obj = Wrapper(nodeName)  
      obj.metadata.exists     (metaAttrName)
      obj.metadata.setValue   (metaAttrName, value)
      obj.metadata.getValue   (metaAttrName)
      obj.metadata.getDictionary ()
      obj.metadata.delete     (metaAttrName)
      obj.metadata.create     (metaAttrName, attrType, ...)
      obj.metadata.deleteAll  ()        
        
    """
    _supportedTypes = ["bool", 
                       "double", 
                       "string",
                       "message",
                       "enum"]
                       
    def __init__(self, mObj):
        # The only real link with the Maya node is the pointer mObj
        # passed to this initializer!
        #
        # DON'T wrap it with a stupid decorator
        # Wanna the nodeName? Use:
        #
        # self._pointer.name()
        
        # Pointer to the original Maya node
        self._pointer = OM.MFnDependencyNode(mObj)

    def create(self, attrName, **kwargs):
        """ 
        RULES:
         - every metaAttribute has a "META_" prefix...
           but it has to be trasparent for the user (me:))
           we could have:
            - "megashit" standard attribute
            - "megashit" metaAttribute (internally "META_megashit")
        """
            
        attrName = "META_" + attrName
        attrType  = kwargs.get("type",  kwargs.get("t", None))
        multiFlag = kwargs.get("multi", kwargs.get("m", False))
        
        if attrType is None:
            raise AttributeFatality("flag 'type' (t) is mandatory!")                               
        
        # Just once please (don't trigger API methods for nothing)
        # Here we don't modify the DAG, hence we can revert to the commandEngine
        nodeName = self._pointer.name() 
        
        if attrType not in Metadata._supportedTypes:
            raise AttributeFatality("The attribute type <" + attrType + "> is unknown!")                               
        
        # Check if already exists
        if MC.attributeQuery(attrName, node=nodeName, exists=True):
            raise AttributeFatality("MayaNode " + nodeName + " has already a <metaAttribute> named " + attrName)  
        
        # Creation
        if attrType == "double":
            defaultValue = kwargs.get("defaultValue", kwargs.get("dv", 0.0))
            MC.addAttr(nodeName, longName=attrName, attributeType="double",
                defaultValue=defaultValue, multi=multiFlag, keyable=False)
            print "created!"
        
        elif attrType == "string":
            # 'defaultValue' is meaningful only for numerics; just initialize 
            initValue = kwargs.get("defaultValue", kwargs.get("dv", ""))
            MC.addAttr(nodeName, longName=attrName, dataType="string", 
            multi=multiFlag, keyable=False)        
            MC.setAttr(nodeName + "." + attrName, initValue, type="string")
            print "created!"
            
        elif attrType == "bool":
            # 'defaultValue' is meaningful only for numerics; just initialize 
            initValue = kwargs.get("defaultValue", kwargs.get("dv", False))
            MC.addAttr(nodeName, longName=attrName, attributeType="bool", 
            multi=multiFlag, keyable=False)        
            MC.setAttr(nodeName + "." + attrName, initValue)
            print "created!"    
        
        elif attrType == "enum":
            enumArg = kwargs.get("enumName", kwargs.get("en", None))
            enumName = ""
            for i, name in enumerate(enumArg):
                enumName += name + "=" + str(i) + ":"
            
            enumName = enumName.rstrip(":")
            print enumName
            MC.addAttr(nodeName, longName=attrName, attributeType="enum", 
            multi=multiFlag, keyable=False, enumName=enumName)                 

            initValue = kwargs.get("defaultValue", kwargs.get("dv", None))
            try:
                numericInitValue = enumArg.index(initValue)
            except:
                MC.error("the default value for the enum is unknown")
                    
            if initValue:
                MC.setAttr(nodeName + "." + attrName, numericInitValue)
        
    def getValue(self, attrName):
        """
        Again: a metaAttr named "grossaFava" is represented internally by "META_grossaFava"
        """
        attrName = "META_" + attrName
        nodeName = self._pointer.name()
        plug = nodeName + "." + attrName
        attrType = MC.getAttr(plug, type=True)
        
        # Skip if "multi"
        if MC.attributeQuery(attrName, node=nodeName, multi=True):
            MC.error(".getValue not implemented for Multi")
            
        if attrType in ["double", "bool", "string"]:
            return MC.getAttr(plug)
        
        elif attrType == "enum":
            return MC.getAttr(plug, asString=True)
      
    def getDictionary(self):
        # Get the string name.
        # Here it's quite unlikely to change the DAG, so we shouldn't
        # have any problem by regressing to a string
        nodeName = self._pointer.name()
        
        metaAttrs = MC.listAttr(nodeName, userDefined=True, string="META_*") or []
        result = {}
        for attr in metaAttrs:
            plug = nodeName + "." + attr
            # Attribute type (string)
            attrType = MC.getAttr(plug, type=True)
            
            # Is it <multi> (type == "TdataCompound")
            isMulti = MC.attributeQuery(attr, node=nodeName, multi=True)
            
            # Is it <compound>? ("TdataCompound" is NOT...)
            #isCompound = MC.attributeQuery(attr, node=self.name, numberOfChildren=True)
            
            if not isMulti:
                if attrType == "enum":
                    attrValue = MC.getAttr(plug, asString=True)
                else: 
                    attrValue = MC.getAttr(plug)
            else:
                logicalIndices = MC.getAttr(plug, multiIndices=True) or []
                attrValue = {}
                for i in logicalIndices:
                    attrValue[i] = MC.getAttr(plug + "[" + str(i) + "]")
                
                
            result[attr] = (attrType, attrValue)
        return (result if len(result) > 0 else None)
    """
    obj = MU.MuNode("XXX")
    print obj.metadata.getValue("wow1")
    print obj.metadata.getValue("boolean2")
    print obj.metadata.getValue("testo2")
    print obj.metadata.getValue("enum2")

    #obj.createMetaAttr("META_listone", t="double", m=True, dv=999.999)
    #obj.createMetaAttr("META_testo2", t="string", dv="fuckYou")
    #obj.createMetaAttr("META_enum6", t="enum", dv="muori", enumName=["fava", "cazzo", "muori"])


    # AS A RULE, if a <metAttr> string rappresenta una list o un dict, 
    # deve essere gestita via JSON... 
    # ABSOLUTELY NO MANUAL PARSING (json does that for you)
    import json as JSON
    # ENCODING an object
    obj = [...]
    objEncoded = JSON.dumps(obj) # No indent implies separators=(", ", ": ")

    # DECODING a string
    try:
        result = JSON.loads(stringToDecode)
    except ValueError:
        print "[FATALITY] UNABLE TO DECODE THE STRING: ", stringToDecode 
        raise
    """

    """
    attrs = MC.listAttr(obj.name, userDefined=True, string="*")
    attrDict = {}
    for attr in attrs:
        try:
            tipo = MC.getAttr(obj.name + "." + attr, type=True)
            num = MC.attributeQuery(attr, n=obj.name, numberOfChildren=True)
            multi = MC.attributeQuery(attr, n=obj.name, multi=True)
        except:
            tipo = "FAILED"
            num = "X"
            multi = "X"
        if tipo not in attrDict:
               attrDict[tipo] = []
        attrDict[tipo].append((attr, num, multi))        

    for t in sorted(attrDict):
        print t
        for a in attrDict[t]:
            print "  ", a
    """










#======================================================================================================
# HELPERS
#======================================================================================================  
def typeString(object):
    """
    From <class 'MuCore.RenderLayer'> to "MuCore.RenderLayer" 
    """
    return str(type(object)).split("'")[1]


def showHierarchy(module):
    """
    Non riesco a passargli l'oggetto modulo "se stesso"...
    cioe': MU.showHierarchy(MU)
    """
    hierarchy = {}
    for elementName in dir(module):
        element = getattr(module, elementName)
        if typeString(element) == "type":
            mro = [cls.__name__ for cls in element.mro()][::-1]
            position = hierarchy
            for cls in mro:
                if cls not in position:
                    position[cls] = {}
                position = position[cls]    
            
    def traverseDict(actualDict, depth=0):
        visualOffset = "  " * depth
        for item in sorted(actualDict):
            print visualOffset + str(item)
            if len(actualDict[item]) > 0:
                traverseDict(actualDict[item], depth + 1)
            
    traverseDict(hierarchy)







#======================================================================================================
# COMMAND ENGINE WRAPPERS
#======================================================================================================
#
# - MU.ls(...) --> <Bundle>
#
#------------------------------------------------------------------------------------------------------
def ls(*args, **kwargs):
    # ls returns [] for "nothing"
    stringResult = MC.ls(*args, **kwargs)
    return Bundle(*stringResult)










#======================================================================================================
# SCENE METHODS
#======================================================================================================  
class Scene(object):
    @staticmethod
    def getSets():
        # listSets(allSets=True) is SEVERELY broken:
        #  - 2 parasites (unselectionable fake sets) comes out
        #  - the namespace info is LOST... seriously
        
        sets = MC.ls(type="objectSet") 
        # or MC.ls(sets=True), same thing
        
        return Bundle(*sets)


    @staticmethod    
    def getWorldChildren():
        worldChildren = []

        # Initialized to a fake "world" (not a kTransform)
        DAGIter = OM.MItDag(OM.MItDag.kBreadthFirst) 

        selList = OM.MSelectionList()
        fn = OM.MFnTransform()
        
        while True:
            DAGIter.next() # Skip the first one (a "fakeWorld")
            nodePtr = DAGIter.currentItem()
            if DAGIter.depth() == 1:
                if nodePtr.apiType() == OM.MFn.kTransform:
                    fn.setObject(nodePtr)
                    nodeName = fn.fullPathName()
                    if MC.objExists(nodeName):
                        # To avoid "weird" transforms like "|groundPlane_transform"
                        # which exist, but invisible to MEL
                        worldChildren.append(nodeName)
            else:
                break
        return Bundle(*worldChildren)


    @staticmethod
    def getIsolatedNodes(**kwargs):
        type_value = kwargs.get("type", kwargs.get("t", None))
        # Check for "isolated" (nodes without connections) of a spefic type
        if type:
            candidates = MC.ls(exactType=type_value) or []
        else:
            candidates = MC.ls() or []
        
        isolatedNodes = []

        for nodeName in candidates:
            connections = MC.listConnections(nodeName, source=True, destination=True) or []
            if len(connections) == 0:
                # Orphan found!
                isolatedNodes.append(Wrapper(nodeName))
        
        return isolatedNodes                








"""========================================================================
RULES:
 - if a "complex property" can be "called" without arguments, 
   set it to @property:
   ex:
    - xxx.nodeName, xxx.shortName, xxx.type, xxx.longName, xxx.namespace

Structure of each class:
    STATIC METHODS (@SORTED)
    CLASS METHODS  (@SORTED)
    CONSTRUCTOR/INITIALIZER
        __new__
        __init__
    MAGIC METHODS  (@SORTED)
        __cockMagic__
        __fuckMagic__
        __shitMagic__
    METHODS        (@SORTED)
        alphaWow()
        betaWow()
        hugeShit()
        pleaseDie()
========================================================================"""


"""=================================================================================================
NOTES:
Ragiona in questi termini:
 - fai le cose protette e incapsulate, ad alto livello
 - nei punti critici, puoi "compilare" la parte astratta in "commandEngine"
   un po come del codice Python con parti compilate in C

   MuCore --> commandEngine
   Python --> C

#-------------------------------------------------------------------------------------------









============================================================================================================
============================================================================================================
     _     _ _     _                                      
    | |   (_) |   | |                                     
 ___| |__  _| |_  | |__   __ _ _ __  _ __   ___ _ __  ___ 
/ __| '_ \| | __| | '_ \ / _` | '_ \| '_ \ / _ \ '_ \/ __|
\__ \ | | | | |_  | | | | (_| | |_) | |_) |  __/ | | \__ \
|___/_| |_|_|\__| |_| |_|\__,_| .__/| .__/ \___|_| |_|___/
                              | |   | |                   
                              |_|   |_|                   

------------------------------------------------------------------------------------------------------------
ISSUES:

 - objExists e' chiamato una volta da __new__ di MuNode... poi una seconda volta da 
   DGNode __init__... MINIMIZZA

 - PyMel usa MObjectHandle invece di MObject... fai un tentativo

 ? apparentemente, l'API 2.0 e davvero piu rapida... fai un tes e  vedi se c'e tutto cio che serve!  

 - il __new__ di MuNode e' orriderrimo... non si puo semplificare?

 - prt il momento non funziona con le "instances"... perche si concentra sul nodo e quando e condiviso
   fallisce. semplicemente per le instances salva anche il DAGPath

 - il decorator [functionDebug] da dei problemi negli __init__, __new__ e __repr__
   In teoria, quando attivi il flaggone DEBUG, dovrebbe applicare automaticamente il 
   decorator a tutti i metodi rilevanti, senza obbligarti a farlo manualmente 

   Inoltre, la wrappedFunction introduce un caller in piu alle volte si alle volte no e non so come calcolare
   l'offset visuale del depth... fuck you so deep...
============================================================================================================
============================================================================================================
"""







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
#======================================================================================================
# MINI FACTORY
#======================================================================================================  
class MuNode(object):
    #-----------------------------
    # CONSTRUCTOR
    #-----------------------------   
    def __new__(cls, nodeName):
        #printDebug("MuNode __new__")
        if MC.objExists(nodeName):
            mayaType = MC.nodeType(nodeName)

            # Start with specialized node and increase in generality: 
            # Specific implemented DGNodes:
            # - transform
            # - joint
            # - mesh 
            # - objectSet
            # - renderLayer

            if mayaType == "transform":
                return Transform(nodeName)
            elif mayaType == "joint":
                return Joint(nodeName)    
            elif mayaType == "mesh":
                return Mesh(nodeName)
            elif mayaType == "objectSet":
                return ObjectSet(nodeName)
            elif mayaType == "renderLayer":
                return RenderLayer(nodeName)

            elif MC.objectType(nodeName, isAType="shape"):
                # Is it a generic "shape"?
                return DAGNode(nodeName)    
            else:
                # Generic DGNode
                return DGNode(nodeName)
        else:
            raise NameFatality(nodeName)              




class DGNode(object):
    """""""""""""""""""""""""""""""""""""""
    INTERNAL  
      self._pointer.name()
      self._pointer.fullPathName()
      self._pointer.partialPathName()
      ... pretty heavy

    EXTERNAL 
      obj.nodeName  (the name of the node, without DAG prefixes)
      obj.shortName (the minimal DAG path)
      obj.longName  (the full, heavy dagpath)       
    
    ==> CHECK FOR PERFORMANCE PENALTIES
    ==> probably using EXTERNALS makes things easier...
    
    --> for the moment, use EXTERNALS
    --> then Profile and if slow, use internals
    """"""""""""""""""""""""""""""""""""""" 

    #-----------------------------
    # STATIC/CLASS METHODS
    #-----------------------------
    @classmethod    
    def create(cls, *args, **kwargs):
        # It's a classMethod... cls holds the class caller:
        # ex: customize: 
        #  DGNode.create(name, type)
        #  Transform.create(name, parent)
        #  Mesh.create(name, parent)...
        if cls == DGNode:
            # Creates a generic DGNode... we need name and type
            if len(args) == 2:
                nodeType = args[1]
                nodeName = args[0]
            else:
                MC.error("BAD ARGUMENTS")

        if cls == Transform:
            if len(args) == 1:
                nodeType = "transform"
                nodeName = args[0]
            else:
                MC.error("BAD ARGUMENTS")

        parent_kwarg = kwargs.get("parent",  kwargs.get("p", None))
        if parent_kwarg:
            name = MC.createNode(nodeType, n=nodeName, p=parent_kwarg, skipSelect=True)
        else:
            name = MC.createNode(nodeType, n=nodeName, skipSelect=True)    

        return MuNode(name)




    #-----------------------------
    # INITIALIZER
    #-----------------------------
    def __init__(self, nodeName):
        printDebug("[DGNode] __init__ " + nodeName)
        selList = OM.MSelectionList()
        try:
            # The API method .add fails if node doesn't exist or there's 
            # a DAG ambiguity, but MC.objExists doesn't in case of ambiguity!!!
            selList.add(nodeName)     
        except:    
            raise NameFatality(nodeName)  
        
        """
        Note:
        This is not gonna work with instances. If you save only the pointer, you'll have just a node.
        But since it's shared, all DAG methods (getParent, getChildren) will fail.

        To work with instances, you need to save the DAGPath (of course...)
        """

        mObj = OM.MObject()
        selList.getDependNode(0, mObj)
        
        apiTypeStr = mObj.apiTypeStr() 
        if apiTypeStr == "kMesh":
            # Mesh node
            self._pointer = OM.MFnMesh(mObj)
        elif apiTypeStr == "kTransform":
            # Transform node
            self._pointer = OM.MFnTransform(mObj)

        elif mObj.hasFn(OM.MFn.kDagNode):
            # Generic DAGNode (ex: shape)
            self._pointer = OM.MFnDagNode(mObj)
        else:
            # Generic Dependency node    
            self._pointer = OM.MFnDependencyNode(mObj)

        self.metadata = Metadata(mObj) # Just pass the pointer




    #-----------------------------
    # MAGIC METHODS
    #-----------------------------
    def __repr__(self):
        # Generic reps for DGNodes; override it for DAGS to show shortName
        return "\"" + self._pointer.name() + "\"<" + self.type + ">"      




    #-----------------------------
    # METHODS
    #-----------------------------
    def breakConnection(self):
        pass


    def connectPlug(self, sourcePlug, destinationPlug):
        pass


    def getAttr(self, attrName): 
        return MC.getAttr("{0}.{1}".format(self.longName, attrName))
        #return MC.getAttr(self.longName + "." + attrName)
    

    def getInputPlugs(self, attrName, **kwargs):
        """
                <DGNode>.getInputPlugs(attrName [, type=<String>,
                                           nodeOnly=<Boolean>, 
                                           skipConversionNodes=<Boolean>] )
        return: <String>|<List of Strings>|None
        (String for a simple attribute, List for an Array attribute)                                   
        """        
        # To do:
        # - multiple types? Probably not needed
        # - check [exactType] flag (for inheriting types, like animCurve) and [shapes] flag 
        
        typeArg                  = kwargs.get("type",                kwargs.get("t",   ""))
        skipConversionNodes_flag = kwargs.get("skipConversionNodes", kwargs.get("scn", False))
        nodeOnly_flag            = kwargs.get("nodeOnly",            kwargs.get("no",  False))
        exactType_flag           = kwargs.get("exactType",           kwargs.get("et",  False))
        
        plugs = MC.listConnections(self.name + "." + attrName, 
            source=True, destination=False, 
            plugs=not nodeOnly_flag, type=typeArg, exactType=exactType_flag, 
            skipConversionNodes=skipConversionNodes_flag)
            
        if plugs is not None:
            if len(plugs) == 1:
                # Simple attribute
                return plugs[0]
            else:
                # Array type
                return plugs    
        else:
            return None   


    def getOutputPlugs(self, attrName, **kwargs):
        pass


    @property
    def isReferenced(self):
        return MC.referenceQuery(self.shortName, isNodeReferenced=True)
    

    @property
    def isReferencedFromFile(self):
        """
        If the node is referenced, returns the source filename.
        Otherwise ""
        """
        if MC.referenceQuery(self.shortName, isNodeReferenced=True):
            return MC.referenceQuery(self.shortName, filename=True)
        else:
            return ""    


    @property
    def longName(self): 
        # To allow loop on generic nodes and DAGs
        return self._pointer.name()


    @property
    def namespace(self):
        return self._pointer.parentNamespace()


    @property
    def nodeName(self): 
        return self._pointer.name()


    def rename(self, newNodeName):
        """
        NOTE:
         - to work with a node with the commandEngine you need the SHORTNAME;
         - but when you assign to it a new name, it has to be the NODENAME!
        It's up to Maya to add or remove the partial DAGPath, not to you!!!  
        """
        # Use the .longName() to allow working on DAGs too!
        # Returns the "true" new name in case of DAG autoResolution of ambiguities
        realNewName = MC.rename(self.longName, newNodeName)
        return realNewName


    def setAttr(self, attrName, newValue):
        # Allow "fluid style" (concatenation)
        if isinstance(newValue, str):
            # It's a string attribute
            MC.setAttr(self.nodeName + "." + attrName, newValue, type="string")
        else:
            MC.setAttr(self.nodeName + "." + attrName, newValue)
            
        # Promote concatenation
        return self    


    @property
    def shortName(self): 
        # To allow loop on generic nodes and DAGs
        return self._pointer.name()


    @property
    def type(self):
        # This is MEL type, not API type
        return self._pointer.typeName()



           
class DAGNode(DGNode):
    #-----------------------------
    # INITIALIZER
    #-----------------------------       
    def __init__(self, nodeName):
        printDebug("[DAGNode] __init__ " + nodeName)
        super(DAGNode, self).__init__(nodeName)
        



    #-----------------------------
    # MAGIC METHODS
    #-----------------------------
    def __repr__(self):
        # For DAGs, we want the minimalistic path
        return "\"" + self._pointer.partialPathName() + "\"<" + self.type + ">"      



    #-----------------------------
    # METHODS
    #-----------------------------
    def getParent(self):
        """
        It requires the shortName and in case of instances it works (it fails indirectly
        because I need to save the DAGPath not only the pointer for DAGs)

        """
        parentList = MC.listRelatives(self._pointer.partialPathName(), parent=True, fullPath=True)
        if parentList is not None:
            return MuNode(parentList[0])
        else:
            return None    


    def isInstanced(self, indirect=False):
        # Apparently, this every DAGNode can be instanciated... (?)
        return self._pointer.isInstanced(indirect)


    @property
    def longName(self): 
        return self._pointer.fullPathName()
        

    @property
    def shortName(self): 
        return self._pointer.partialPathName()




class Mesh(DAGNode):
    #-----------------------------
    # INITIALIZER
    #-----------------------------
    def __init__(self, nodeName):
        printDebug("[Mesh] __init__ " + nodeName)
        super(Mesh, self).__init__(nodeName)



    #-----------------------------
    # METHODS
    #-----------------------------
    def getShader(self, **kwargs):  
        pass
        """  
        renderLayer_flag = kwargs.get("renderLayer", kwargs.get("rl", "defaultRenderLayer"))
        
        if self.isInstanced():
           MC.error("[FATAL] Instanced, not implemented!")
        """


    def getShadingEngine(self, **kwargs):
        pass
        """
        renderLayer_flag = kwargs.get("renderLayer", kwargs.get("rl", "defaultRenderLayer"))
        
        if self.isInstanced():
           MC.error("[FATAL] Instanced, not implemented!")
        """




class Transform(DAGNode):
    """=========================================================="""
    """ Only a <transform> (and its derived) can have "children" """
    """=========================================================="""      

    #-----------------------------
    # INITIALIZER
    #-----------------------------  
    def __init__(self, nodeName):
        printDebug("[transform] __init__ " + nodeName)
        super(Transform, self).__init__(nodeName)


 
    #-----------------------------
    # METHODS
    #-----------------------------
    def getChildren(self, **kwargs):
        type_flag = kwargs.get("type", kwargs.get("t", None))

        nodeName = self._pointer.fullPathName()
        if not type_flag:
            children = MC.listRelatives(nodeName, children=True, path=True) or []
        else:
            children = MC.listRelatives(nodeName, children=True, type=type_flag, path=True) or []

        return Bundle(*children)


    def getMesh(self, **kwargs):
        """
        If nothing is found, returns None!
        If multiple meshes are present, it doesn't give a fuck: you get the first one!
        """
        kwargs["noIntermediate"] = True
        meshChildren = self.getMeshes(**kwargs)
        meshChild = None
        try:
            meshChild = meshChildren[0]
        except IndexError:
            pass
            
        return meshChild     


    def getMeshes(self, **kwargs):
        """
        If nothing is found, returns []
        (to allow void loops, e.g. for x in node.getMeshes():...)
        """
        noIntermediate_flag = kwargs.get("noIntermediate", kwargs.get("ni", True))
        
        # Probably useless... we return a list of Wrappers
        #fullName_flag       = kwargs.get("fullName",       kwargs.get("fn", False))

        nodeName = self._pointer.fullPathName()
        
        # The "path=True" force the returned names to be minimalistic (i.e. shortName)
        meshChildren = MC.listRelatives(nodeName, children=True, type="mesh", path=True) or []
                                                                               
        if noIntermediate_flag:
            meshChildren = [x for x in meshChildren if MC.getAttr(x + ".intermediateObject") == 0]
        
        return Bundle(*meshChildren)
        



class Joint(Transform):
    def __init__(self, nodeName):
        printDebug("[joint] __init__ " + nodeName)
        super(Joint, self).__init__(nodeName)



  
class ObjectSet(DGNode):
    """
    ===> PER IL MOMENTO FUNZIONA SOLO CON OGGETTI, NON COMPONENTI
    """


    """ DOC
      Note: the class <MFnSet> is almost like the corr. commandEngine 
    
      Probably one of the worst command syntax ever seen!!! ABOMINABLE)  
      sets(NODE, isMember=SET)
      sets(NODE, remove=SET)
      sets(NODE, addElement=SET)
      sets(NODE, forceElement=SET)
      sets(SET, size=True)
      sets(SET, query=True)
      sets(clear=SET)
      ... Seriously, WHAT THE FUCK?
    
      """

    #-----------------------------
    # STATIC/CLASS METHODS
    #-----------------------------
    @staticmethod
    def create(nodeName, initialMembers=[]):
        # HERE IT'S BETTERO TO CALL .sets to build it
        tempName = MC.createNode("objectSet", name=nodeName, skipSelect=True)
        unionSet = ObjectSet(tempName)
        unionSet.add(initialMembers)
        return unionSet
    

    @staticmethod
    def union(setA, setB):
        setA_name = setA._pointer.name()
        setB_name = setB._pointer.name()
        union_string = MC.sets(setA_name, union=setB_name)
        
        unionSet = ObjectSet.create(setA_name + "_" + setB_name + "_union", union_string)
        return unionSet


    #-----------------------------
    # INITIALIZER
    #-----------------------------
    def __init__(self, nodeName):
        printDebug("[objectSet] __init__ " + nodeName)
        super(ObjectSet, self).__init__(nodeName)


    #-----------------------------
    # MAGIC METHODS
    #-----------------------------    
    def __repr__(self):
        #
        return "\"" + self.nodeName + "\"<ObjectSet>"        
    

    #-----------------------------
    # METHODS
    #-----------------------------
    def add(self, other, **kwargs):
        # WHat happens if "other"is already there?
        # mySet.add(<DGNode>)
        # mySet.add(<str>)
        # mySet.add(<list of DGNode or str>)
        
        setName = self._pointer.name()
        force_flag = kwargs.get("force", kwargs.get("f", True))
        
        # issubclass(MyClass, MyClass) == True
        nodeToAdd_name = None
        
        if issubclass(type(other), Wrapper):
            nodeToAdd_name = other.shortName
        elif isinstance(other, str):
            nodeToAdd_name = other
        elif isinstance(other, list):
            # The horrid .sets accepts even a list of <str>
            nodeToAdd_name = []
            for x in other:
                try:
                    nodeToAdd_name.append(x.nodeName)
                except:
                    nodeToAdd_name.append(x)
                    
        if force_flag:
            MC.sets(nodeToAdd_name, forceElement=setName)
        else:    
            MC.sets(nodeToAdd_name, addElement=setName)
            
        return self    
    

    def clear(self):
        setName = self._pointer.name()
        MC.sets(clear=setName) # Another wonderful syntactic abomination
        return self


    def getMembers(self):
        setName = self._pointer.name()
        # Another wonderful syntactic abomination
        # But luckily, it returns shortNames and namespaces
        memberNames = MC.sets(setName, query=True) or [] 
        return [Wrapper(x) for x in memberNames]
    

    def _getMemberNames(self):
        setName = self._pointer.name()
        return MC.sets(setName, query=True) or [] 
       

    def has(self, other):
        setName = self._pointer.name()
        other_name = None        
        if issubclass(type(other), Wrapper):
            other_name = other.shortName
        if isinstance(other, str):
            other_name = other    
        return MC.sets(other_name, isMember=setName)
               



class RenderLayer(DGNode):
    #-----------------------------
    # INITIALIZER
    #-----------------------------       
    def __init__(self, nodeName):
        printDebug('[RenderLayer] __init__ {0}'.format(nodeName))
        super(RenderLayer, self).__init__(nodeName)




    #-----------------------------
    # METHODS
    #-----------------------------
    def getConnectionOverrides(self):
        print "fuckYou"

    def makeActive(self):
        try:
            MC.editRenderLayerGlobals(currentRenderLayer=self.nodeName, useCurrent=True, enableAutoAdjustments=True)
        except Exception as exc:
            # This could happen when the layer is badly referenced!!! check it out better!
            MC.error('FAILED TO SELECT LAYER {0}... {1}!'.format(self.nodeName, exc))
    



class Bundle(object):
    """
    The class that allows "massive" methods, ex:
    Bundle("xxx", "yyy", "zzz", "www").lockAttr("tx", "ty", tz")\
                                      .visibility(False)\
                                      .setParent("pippo")

    un for x in bundleObj: prende __len__ e fa un __getitem__... 
    ma allo stato attuale non e' un iterabile in senso proprio
    """

    #-----------------------------
    # INITIALIZER
    #-----------------------------    
    def __init__(self, *args):
        self._list = [MuNode(x) for x in args]
    



    #-----------------------------
    # MAGIC METHODS
    #-----------------------------    
    def __getitem__(self, index): 
        try:
            return self._list[index]
        except:
            # This is pointless
            raise    


    def __len__(self):
        return len(self._list)


    def __repr__(self):
        if len(self) == 0:
            result = "[]"
        else:
            result = "["
            for i in range(len(self)):
                result += repr(self._list[i]) + ("\n " if i < len(self) -1 else "]")
              
        return result


    def __setitem__(self, index, node):
        if isinstance(node, basestring):
            self._list[index] = MuNode(node)
        else:
            self._list[index] = node




    #-----------------------------
    # METHODS
    #-----------------------------
    def append(self, node):
        if isinstance(node, basestring):
            self._list.append(MuNode(node))
        else:
            self._list.append(node)




# Not implemented yet... probably a derived of "renderPass"??? 'cause it's not exactly a type of node...
class Occlusion(object):
    #-----------------------------
    # INITIALIZER
    #-----------------------------    
    def __init__(self, nodeName, **kwargs):
        selList = OM2.MSelectionList()
        try:
            selList.add(nodeName)
        except:
            MC.error("[FATAL] Can't found node!")
        mObj = selList.getDependNode(0)
        self._pointer = OM2.MFnDependencyNode(mObj)
        
        # The initializer accept all the attributes of the node
        for arg in kwargs:
            # Check if the object has the attribute. Otherwise, it's gonna
            # create a NEW attribute
            if hasattr(self, arg):
                setattr(self, arg, kwargs[arg])
            else:
                MC.error("Object has no attribute:", arg)   



    #-----------------------------
    # METHODS
    #-----------------------------  
    @property
    def samples(self):
        return MC.getAttr(self._pointer.name() + ".samples")


    @samples.setter
    def samples(self, numSamples):
        MC.setAttr(self._pointer.name() + ".samples", numSamples)


    @property
    def spread(self):
        return MC.getAttr(self._pointer.name() + ".spread")


    @spread.setter
    def spread(self, spreadValue):
        MC.setAttr(self._pointer.name() + ".spread", spreadValue)


    @property
    def maxDistance(self):
        return MC.getAttr(self._pointer.name() + ".max_distance")


    @maxDistance.setter
    def maxDistance(self, maxDistanceValue):
        MC.setAttr(self._pointer.name() + ".max_distance", maxDistanceValue)


    @property
    def falloff(self):
        return MC.getAttr(self._pointer.name() + ".falloff")


    @falloff.setter
    def falloff(self, falloffValue):
        MC.setAttr(self._pointer.name() + ".falloff", falloffValue)


    @property
    def includeExclude(self):
        return MC.getAttr(self._pointer.name() + ".id_inclexcl")


    @includeExclude.setter
    def includeExclude(self, includeExcludeValue):
        MC.setAttr(self._pointer.name() + ".id_inclexcl", includeExcludeValue)


    @property
    def nonSelf(self):
        return MC.getAttr(self._pointer.name() + ".id_nonself")


    @nonSelf.setter
    def nonSelf(self, nonSelfValue):
        MC.setAttr(self._pointer.name() + ".id_nonself", nonSelfValue)

    @property
    def nonSelf(self):
        return MC.getAttr(self._pointer.name() + ".id_nonself")


    @nonSelf.setter
    def nonSelf(self, nonSelfValue):
        MC.setAttr(self._pointer.name() + ".id_nonself", nonSelfValue)






def assignBaseShader(self, shaderName):
    # self == <mesh>
    
    meshName = self._pointer.fullPathName()

    # Get the <groupiD> entering the meshNode
    uselessGroupIds = MC.listConnections(meshName, source=True, destination=False, type="groupId")
    
    """Questa parte la schiaffi in un "with DefaultRenderLayerActive(): ..." """ 
    
    with DefaultRenderLayerActive_active():
        pass






def getObjectSets(self, **kwargs):
    onlyShadingEngines_flag = kwargs.get("onlyShadingEngines", kwargs.get("ose", False))
    noShadingEngine_flag    = kwargs.get("noShadingEngine", kwargs.get("nse", True))
    
    # In this case, it preserves namespaces... wow
    setNames = MC.listSets(object=self.nodeName) or []
    #setNames = MC.listSets(object=self.shortName) or []

    """ THIS IS HORRID """
    if onlyShadingEngines_flag:
        results = [ObjectSet(x) for x in setNames if MC.nodeType(x) == "shadingEngine"]
    elif noShadingEngine_flag:
        results = [ObjectSet(x) for x in setNames if MC.nodeType(x) != "shadingEngine"]
    else:
        results = [ObjectSet(x) for x in setNames]

    return results














"""
class UI(object):
    @staticmethod
    def getMayaMainQWidget():
        mayaWindow_SWIGPointer = OMUI.MQtUtil.mainWindow() # SWIG wrap of a C++ pointer
        mayaWindow_address     = mayaWindow_SWIGPointer.__long__() # equivalent to long(...)
        mayaWindow_QWidget     = SH.wrapInstance(mayaWindow_address, QG.QWidget) # The PySide object
        return mayaWindow_QWidget

"""

"""        
#fava = MuNode("XXX")

# ex:
# xxx = Transform.create("myTrans", t=(1,1,1), r=(2,2,2), s=(1,1,1), v=True, ws=True, p=shit)
# or
# xxx = Transform.create("myTrans")
# xxx.t(1,2,3)
#    .s(3,4,5)
#    .r(3,0,0)
#    .v(True)
#    .p(geppetto)






 OGGETTI CHE INCAPSULANO FACILMENTE LE FATALITY, CON ERRORi, FORMATTAZIONE, popUpWindow
VALIDO ANCHE PER WARNING ECT ECT, DEBUGGING, ETC ECT
class popupWindow
class Fatality(popUpWindow):
    title =...
    list =...
    makeSelectable...
    show, color, size, type etc etc


# Esempio di pointer disattivabile
# - per i DAGNodes serve MFnDagNode per recuperare il long name
# deve esserci il minimo possibile di overhead nel "name()" perche
# tutti la chiameranno...
# se porribile:
# - se pointer: hai un wrapper alla chiamata del MFn
# - se !pointer: hai un attributo diretto che non chiama nulla
#
# SI PUO FARE????
     

def getPlugPtr(nodeName, attrName):
    selList = OM.MSelectionList()
    try:
        selList.add(nodeName)
    except:
        MC.error("node missing!")    
    mObj = OM.MObject()
    selList.getDependNode(0, mObj)
    
    # Get node pointer
    ptr  = OM.MFnDGNode(mObj)
    
    # Get plug pointer
    try:
        plug = ptr.findPlug(attrName)
    except:
        MC.error("attr miing")
    return plug

def getLogicalIndices(nodeName, arrayAttrName):               
    plug = getPlugPtr(nodeName, arrayAttrName)    
    size = plug.numElements()
    logicalIndices = []
    for i in range(size):
        arrayPlug = plug.elementByPhysicalIndex(i)
        #print (x.logicalIndex(), x.name(), x.asString())
        logicalIndices.append(arrayPlug.logicalIndex())
    return logicalIndices 




"""






"""
CALLBACKS

import functools
if MC.window("XXX", ex=1):
    MC.deleteUI("XXX") 
MC.window("XXX", t="CALLBACK", tlb=1, s=0, mb=0)
MC.showWindow("XXX")
MC.window("XXX", edit=True, width=30, height=30)

def selectionListener(index):
    sel = MC.ls(selection=True, long=True, objectsOnly=True)
    try:
        print str(index) + "^ [SEL]", sel[-1]
    except:
        print " None"

def curry(func, arg):
    def _func():
        func(arg)
    return _func
    
for i in range(10):
    #MC.scriptJob(event=["SelectionChanged", functools.partial(selectionListener, i)], parent="XXX") 
    n = MC.scriptJob(event=["SelectionChanged", curry(selectionListener, i)], parent="XXX") 
    print str(i) + " --> " + str(n)

# Apparently, the order of call is not predictable...   

"""


"""
RENDER SHIT


# To delete a layer, DON'T delete directly the node!!!
MM.eval("renderLayerEditorDeleteLayer RenderLayerTab " + layer + ";")

def orderRenderLayers(*args):
    # Apprently, "renderLayers" has not a sorting option ("displayLayers" does), so:
    # - get from renderLayerManager the layer list (with proper names)
    # - reorder via the ".displayOrder" attribute of each layer
    renderLayers = MC.listConnections("renderLayerManager.renderLayerId")
    numberOfLayers = len(renderLayers)

    renderLayers.remove("defaultRenderLayer")
    sortedRenderLayers = sorted(renderLayers)
    
    for index, layer in enumerate(sortedRenderLayers):
        MC.setAttr(layer + ".displayOrder", numberOfLayers - index - 1)




def getRenderLayerData(*args):
    renderLayerData = {}
    renderLayers = MC.listConnections("renderLayerManager.renderLayerId", source=False, destination=True, 
    type="renderLayer", exactType=True) or []
    for renderLayer in renderLayers:
        renderLayerData[renderLayer] = {}
    
        renderLayerData[renderLayer]["valueAdjustments"] = []
        logicalIndices = MC.getAttr(renderLayer + ".adjustments", multiIndices=True) or []
        for i in logicalIndices:
            plug = MC.listConnections(renderLayer +".adjustments[" + str(i) + "].plug", s=True, d=False, plugs=True)[0]
            value = MC.getAttr(renderLayer +".adjustments[" + str(i) + "].value")
            if isinstance(value, list) and len(value) == 1:
                # "getAttr" returns [(a, b, c)] for triples (r, t, s, ...) 
                value = value[0]
            renderLayerData[renderLayer]["valueAdjustments"].append((plug, value))
    
        renderLayerData[renderLayer] ["connectionAdjustments"] = []
        logicalIndices = MC.getAttr(renderLayer + ".outAdjustments", multiIndices=True) or []
        for i in logicalIndices:
            outPlug = MC.listConnections(renderLayer +".outAdjustments[" + str(i) + "].outPlug", s=True, d=False, plugs=True)[0]
            outValue = MC.listConnections(renderLayer +".outAdjustments[" + str(i) + "].outValue", s=False, d=True, plugs=True)[0]
            renderLayerData[renderLayer]["connectionAdjustments"].append((outPlug, outValue))
    return renderLayerData

"""    



"""
#
#    ngSkinTools
#    Copyright (c) 2009-2015 Viktoras Makauskas. 
#    All rights reserved.
#    
#    Get more information at 
#        http://www.ngskintools.com
#    
#    --------------------------------------------------------------------------
#
#    The coded instructions, statements, computer programs, and/or related
#    material (collectively the "Data") in these files are subject to the terms 
#    and conditions defined by
#    Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License:
#        http://creativecommons.org/licenses/by-nc-nd/3.0/
#        http://creativecommons.org/licenses/by-nc-nd/3.0/legalcode
#        http://creativecommons.org/licenses/by-nc-nd/3.0/legalcode.txt
#         
#    A copy of the license can be found in file 'LICENSE.txt', which is part 
#    of this source code package.
#    

from ngSkinTools.ui.layerDataModel import LayerDataModel
from ngSkinTools.utils import Utils
from maya import cmds
from ngSkinTools.ui.events import MayaEvents, restartEvents, scriptJobs
from ngSkinTools.doclink import SkinToolsDocs
from ngSkinTools.log import LoggerFactory


log = LoggerFactory.getLogger("HeadlessDataHost")


class RefCountedHandle:
    '''
    reference counted handle to a dynamically allocated instance;
    
    creates reference after first addReference() call, and destroys it 
    when last reference is removed via removeReference()
    '''
    
    def __init__(self,instantiator):
        self.instantiator=instantiator
        self.instance = None
        self.references = set()
    
    def getCurrentInstance(self):
        '''
        returns handle to currently created instance
        '''
        return self.instance

    def addReference(self,refSource):
        if refSource in self.references:
            return
        
        if len(self.references)==0:
            self.instance = self.instantiator()
            self.instance.initialize()
            
        self.references.add(refSource)
        
        
    def removeReference(self,refSource):
        '''
        returns false, if provided reference was not found in the stack
        '''
        
        if refSource not in self.references:
            return False
        
        self.references.remove(refSource)
        if len(self.references)==0:
            self.instance.cleanup()
            self.instance=None
            
        return True
            
        
class HeadlessDataHost:

    '''
    A singleton of this object is created when at least one UI window is opened,
    and performs a cleanup once all objects are closed
    '''
    
    HANDLE = None
    
    @staticmethod
    def get():
        return HeadlessDataHost.HANDLE.getCurrentInstance() 
    
    def __init__(self):
        self.documentation = SkinToolsDocs
        
        
    def initialize(self):
        log.debug("creating headless data host")
        
        LayerDataModel.reset()
        restartEvents()

        Utils.loadPlugin()

        MayaEvents.registerScriptJobs()
        
        LayerDataModel.getInstance()
        
    def cleanup(self):
        '''
        cleanup any acquired resources
        '''
        scriptJobs.deregisterScriptJobs()
            
        log.debug("headless data host cleanup")


HeadlessDataHost.HANDLE = RefCountedHandle(HeadlessDataHost)        
    
#
#    ngSkinTools
#    Copyright (c) 2009-2015 Viktoras Makauskas. 
#    All rights reserved.
#    
#    Get more information at 
#        http://www.ngskintools.com
#    
#    --------------------------------------------------------------------------
#
#    The coded instructions, statements, computer programs, and/or related
#    material (collectively the "Data") in these files are subject to the terms 
#    and conditions defined by
#    Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License:
#        http://creativecommons.org/licenses/by-nc-nd/3.0/
#        http://creativecommons.org/licenses/by-nc-nd/3.0/legalcode
#        http://creativecommons.org/licenses/by-nc-nd/3.0/legalcode.txt
#         
#    A copy of the license can be found in file 'LICENSE.txt', which is part 
#    of this source code package.
#    



"""
"""
from maya import cmds
from ngSkinTools.utils import Utils
from ngSkinTools.log import LoggerFactory


log = LoggerFactory.getLogger("events")

class Signal:
    '''
    Signal class collects observers, interested in some particular event,and handles
    signaling them all when some event occurs. Both handling and signaling happens outside
    of signal's own code
    '''
    
    TOTAL_HANDLERS = 0
    
    def __init__(self,name=None):
        self.name = name
        self.reset();
        
    def reset(self):
        self.handlers = []
        self.executing = False
        
    
    def emitDeffered(self,*args):
        import maya.utils as mu
        mu.executeDeferred(self.emit,*args)
        
        
    def emit(self,*args):
        if self.executing:
            raise Exception,'Nested emit on %s detected' % self.name
        
        self.executing = True
        try:
            for i in self.handlers[:]:
                try:
                    i(*args)
                except Exception,err:
                    import traceback;traceback.print_exc()
        finally:
            self.executing = False
            

    class UiBoundHandler:
        '''
        Proxy wrapper for event handlers that has a method to deactivate 
        itself after when associated UI is deleted
        '''
        def __init__(self,handler,ownerUI,deactivateHandler):
            scriptJobs.scriptJob(uiDeleted=[ownerUI,self.deactivate])
            self.handler=handler
            self.deactivateHandler=deactivateHandler
        
        def deactivate(self):
            self.deactivateHandler(self)
            
            
        def __call__(self):
            self.handler()
            
            
    def addHandler(self,handler,ownerUI=None):
        if (ownerUI!=None):
            handler=self.UiBoundHandler(handler,ownerUI,self.removeHandler)
            
        self.handlers.append(handler)

    def removeHandler(self,handler):
        
        # if handler was wrapped, try finding the wrapper first
        for i in self.handlers:
            if isinstance(i, self.UiBoundHandler) and i.handler==handler:
                handler = i
                
        try:
            self.handlers.remove(handler)
        except ValueError:
            # not found in list? no biggie.
            pass
        


class EventsHost(object):
    def restart(self):
        for _, propertyValue in vars(self).iteritems():
            if isinstance(propertyValue, Signal):
                propertyValue.reset()

class LayerEventsHost(EventsHost):

    def __init__(self):
        self.nameChanged = Signal('layerNameChanged')
        self.layerListModified = Signal('layerDataModified')
        self.currentLayerChanged = Signal('currentLayerChanged')
        self.currentInfluenceChanged = Signal('currentInfluenceChanged')
        self.layerSelectionChanged = Signal('layerSelectionChanged')
        self.layerListUIUpdated = Signal('layerListUIUpdated')
        self.layerAvailabilityChanged = Signal('layerAvailabilityChanged')
        self.influenceListChanged = Signal('influenceListChanged')
        self.mirrorCacheStatusChanged = Signal('mirrorCacheStatusChanged')


class MayaEventsHost(EventsHost):
    '''
    global maya-specific events
    '''
    def __init__(self):
        
        self.nodeSelectionChanged = Signal('nodeSelectionChanged')
        self.undoRedoExecuted = Signal('undoRedoExecuted')
        self.toolChanged = Signal('toolChanged')
        self.quitApplication = Signal('quitApplication')
        
    def registerScriptJob(self,jobName,handler):
        def mockHandler(*args,**kwargs):
            log.debug("running script job "+jobName)
            handler(*args,**kwargs)
            
        
        job = scriptJobs.scriptJob(e=[jobName,mockHandler if Utils.DEBUG_MODE else handler])
        

            
    def registerScriptJobs(self):
        self.registerScriptJob('SelectionChanged',self.nodeSelectionChanged.emit)
        self.registerScriptJob('Undo',self.undoRedoExecuted.emit)
        self.registerScriptJob('Redo',self.undoRedoExecuted.emit)
        self.registerScriptJob('ToolChanged',self.toolChanged.emit)        
        self.registerScriptJob('quitApplication',self.quitApplication.emit)    
        
    
    


def restartEvents():
    '''
    (re)creates signal holders in LayerEvents and MayaEvents  
    '''
    MayaEvents.restart()
    LayerEvents.restart()


class ScriptJobHost:
    def __init__(self):
        self.scriptJobs = []
        
    def scriptJob(self,*args,**kwargs):
        '''
        a proxy on top of cmds.scriptJob for scriptJob creation;
        will register a script job in a global created script jobs list
        '''
        job = cmds.scriptJob(*args,**kwargs)
        self.scriptJobs.append(job)
    
    def deregisterScriptJobs(self):
        for i in self.scriptJobs:
            try:
                cmds.scriptJob(kill=i)
            except:
                pass
        self.scriptJobs = []
        
scriptJobs = ScriptJobHost()

MayaEvents = MayaEventsHost()
LayerEvents = LayerEventsHost() 
"""