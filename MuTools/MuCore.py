__version__ = '1.0.4'
print '--> Executing MuCore...'

""" SINGULARITY SKINCLUSTER FIX                                        """
""" Note the transform=None (in MEL THE ORDER OF ARGS MATTERS, here no)"""
"""

import maya.cmds as MC

def correctWeights(skinClusterName, singType):
    vertices = MC.ls(sl=True, flatten=True)
    if len(vertices) != singType:
        MC.error('EXACTLY {} VERTICES!!!'.format(singType))
        
    joints = set()
    for vtx in vertices:
        vtxJoints = MC.skinPercent(skinClusterName, vtx, query=True, transform=None)
        vtxActiveJoints = [x for x in vtxJoints if MC.skinPercent(skinClusterName, vtx, query=True, transform=x) > 0.0]
        joints = joints | set(vtxActiveJoints)
    
    for joint in joints:
        # take the first weight and copy to the others
        valueToSet = MC.skinPercent(skinClusterName, vertices[0], query=True, transform=joint)
        
        for i in range(1, singIndex)
            MC.skinPercent(skinClusterName, vertices[i], transformValue=[(joint, valueToSet)])
        
        # Lock joint to prevent interactive update
        MC.setAttr(joint + '.liw', 1) 
    
    # Unlock joints    
    for joint in joints:
        MC.setAttr(joint + '.liw', 0) 

correctWeights('skinCluster12', 3)    
"""





print '>>>[{}] Interface:'.format(__name__)
print
print '                    GETTER    -->  object.myProp()        (or object.myProp(*args, **kwargs) if needed)'
print '                    SETTER    -->  object.setMyProp(...)'
print                    
print '                    STRINGIFY -->  object.myPropAsStr()'
print '                              -->  str(object.myProp)     (and using __repr__ to get more informations)'
print 
print '                    DON\'T use a shitty "object.myProp" as a getter/@property... (it\'s sooo \'Pythonic\')'
print '                    (you\'d have 2 styles for getters, sometimes a bare "xxx.pippo", sometimes "xxx.pippo(params)"... ugly!)'
print '                    A priory, "object.myProp" MUST be treated as "object._myProp": INTERNAL and PRIVATE!!!'
print 
print '                    --> BE CONSISTENT, NOT "PYTHONIC" <--'



import MuTools.MuUtils   as Utils

import maya.cmds         as MC
import maya.OpenMaya     as OM 

import functools
import os
import time
import types
import uuid



#------------------------------------------------------------------------------
# Loading module...
Utils.moduleLoadingMessage()
#------------------------------------------------------------------------------



# Instantiating the 'MuCoreLog'
log       = Utils.Log()
debug     = log.debug
hardDebug = log.hardDebug



def printDebug(*args, **kwargs):
    # RELIC
    pass






"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Try this;
Then in the wrappers you can do:
def wrappedCluster(node):
    MC.cluster(name=nodeName(node) + "Clustering", relative=True)
And call it in two ways:

wrappedCluster(<MuNode>)
wrappedCluster(<str>)

--> OR WRAP THE ENTIRE COMMAND ENGINE TO AUTOMATIZE THIS...    

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def nodeName(obj):
    if isinstance(obj, basestring):
        # Node name
        return obj
    else:
        # MuNode derived
        return obj.name()











"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

CONTEXT MANAGERS

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Typical usage:
# - with #####Active(*args, **kwargs): ...
# - with #####Disabled(*args, **kwargs): ...

class RootNamespaceActive(object):
    def __enter__(self):
        self.originalNamespace = MC.namespaceInfo(currentNamespace=True)
        MC.namespace(set=':')        
    def __exit__(self, *args):
        MC.namespace(set=self.originalNamespace)



class DefaultViewportActive(object):
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



class TimerActive(object):
    def __enter__(self):
        self.startTime = time.clock()
    def __exit__(self, *args):
        print "-"*80
        print "Elapsed time:", time.clock() - self.startTime
        print "-"*80
        print  



class ProfilerActive(object):
    """ A context for cProfile """
    pass



class MainPanelDisabled(object):
    def __enter__(self):
        MM.eval('paneLayout -e -manage false $gMainPane')
    def __exit__(self, *args): 
        MM.eval('paneLayout -e -manage true $gMainPane')



class WaitCursorActive(object):
    def __enter__(self):
        MC.waitCursor(state=True)
    def __exit__(self, *args):
        MC.waitCursor(state=False)    



class UndoChunkOpen(object):
    def __init__(self, undoChunkName):
        self._name = undoChunkName

    def __enter__(self):
        MC.undoInfo(chunkName=self._name, openChunk=True)

    def __exit__(self, *args):
        MC.undoInfo(chunkName=self._name, closeChunk=True)










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


class PlugFatality(Fatality):
    def __init__(self, attrName):
        tag = "attribute error"
        mess = "you just did shit \"" + attrName + "\" die!"        
        super(PlugFatality, self).__init__(tag, mess)
            

class NameFatality(Fatality):
    def __init__(self, nodeName):
        # At this point the script is already dead, so don't worry about performances and find-out the reason:
        candidates = MC.ls(nodeName)

        if not candidates:
            # No ambiguity, simply it's a shitty name
            tag     = 'UNKNOWN NAME'
            message = 'There\'s no DGNode named "{}"!'.format(nodeName)        
        
        else:
            # The provided name is not enough to identify a node
            tag     = 'AMBIGUOUS NAME'
            message = 'The name "{}" is not long enough to determine an unique DAG-node!\nPossible alternatives:'.format(nodeName)
            for candidate in candidates:
                message += '\n - "{}"'.format(candidate)        

        super(NameFatality, self).__init__(tag, message)
        
















#======================================================================================================
# DECORATORS
#======================================================================================================

# Check for decorators' order:
#   @staticmethod
#   @functionDebug
#   def fuckYou(...)
# One fails:(, the other not:)
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






# Apparently, the price for this decorator is really irrelevant, 'cause it does almost nothing
# PREMATURE OPTIMIZATION IS EVIL!
def massiveMethod(func):
    """ IT DOESN'T WORK WITH @DECORATORS... fuck! """

    """
    @massivemethod
    def setVisibility():
        ...

    Adds the flag _isMassive to a "massive" method; it's up to the <Bundle>
    to inspect all classes and create a massive method!
    """ 

    def wrappedFunc(*args, **kwargs):
        return func(*args, **kwargs)

    wrappedFunc._isMassive = True # The value is not relevant!   
    wrappedFunc.__name__ = func.__name__
    wrappedFunc.__doc__  = func.__doc__

    return wrappedFunc   
































'''
#################################################################################################
=================================================================================================
-------------------------------------------------------------------------------------------------
                             ,,          
              mm            `7MM          
              MM              MM          
    ,pP"Ybd mmMMmm `7M'   `MF'MM  .gP"Ya  
    8I   `"   MM     VA   ,V  MM ,M'   Yb 
    `YMMMa.   MM      VA ,V   MM 8M"""""" 
    L.   I8   MM       VVV    MM YM.    , 
    M9mmmP'   `Mbmo    ,V   .JMML.`Mbmmd' 
                      ,V                  
                   OOb"  

-------------------------------------------------------------------------------------------------
=================================================================================================
#################################################################################################
'''













"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
===============================================================================================================================================
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

MAYA NODE WRAPPERS

_______________________________________________________________________________________________________________________________________________
===============================================================================================================================================
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""--------------------------------------------------------------------------
C'e' un modo per mette sta merda in un dizionario? Specialmente le classi!
e evitare quel troiaio immondo di doppio controllo... ORRENDo

'kTransform'  Transform  OM.MFnTransform
'kMesh'       Mesh       OM.MFnMesh
'kSet'        ObjectSet  OM.MFnSet 
--------------------------------------------------------------------------"""




"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
CLASS STRUCTURE
---------------------------------------------------------------------------------
--> All methods inside a category MUST be sorted!

  STATIC METHODS 
      staticA()
      staticB()
      ...

  CLASS METHODS  
      cMathodA()
      cMethodB()
      ...

  -------------------------
  CONSTRUCTOR/INITIALIZER
      __new__
      __init__
  -------------------------

  MAGIC METHODS  
      __magicA__
      __magicB__
      ...
  
  QT-SLOTS       
      slotA()
      slotB()
      ...

  QT-VIRTUALS    
      virtualA()
      virtualB()
      ...

  METHODS        
      methodA()
      methodB()
      ...


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



"""""""""""""""""""""""""""""""""""
CLASS HIERARCHY
-----------------------------------
MuNode            [FACTORY]
MuPlug       [MPLUG WRAP]

DGNode          
  DAGNode         [ABSTRACT]
    Mesh
    Transform
      Joint
  ObjectSet  
  RenderLayer
  ? Reference ?   (yep, it's node-based!)  

List              [MASSIVE]
Set               [MASSIVE]
Scene             [MODULE?] 
"""""""""""""""""""""""""""""""""""








class DGNode(object):
    """
    ------------------------------------------
    NEW BASIC GETTERS
     .type()       -->  Maya type
     .name()       -->  minimal unique name
     .longName()   -->  full DAGPath
     .shortName()  -->  bare nodeName
     
    Forget @property and bare attributes
    ------------------------------------------
    """ 



    #-----------------------------
    # STATIC/CLASS METHODS
    #-----------------------------
    @staticmethod    
    def create(nodeType='network', name=None):
        """
        ---------------------------------------------------------------------------
        DESCRIPTION
          Create a new dependNode of the chosen type.
          If others auxiliary nodes must be created (as for 'mesh'), they'll be 
          named automatically.


        ARGUMENTS
          nodeType


        RETURN
          <MuNode>
            The wrapped node (not the auxiliaries)


        NOTE
          Each derived class should reimplement this method!
        ---------------------------------------------------------------------------      
        """        


        if name is not None:
            newNodeName = MC.createNode(nodeType, n=name, skipSelect=True)
        else:
            newNodeName = MC.createNode(nodeType, skipSelect=True)    
        return MuNode(newNodeName)







    #-----------------------------
    # INITIALIZER
    #-----------------------------
    def __init__(self, mObject, mFn):

        # TERMINOLOGY:
        # The MObject is indeed the c++ pointer (with type included)
        # pointing to the true c++ object; the MFn is only the
        # simplification of the real interface od the apiObj
        # The mechanic MObject-MFn only exists to allow the 'facade' interface
        #
        # But in the end, once you have a proper valid MFn(MObject), you have
        # full access to the apiObj

        # Hence I'll stick to:
        #-------------------------------------------------
        # self._apiObj --> self._Mfn.setObject(self._mObject)
        #------------------------------------------------
        # (even though it's just the 'facaded' interface of the real apiObject)


        # Every wrap carries:
        # - _mObject        -->  the real C++ pointer
        # - _mObjectHandle  -->  the pointer validator
        # - _mFn            -->  a detached compatible functionSet
        # - _apiObj         -->  a 'property' return a valid mFn
        #                        (this is the only exception of a tolerated 'property')
        # 
        # To use an API method:
        
        #   (OLD) self._mObj.method(... )
        #   (NEW) self._apiObj.method(... )

        # There will be an exception if the _mObj is invalid!


        self._mObject       = mObject
        self._mObjectHandle = OM.MObjectHandle(self._mObject)
        self._mFn           = mFn
        self._type          = self._apiObj.typeName()


        """
        Note:
        This is not gonna work with instances. If you save only the pointer, you'll have just a node.
        But since it's shared, all DAG methods (getParent, getChildren) will fail.

        To work with instances, you need to save the DAGPath (of course...)
        """


    @property
    def _apiObj(self):
        """
        Probably a little overzealous and paranoid; but nonetheless the performance
        penalty is irrelevant compared to the huge weight of using the
        API in the first place (even in a minimalistic not pymel-like way)
        This way, if an MObject enters in the 'dangling pointer' state, we're
        gonna know it:)
        """
        # To return a VALID mFn:
        # - Use _mObjectHandle to test if the pointer _mObject is still valid
        # - Attach _mFn to _mObject
        # - Return _mFn

        if self._mObjectHandle.isValid():
            self._mFn.setObject(self._mObject)
            return self._mFn

        else:
            # The pointer is invalid; check if it's alive (i.e. the apiObj is deleted
            # but still in memory, e.g. in the undo queue)
            MC.error('INVALID POINTER!!!')
            # ... Now what? Need to recover? How? Or simply a blocking 'Fatality'?




    #-----------------------------
    # MAGIC METHODS
    #-----------------------------  
    

    # COMPARING WRAPPERS
    #
    #   x = MuNode('myNode')
    #   y = MuNode('myNode')
    #
    #     id(x) == id(y)    --> False: they're 2 different wrappers
    #         x == y        --> True:  they point to the same node
    #   hash(x) == hash(y)  --> True:  same minimalName --> same node
    #   
    #   set([x, y])         --> MuNode('myNode')... see below
    #   
    #   z = MuNode('myNode')
    #   z in List(x, y)   --> True: it checks __eq__




    def __eq__(self, other):
        """
        ------------------------------------------------------------------------------
        CUSTOM EQUALITY
          Return True iff the DGNode wrappers wrap the same Maya node!

          The MObjects have an overloaded == which returns True iff they points to 
          the same Maya object (use MFnBase.object() --> <MObject>)
        ------------------------------------------------------------------------------
        x in [a, b, c, d, e]  -->  __eq__ is called to test membership
        ------------------------------------------------------------------------------
        """

        return self._apiObj.object() == other._apiObj.object()



    def __hash__(self):
        """
        ------------------------------------------------------------------------------
        HASH
          hash(node) == node.__hash__()
          It is used when casting a List to a Set (or in a dict, but NOT in a list).
          E.g. from [a, b] to set([a, b]):

            hash(a) != hash(b)  -->  The object are (assumed to be) different and no 
                                     __eq__ is performed; both will be added!
            hash(a) == hash(b)  -->  Equality is judged via the __eq__!

          Hence, the mandatory rule must be respected; nothing more!                         
        ------------------------------------------------------------------------------
        MANDATORY RULE:
          a == b  >>>  hash(a) == hash(b)
          The contrary is not needed (except for speed)! A 'good' hash allows Python to
          skip expensive __eq__ tests; if __hash__ is not a weaker __eq__ everything 
          can happen!

          >>> __hash__ is a weaker __eq__ <<<
        ------------------------------------------------------------------------------
        WARNING:
          An object with hash = h must be h-immutable (not necessarily deeply-immutable)
          - with h = longName, a DGnode is NOT h-immutable;
          - with h = MObjectHandle.hashCode() a DGNode is almost h-immutable; BUT check 
            for the UNDO/REDO operation: the value could change!

          The problem here is an object (!.isValid() and .isAlive()) (deleted + undoQueue)  
        ------------------------------------------------------------------------------
        """

        # The only warranty is that if the wrappers point to the same node, they have the same hash...
        return hash(self.name()) # NO, a wrapper is not minimalName-immutable!

    





    def __getattr__(self, attr):
        # '__getattr__' is called only when the Python object has not an 
        # attribute named 'attr'; hence we try to ask the same attribute 
        # to the underlying DependNode

        """ 
        NOTE:
          The old __getattr__ is gonna fail in these cases:
          - array plug (as 'input1D[0]')
          - child of a compound (as 't.tx')

          I should try to recover the arrayPlug this way:
          -            myNode.plugName[3] <--> myNode.__getattr__('plugName').__getitem__[3]
          - myNode.compoundPlug.childPlug <--> myNode.__getattr__('compoundPlug').__getattr__('childPlug')
          Where le last __getitem__ and __getattr__ are methods of MuPlug

        """
        try: 
            # Accessing the attribute via the commandEngine is necessary...
            mPlug = self._apiObj.findPlug(attr, True)

        except: # It's a fucking generic <RuntimeError> (__doc__ == 'Unspecified...' WOW!)
            # Even the DependNode can't answer
            MC.error('[Plug Error] The plug "{0}" can\'t be found on node/MuNode "{1}"!'.format(attr, self.name()))

        return MuPlug(mPlug)
    

    def getPlug(self, attributeName):
        """ 
        Get plug by:
        -   NAME: myNode.myAttr
        - STRING: myNode.getPlug('myAttr')
        
        NOTE:
          You will have to check when attributeName has special chars '.' or '[]'
          - myNode.getattr('input1[1]')
          - myNode.getattr('t.tx')
          For the moment, it fails!!!  
        """

        return self.__getattr__(attributeName)






    def __repr__(self):
        # Format: "name"<Type>
        return '"{0}"<{1}>'.format(self.name(), self.type())      



    def __str__(self):
        # The 'minimal' name
        return self.name()



    #-----------------------------
    # METHODS
    #-----------------------------



    def addPlug(self, **kwargs):
        """
        ----------------------------------------------------
        EXTRA FLAGS:
          type(t) --> shortcut for dataType/attributeType
          name(n) --> EXTRA for longName
        ----------------------------------------------------

        FLAGS of MC.addAttrs:
          niceName=string, 
          longName=string, 
          shortName=string, 

          exists=boolean, 

          keyable=boolean, 
          hidden=boolean, 

          defaultValue=float, 
          dataType=string, 
          attributeType=string, 

          enumName=string, 
          
          hasMaxValue=boolean, 
          hasMinValue=boolean, 
          maxValue=float, 
          minValue=float,           
          hasSoftMaxValue=boolean, 
          hasSoftMinValue=boolean, 
          softMaxValue=float, 
          softMinValue=float, 

          multi=boolean, 
          indexMatters=boolean, 
          parent=string,           
          numberOfChildren=uint, 

          internalSet=boolean, 

          readable=boolean, 
          writable=boolean 
          storable=boolean, 

          binaryTag=string, 
          cachedInternally=boolean, 
          usedAsColor=boolean, 
        """

        # If present, 'name' rules over 'longName' and 'shortName'
        name_flag = kwargs.pop('name', kwargs.pop('n', None))
        if name_flag is not None:
            plugName = name_flag
            try:
                del kwargs['longName']
                del kwargs['ln']
                del kwargs['shortName']
                del kwargs['sn']
            except:
                pass

            kwargs['longName'] = name_flag    
        else:
            plugName = kwargs.get('shortName', kwargs.get('sn', kwargs.get('longName', kwargs.get('ln', None))))


        # 'type' flag to simplify creation
        plugType  = kwargs.pop('type',  kwargs.pop('t', None))
        if plugType is None:
            raise PlugFatality("flag 'type' (t) is mandatory!")                               
        


        # Check if already exists
        if MC.attributeQuery(plugName, node=self.name(), exists=True):
            raise PlugFatality("MayaNode " + self.name() + " has already a <Plug> named " + plugName)  
        

        # Creation
        if plugType == "double":
            # horrid
            defaultValue = kwargs.get('defaultValue', kwargs.get('dv', 0.0))
            keyable      = kwargs.get('keyable', kwargs.get('k', True))

            MC.addAttr(self.name(), longName=plugName, attributeType="double",
                defaultValue=defaultValue, keyable=True, hidden=False)
            
            return self.__getattr__(plugName) # (HORRID)A MuPlug



        elif plugType == "string":
            # 'defaultValue' is meaningful only for numerics; just initialize 
            initValue = kwargs.get("defaultValue", kwargs.get("dv", ""))
            MC.addAttr(nodeName, longName=attrName, dataType="string", 
            multi=multiFlag, keyable=False)        
            MC.setAttr(nodeName + "." + attrName, initValue, type="string")
            print "created!"
            
        elif plugType == "bool":
            # 'defaultValue' is meaningful only for numerics; just initialize 
            initValue = kwargs.get("defaultValue", kwargs.get("dv", False))
            MC.addAttr(nodeName, longName=attrName, attributeType="bool", 
            multi=multiFlag, keyable=False)        
            MC.setAttr(nodeName + "." + attrName, initValue)
            print "created!"    
        
        elif plugType == "enum":
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
        





    @massiveMethod
    def fuckYou(self):
        return '"{}" is bundled!'.format(self.name)



    def longName(self): 
        return self._apiObj.name()



    def name(self): 
        # To allow loop on generic nodes and DAGs
        return self._apiObj.name()



    def rename(self, newName):
        newName = MC.rename(self.name(), newName)
        return self



    def shortName(self): 
        return self._apiObj.name()



    def type(self):
        # Not really necessary, but it's a matter of coherence: 
        # - xxx.parent()
        # - xxx.name()
        # - xxx.type()
        return self._type



    #========================================================
    def lock(self):
        try:
            self._apiObj.setLocked(True)
        except:
            # Pointer failure, referenced object etc ect
            pass
    def unlock(self):
        try:
            self._apiObj.setLocked(False)
        except: 
            # as for .lock()
            pass
    def isLocked(self):    
        return self._apiObj.isLocked()
    def isReferenced(self):
        return self._apiObj.isFromReferencedFile()    
    #========================================================    










    """ CHECK IF IT'S A TRANSFORM and IT'S 'TYPIZED' """


    def _isTypedTransform(self, allowedType='mesh', noIntermediate=True, onlyOne=True):
        """ Check if the transform has shapeChildren of an allowedType """
        # The flag combination 'shapes + noIntermediate' is valid, 
        # but not 'type + noIntermediate' (the latter is ignored)
        if self.type()  != 'transform':
            return False

        shapeChildren = MC.listRelatives(self.name(), children=True, path=True, shapes=True, noIntermediate=noIntermediate) or []
        allowedShapeChildren = [x for x in shapeChildren if MC.nodeType(x) == allowedType]
        
        if onlyOne:
            return len(allowedShapeChildren) == 1
        else:
            return len(allowedShapeChildren) >= 1 



    def isPureTransform(self):
        """
        Check if:
         - it's a 'transform';
         - it has no 'shape' children.
        """
        if self.type()  != 'transform':
            return False

        shapeChildren = MC.listRelatives(self.name(), children=True, path=True, shapes=True, noIntermediate=False) or []
        return len(shapeChildren) == 0



    def isMeshTransform(self, onlyOneAllowed=True):
        """ Check if the transform has only one meshChild (or multiple, according to 'onlyOneAllowed') """
        return self._isTypedTransform(allowedType='mesh', noIntermediate=True, onlyOne=onlyOneAllowed)
    


    def isLocatorTransform(self):
        return self._isTypedTransform(allowedType='locator', noIntermediate=True, onlyOne=True)


       
    def isNurbsCurveTransform(self):
        return self._isTypedTransform(allowedType='nurbsCurve', noIntermediate=True, onlyOne=False)  








class Reference(object):
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Quando un filePath non viene trovato, on a lapossibilita di SKIP IGNORE RETRY, CHANGE
    ... lo SKIP lascia la referenza not loaded ma dentro la sceneNamespaces
    ... IGNORE getta via la referenza

    KOSA SUCCEDE IN MAYAPY????
    - da dei warnings, ma continua;
    - getReferences() funziona
    - abbiamo tutti i referenceNodes
    - abbiamo anche i namespace...

    QUINDI TUTTO OK anche in mayapy
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """ 
    --------------------------------------------------------------------------------
    FALSE: even in a bare load, there's always a reference node...
    hence, WRAP IT into a DGNode
    --------------------------------------------------------------------------------


    NO  'Reference' is not necessarily a node wrap; if you open a scene withour loading 
    NO  references, there's NO node. The 'Reference' methods still work (probably hidden). 
    NO  Hence this is a fine example of a 'MuNode' which is not a wrap of a Maya node.

    A 'Reference' object shgould never be directly instantiated. It's up to 
    Scene.getReferences() or Scene.createReference() to do so.

    NOTES:
      - There's no real need to use the API for this, just use the commandEngine.
    """

    #-----------------------------
    # INITIALIZER
    #-----------------------------       
    def __init__(self, filePath):
        self._filePath = filePath



    #-----------------------------
    # MAGIC METHODS
    #-----------------------------
    def __repr__(self):
        representation = '"{0}"({1})<Reference>'.format(str(self.namespace()), self._filePath)
        return representation

    

    #-----------------------------
    # METHODS
    #----------------------------- 
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""
    A bunch of method that works on 'abstract' references:


    def reload(self):
        pass
    def unload(self):
        pass
    def replace(self):
        pass        
    def getNode(self):
        pass
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""


    def filePath(self):
        return self._filePath


    def isValid(self):
        # Simply check if the reference exists as file
        #return os.path.isfile(self.cleanFilePath)
        return MC.file(self.cleanFilePath(), query=True, exists=True)



    def isLoaded(self):
        return MC.referenceQuery(self.filePath(), isLoaded=True)



    def load(self):
        # Try to load a reference only if the file exists; if nod, don't do anything;
        """ Probably it should return True if succeeded or False if it failed! """
        if self.isValid():
            MC.file(self.filePath(), loadReference=self.getReferenceNode().name(), loadReferenceDepth='asPrefs')
            return True
        else:
            return False



    def cleanFilePath(self):
        return self.filePath().split('{')[0]



    def setNamespace(self, newNamespace):
        """
        WHAT HAPPENS IF THE NAMESPACE IS INVALID (or already existing)?
         - should this return True/False if it succeeded/failed???
        """ 
        try:
            MC.file(self.filePath(), edit=True, namespace=newNamespace)
        except:
            raise



    def namespace(self):
        # After a bare load scene (no reference load), each virtual reference has
        # a 'potential' namespace, which is not yet a real namespace
        potentialNamespace = MC.file(self.filePath(), query=True, namespace=True)
        return Namespace(potentialNamespace) 


    """            
    def namespaceAsStr(self):
        # A shortcut for ref.namespace().name()
        potentialNamespace = MC.file(self._filePath, query=True, namespace=True)
        return potentialNamespace         
    """
    """ OBSOLETE """
    #@property
    #def namespace(self):
        
        #Every referenced file MUST have either a namespace or a prefix (and the latter is FATAL)
        
        #potentialNamespace = MC.file(self.filePath, query=True, namespace=True)
        # It could be a "prefix" (and it would be a serious problem because this can't be corrected via a command!!!)
        # NOT EXACTLY; if the namespace already existed because assigned to another asset, this check would fail """
        # ... protect everything!!! """
        #if MC.namespace(exists=potentialNamespace):
        #    return potentialNamespace
        #else:
        #    return None   






    def originalName(self):
        originalName = self._filePath.split('/')[-1].split('{')[0].replace('.ma', '')
        return originalName



    def getReferenceNode(self):
        return MuNode(MC.file(self._filePath, query=True, referenceNode=True))
    







 
class DAGNode(DGNode):
    #-----------------------------
    # INITIALIZER
    #-----------------------------       
    def __init__(self, mObject, mFn):
        printDebug('DAGNode.__init__')
        super(DAGNode, self).__init__(mObject, mFn)
        



    #-----------------------------
    # MAGIC METHODS
    #-----------------------------



    #-----------------------------
    # METHODS
    #-----------------------------
    def parent(self):
        """ By returning a full-fledged node, there's no need for the 'longName' option! """
        if self.isInstanced():
            # Remember, it fails with instances...
            MC.error('INSTANCED!!!')

        parentList = MC.listRelatives(self.name(), parent=True, path=True) or [] 
        try:
            return MuNode(parentList[0])
        except:
            # Child of the world
            return None    


    
    def rootParent(self):
        """ 
        Return None if the DAG is a worldChild, otherwise the worldChild that contains it
        """
        if self.isInstanced():
            # Remember, it fails with instances...
            MC.error('INSTANCED!!!')
        
        # Not worldChild ex: "|__CAMERA__|SH054_CAM:camera_rig|SH054_CAM:rig_extra|SH054_CAM:aimLine"
        #     WorldChild ex: "|__SET__" 

        longName = self.longName
        tokens = longName.lstrip('|').split('|')
        if len(tokens) == 1:
            # World child
            return None
        else:
            # The first token is the rootParent and being top root, there's no DAG ambiguity
            rootParent = MuNode('|' + tokens[0])
            return rootParent    



    def isInstanced(self, indirect=False):
        """
        NOTE 

          Every DAGNode (except lights) can be instantiated! 
          - Transforms, joints, constraints...
          - Cameras, meshes, nurbsCurve, locators...

          But remember:
          - LIGHTS CANNOT BE INSTANTIATED!!!
        """        
        return self._apiObj.isInstanced(indirect)



    def longName(self):
        return self._apiObj.fullPathName()

        

    def name(self): 
        return self._apiObj.partialPathName()



    def shortName(self): 
        return self._apiObj.name()




    """ If I am not wrong, the 'visibility' is present on every derived of DagNode """
    def hide(self):
        """
        A simple shortcut; note that it works on self, not on it's descendants
        myNode.hide()
        myNode.mesh().hide()
          VS
        myNode.visibility.set(False)
        """
        MC.setAttr(self.name() + '.visibility', False)
        return self


    def show(self):    
        MC.setAttr(self.name() + '.visibility', True)
        return self




class Transform(DAGNode):
    """
    matrix = SP^-1 * S * SH * SP * <SPT> * RP^-1 * RA * R * RP * <RPT> * T

    <RPT> = Rotate pivot correction.
            Used when moving the rotate pivot point without 
            affecting the overall transformation matrix.
    <SPT> = Scale pivot correction. 
            Used to moving the scale pivot point without 
            affecting the overall transformation matrix.

    transMinusRotatePivot (tmrp)    
      Attribute to extract the offset of the translation from 
      the rotate pivot. The offset is in the same transformation 
      space as the translate attribute which is parent-space. 
      This value is typically used in expressions where it is subtracted 
      from a position before setting the translation attribute. 
      This causes the object to move so that the rotate pivot point 
      is positioned at the desired position.    

    """


    """=========================================================="""
    """ Only a <transform> (and its derived) can have "children" """
    """ ??? SURE ??? The DAGNodes have children methods...       """
    """=========================================================="""      

    #-----------------------------
    # STATIC/CLASS METHODS
    #-----------------------------
    @staticmethod    
    def create(**kwargs):
        # myTrans = Core.Transform.create(name='myName', parent=parentObj)
        """
        CommandEngine kargs:
          n  name 
          p  parent  --> <str>|<DAGNode>
          s  shared 
          ss skipSelect=True

        TO DO: Extra kwargs   
          t  translation
          r  rotation
          s  scale
          ws worldSpace
        """
        

        # Set 'skipSelect=True' as default
        kwargs['skipSelect'] = kwargs.pop('skipSelect', kwargs.pop('ss', True))
        

        # Allow a MuNode as a parent
        parent = kwargs.pop('parent', kwargs.pop('p', None))
        if parent is not None:
            kwargs['parent'] = nodeName(parent)


        newNodeName = MC.createNode('transform', **kwargs)
        return MuNode(newNodeName)



    #-----------------------------
    # INITIALIZER
    #-----------------------------  
    def __init__(self, mObject, mFn):
        printDebug('Transform.__init__')        
        super(Transform, self).__init__(mObject, mFn)


 
    #-----------------------------
    # METHODS
    #-----------------------------
    def children(self, **kwargs):
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        Argumetns to add:
        - FILTERING:         nameFilter=REGEXP
        - MULTIPLE TYPES:    type=[type1, type2, ...]
        - TYPIZEDTRANSFORMS: 'pureTransform', 'meshTransform', 'nurbsTransform', 'XXXTransform'

        Ex:
        node.children(type='meshTransform')
        node.children(type='locatorTransform')
        node.children(type='ShittyNodeTypeTransform')

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


        """
        Recycle the syntax of 'listRelatives(children=True, ...)'
        and correct the type/noIntermediate bug!
        """
        type_flag  = kwargs.get('type', kwargs.get('t', None))

        typizedTransform_flag = None
        if 'Transform' in type_flag:
            typizedTransform_flag = type_flag.replace('Transform', '')
            type_flag = 'transform'


        nameFilter = kwargs.get('nameFilter', kwargs.get('nf', None))

        if not type_flag:
            children = MC.listRelatives(self.name(), children=True, path=True) or []
        else:
            children = MC.listRelatives(self.name(), children=True, type=type_flag, path=True) or []

        if nameFilter is not None:
            """ --> Here you should put a regExp; like this is too harsh and limited <--""" 
            children = [x for x in children if nameFilter in x]

        if typizedTransform_flag is not None:
            children = [x for x in children if MuNode(x)._isTypedTransform(allowedType=typizedTransform_flag)]

        return List(children)






    def shapes(self, **kwargs):
        """ Return the shape children """
        # --> DO A BETTER WRAP
        shapes = MC.listRelatives(self.name(), children=True, shapes=True, path=True) or []
        
        # Does the flag work for shapes?                                                                      
        #if noIntermediate:
        #    meshChildren = [x for x in meshChildren if MC.getAttr(x + '.intermediateObject') == 0]
        
        return List(shapes)





    def incapsulate(self, capsuleName):
        """
        Create a new transform, holder of self.
        Ex:
         capsule = trans.incapsulate('myCapsule')
        """
        capsule = DGNode.create(nodeType='transform', name=capsuleName)
        parent = self.parent()


        if parent is not None:
            # Move the capsule at the same hierarchy position of node
            capsule.setParent(parent)


        # Copy all the transform values (pivots and compensation included) 
        """ the matrix is the result of these parameters; if you copy 
            the matrix I don't know it's a brutal copy (dataloss) or 
            if it copies all the info needed... """
            
        transformAttributes = [
            'translate', 
            'rotate', 
            'scale', 
            'shear', 
            'rotateOrder', 
            'rotateAxis',                       
            'inheritsTransform', 

            'rotatePivot', 
            'rotatePivotTranslate', 
            'transMinusRotatePivot',                        
            'scalePivot', 
            'scalePivotTranslate', 
        ]
        MC.copyAttr(self.name(), capsule.name(), values=True, attribute=transformAttributes)


        # This is enough to match the TRS, but not the pivots
        self.setParent(capsule, absolute=True) 
        # Reset all pivots included compensation
        MC.xform(self.name(), zeroTransformPivots=True)

        # Fluency
        """ It must return the capsule, NOT self """
        return capsule





    def mesh(self):
        """
        If nothing is found, returns None!
        If multiple meshes are present, it doesn't give a fuck: you get the first one!
        """
        try:
            return self.meshes()[0]
        except IndexError:
            return None

        



    def meshes(self, noIntermediate=True):
        """
        If nothing is found, returns []
        (to allow void loops, e.g. for x in node.meshes():...)
        """        
        # Probably useless... we return a list of Wrappers
        meshChildren = MC.listRelatives(self.name(), children=True, type='mesh', path=True) or []
                                                                               
        if noIntermediate:
            meshChildren = [x for x in meshChildren if MC.getAttr(x + '.intermediateObject') == 0]
        
        return List(meshChildren)



        

    def setParent(self, parent=None, absolute=True):
        """
        ---------------------------------------------------------------------------
        DESCRIPTION 
          BlahBlahBlah...

        
        ARGUMENTS  
          parent = None <str>|<MuNode>
            Accepts a name or a MuNode. 
            setParent([absolute=<bool>]) unparents the node to world (absolutely or not)

          absolute = True <bool>
            True  -->  Preserve world matrix
            False -->  Preserve local matrix (it's gonna jump)
        

        RETURN
          self For fluency


        NOTES
          - The flags 'absolute' and 'relative' are valuelessin Mel; hence in 
            Python 'absolute=False' means 'flag absent', NOT '-relative';
          - Probably something difefrent happens for joints.. check that out!  
        ---------------------------------------------------------------------------
        """

        '''
        FLAGS TO DO
        NOTE: If the object to parent is a joint, it will alter the translation and 
              joint orientation of the joint to preserve the world object transformation 
              if this suffices. Otherwise, a transform will be inserted between the joint 
              and the parent for this purpose. In this case, the transformation inside 
              the joint is not altered. [default]
        - add an 'index' flag: first children, last children, relative position
        
        INHERITANCE
        - Every shape has the right to be reparented... Move this in DAGNode
        '''
        
        if parent is not None:
            # Note the use here of 'MuCore.nodeName(obj)' to allow <str> and <MuNode>
            MC.parent(self.name(), nodeName(parent), absolute=absolute, relative=not absolute)
        else:
            # Reparent to the world
            MC.parent(self.name(), world=True, absolute=absolute, relative=not relative)

        return self






'''
======================================================
Mesh shit...
======================================================
# Is a list 'subset' of another list:
#   [CYCLE STYLE] if all(item in list1 for item in list2): ...
#   [ SET  STYLE] if set(list1).issubset(list2): ...

class Mesh(object):
    _smoothDefault = {
       'smoothLevel': 2, 
       'displayType': 'shit', 
       'renderSmoothLevel': 2
    }
    def smooth(self, **smoothKwargs):
        #if not all(key in Mesh._smoothDefault for key in smoothKwargs):
        if not set(smoothKwargs).issubset(Mesh._smoothDefault):
            print 'shitty arg'
            return
        originalSmooth = Mesh._smoothDefault.copy() # This shallow copy is indeed a deep copy
        originalSmooth.update(smoothKwargs)
        print originalSmooth
      
x = Mesh()
x.smooth(smoothLevel='SHIT') 
'''
class Mesh(DAGNode):
    #-----------------------------
    # INITIALIZER
    #-----------------------------
    def __init__(self, mObject, mFn):
        printDebug('Mesh.__init__')        
        super(Mesh, self).__init__(mObject, mFn)



    #-----------------------------
    # METHODS
    #-----------------------------

    # Default values
    _smoothMeshAttributes = {
        'displaySmoothMesh':         0,
        'smoothMeshSelectionMode':   0,
        'useGlobalSmoothDrawType':   True,
        'smoothDrawType':            2,
        'displaySubdComps':          False,
        'smoothLevel':               2,
        'useSmoothPreviewForRender': True,
        'renderSmoothLevel':         2
    }





    def mesh(self):
        # To simplify loops
        return self



    def smoothMeshDict(self):
        smoothDict = {}
        for attr in Mesh._smoothMeshAttributes:
            smoothDict[attr] = MC.getAttr(self.name() + '.' + attr)
        return smoothDict    



    def setSmoothMesh(self, *args, **kwargs):
        meshName = self.name

        if kwargs.pop('setDefault', None):
            # Reset default values        
            for attr in Mesh._smoothMeshAttributes:
                MC.setAttr(meshName + "." + attr, Mesh._smoothMeshAttributes[attr])
        
        if kwargs.pop('setZero', None):
            # All to 'zero' (it's legal:)
            for attr in Mesh._smoothMeshAttributes:
                MC.setAttr(meshName + "." + attr, 0)
        
        if len(args) == 1 and isinstance(args[0], dict):
            # args[0] is probably another 'smoothDict': convert it to kwargs and recycle!
            self.setSmoothMesh(**args[0]) 
        else:
            for kwarg in kwargs:
                # Check or not???
                MC.setAttr(meshName + "." + kwarg, kwargs[kwarg])
                # ??? try except???

        return self

            
        # .displaySmoothMesh:
        # 0 --> smoothMeshPreview off
        # 1 --> smoothMeshPreview on: cage + smoothMesh
        # 2 --> smoothMeshPreview on: smoothMesh 

        # .smoothMeshSelectionMode:
        # 0 --> edit: cage
        # 1 --> edit: smoothMesh
        # 2 --> edit: both
        """
        MC.setAttr(meshName + ".useGlobalSmoothDrawType", useGlobalSmoothDrawType) # 0 --> local override
        MC.setAttr(meshName + ".smoothDrawType", smoothDrawType) # 0 --> Maya Catmull-Clark, 1 --> openSubdiv Catmull-Clark

        MC.setAttr(meshName + ".displaySubdComps", displaySubdComps) # Show Display subdivisions on/off
        MC.setAttr(meshName + ".smoothLevel", smoothLevel) # preview division levels 

        MC.setAttr(meshName + ".useSmoothPreviewForRender", useSmoothPreviewForRender) # use preview level for rendering
        MC.setAttr(meshName + ".renderSmoothLevel", renderSmoothLevel) # Render division level
        """



    def shader(self, **kwargs):  
        pass
        """  
        renderLayer_flag = kwargs.get("renderLayer", kwargs.get("rl", "defaultRenderLayer"))
        
        if self.isInstanced():
           MC.error("[FATAL] Instanced, not implemented!")
        """



    def shadingEngine(self, **kwargs):
        """
        FIRST WRAP: it doesn't check anything (e.g. per-component shadingEngines)
        """
        """
        renderLayer_flag = kwargs.get("renderLayer", kwargs.get("rl", "defaultRenderLayer"))
        
        if self.isInstanced():
           MC.error("[FATAL] Instanced, not implemented!")
        """
        
        shadingEngineNames = MC.listConnections(self.name(), source=False, destination=True, type='shadingEngine') or []
        if len(shadingEngineNames) == 0:
            # No shadingEngine connected
            return None
        elif len(shadingEngineNames) > 1:
            # per-component shadingEngines: FATALITY
            MC.error('[FATALITY] Per-component shadingEngines!')       
        else:
            return MuNode(shadingEngineNames[0])









  
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
        # HERE IT'S BETTER TO CALL .sets to build it
        tempName = MC.createNode("objectSet", name=nodeName, skipSelect=True)
        unionSet = ObjectSet(tempName)
        unionSet.add(initialMembers)
        return unionSet
    

    @staticmethod
    def union(setA, setB):
        setA_name = setA._apiObj.name()
        setB_name = setB._apiObj.name()
        union_string = MC.sets(setA_name, union=setB_name)
        
        unionSet = ObjectSet.create(setA_name + "_" + setB_name + "_union", union_string)
        return unionSet


    #-----------------------------
    # INITIALIZER
    #-----------------------------
    def __init__(self, mObject, mFn):
        super(ObjectSet, self).__init__(mObject, mFn)


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
        
        setName = self._apiObj.name()
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
        setName = self._apiObj.name()
        MC.sets(clear=setName) # Another wonderful syntactic abomination
        return self


    def members(self):
        setName = self._apiObj.name()
        # Another wonderful syntactic abomination
        # But luckily, it returns shortNames and namespaces
        memberNames = MC.sets(setName, query=True) or [] 
        return List(memberNames)
    

    def _memberNames(self):
        setName = self._apiObj.name()
        return MC.sets(setName, query=True) or [] 
       

    def has(self, other):
        setName = self._apiObj.name()
        other_name = None        
        if issubclass(type(other), Wrapper):
            other_name = other.shortName
        if isinstance(other, str):
            other_name = other    
        return MC.sets(other_name, isMember=setName)
               




#---------------------------------------------------------------
# NOT REALLY NECESSARY IN THE END... add it, but it's SECONDARY 
#---------------------------------------------------------------
""" EASY-CONNECT wrappers                                 """
""" just a CREATE who allows to connect directly plugs    """
""" """
""" YOU SHOULD WRAP BETTER THE TYPE from MuNode           """

'''
class MultiplyDivide(DGNode):
    """
    MultiplyDivide.create('factor',
        input1X=myPlug
        input2X=myPlug2
        outputX=exit, 
        operation='divide'
    )
    """
    @staticmethod
    def create(name):
        inputPlugs = {
            'input1X': 0, 
            'input1Y': 0, 
            'input1Z': 0, 
            'input2X': 1,
            'input2Y': 1, 
            'input2Z': 1
        }
        outputPlugs = ('outputX', 'outputY', 'outputZ')
        
class AddDoubleLinear(DGNode):
    pass

class PlusMinusAverage(DGNode):    
    pass
'''




#============================================================================== 
#
# MuIterables:
#  - MuCore.List
#  - MuCore.Set
#
# Wraps of <list> and <set> compatible with DGNodes ans 'massive methods'
#------------------------------------------------------------------------------
# Everything works seamlessly:
#   s1 = Set(a, a, b, b, c, d, e)   
#   s2 = Set([a, a, b, b, c, d, e])
#   s3 = Set(List(a, a, b, b, c, d, e))
#   l1 = List(s1)   
#============================================================================== 

class List(list):
    def __init__(self, *args):
        """
        List(name1, name2, ...)
        List([name1, name2, ...])
        """
        if len(args) == 1:
            # nodeList = List(a, b, c, ...) (list() takes at most one arg!)
            args = [MuNode(x) for x in args[0]]
        else:
            args = [MuNode(x) for x in args]    
        super(List, self).__init__(args)


    def append(self, newObj):
        """
        Only DGNode-able objects

        myMuList.append('nodeName')
        myMuList.append(node)
        """
        if isinstance(newObj, basestring) or issubclass(type(newObj), DGNode):
            super(List, self).append(MuNode(newObj))
        else:
            raise Fatality('LIST APPEND ERROR', 
                           '<List> accepts only <DGNodes>: the object "{0}" is of {1}!'.format(newObj, type(newObj)))

    
    def __setitem__(self, position, newObj):
        """
        Only DGNode-able objects
        """
        if isinstance(newObj, basestring) or issubclass(type(newObj), DGNode):
            super(List, self).__setitem__(position, MuNode(newObj))
        else:
            raise Fatality('LIST SET ERROR', 
                           '<List> accepts only <DGNodes>: the object "{0}" is of {1}!'.format(newObj, type(newObj)))




class Set(set):
    def __init__(self, *args):
        if len(args) == 1:
            # nodeSet = Set(a, b, c, ...) (set() takes at most one arg!)
            args = [MuNode(x) for x in args[0]]
        else:
            args = [MuNode(x) for x in args]    

        super(Set, self).__init__(args)        
    





def registerMassiveMethods(muIterableClass, classToScan):
    """
    ??????????????????????????????????????????????????????????????????????????
    After @property, we loose a method and get a 'property' object, hence:
    CANT WRAP @property METHODS... there's non __name__ etc ect
    https://docs.python.org/3/library/functools.html#functools.wraps

    ??????????????????????????????????????????????????????????????????????????
    """

    """
    Inspects 'classToScan' (a derived of <MuNode>) and gathers all the methods 
    marked with a "_isMassive" attribute; then adds a method of the same name 
    to the 'muIterableClass' passed (List or Set)

    The MuIterables must be the last defined; then call registerMassiveMethods(...)
    """

    print 'Scanning {} for massive methods:'.format(str(targetClass))


    massiveMethods = []
    for x in dir(targetClass):

        # Avoid magic/private methods
        if x.startswith('_'):
            continue

        element = getattr(targetClass, x)
        # "_isMassive" is just a TAG... no need for a value!
        if hasattr(element, '_isMassive'):
            print " - '{}' is massive!".format(element.__name__)
            massiveMethods.append(element) 
    

    def methodMassivizer(originalMethod, self, *args, **kwargs):
        # A bundle is just a wrapped list of DGNodes; hence a massive method should
        # try to return a classic list (probably a list of Nones)
        result = []
        for obj in self._objectList:
            # ??? use 'issubclass()' to inherit baseClasses methods

            if isinstance(obj, targetClass):
                result.append(originalMethod(obj, *args, **kwargs)) 
            else:
                # Raise a 'Bundle disomogeneity'
                MC.error('Bundle error!')
        
        return result    
                
    for method in massiveMethods:
        temp = types.MethodType(functools.partial(methodMassivizer, method), None, Bundle)
        setattr(Bundle, method.__name__, temp) 
        # Add an updated __doc__, ex:
        # new.__doc__ = "Massive method\n" + old.__doc__       





"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Add the 'massive' methods to MuIterable classes
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# registerMassiveMethods(List, DGNode)
# registerMassiveMethods(Set,  DGNode)


















"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
===============================================================================================================================================
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

MINI FACTORIES

_______________________________________________________________________________________________________________________________________________
===============================================================================================================================================
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""






class MuNode(object):
    """
    DESCRIPTION
      Main wrapper for Maya nodes.
      If the type has not a specific wrapper, regress to a generic DependencyNode
      (or a generic MFnDagNode, even if abstract??? Ex: constraints, locator, 
       annotations, SHAPES in general...) 

    """
    


    # DependencyNode (generic)
    # |
    # +--DagNode (abstract)
    # |  |
    # |  +--Mesh    
    # |  |
    # |  +--Transform
    # |
    # +--Reference
    # |
    # +--ObjectSet

    wrappedNodeTypes = {
        # apiType                functionSet,     wrapperClass 
        OM.MFn.kTransform:      (OM.MFnTransform, Transform),
        OM.MFn.kMesh:           (OM.MFnMesh,      Mesh),
        OM.MFn.kSet:            (OM.MFnSet,       ObjectSet),
        OM.MFn.kReference:      (OM.MFnReference, Reference)
    }


    #-----------------------------
    # CONSTRUCTOR
    #-----------------------------
    def __new__(cls, nodeArg):
        """
        ---------------------------------------------------------------------------          
        DESCRIPTION                


        ARGUMENTS
          nodeArg <str>|<DGNode derived>
            MuNode('nodeName')  --> wrappedNode  (creates the wrapper)
            MuNode(wrappedNode) --> wrappedNode  (just another bound name)


        RETURN <DGNode derived>    
        ---------------------------------------------------------------------------
        """

       
        """ 
        ?????????????????????
        ==> NOTE: probably it should be up to the DGNode class to create the proper 
                  MFn* by sending only the MObject... I just wanna do the type check
                  ONLY ONCE, NOT TWICE!!!
        ?????????????????????
        """          

        #---------------------------------------------------------
        # It's already a wrappedNode (i.e. derived from DGNode)
        #---------------------------------------------------------
        if issubclass(type(nodeArg), DGNode):
            return nodeArg
        


        #---------------------------------------------------------
        # It's probably the name of a Maya node
        #---------------------------------------------------------
        selList = OM.MSelectionList()
        try:
            # The API method .add fails if node doesn't exist or there's 
            # a DAG ambiguity, but MC.objExists doesn't in case of ambiguity!!!
            selList.add(nodeArg)     

        except:
            """ AVOID BARE EXCEPT as a rule! """
            # 'nodeArg' is not bound to a Maya node...
            # It could be an attribute??? No idea 
            raise NameFatality(nodeArg)  
        
        mObject = OM.MObject()
        selList.getDependNode(0, mObject)

        try:
            mFn = MuNode.wrappedNodeTypes[mObject.apiType()][0]()
        except KeyError: # <-- This is a nice EAFP (NOT a bare silly 'except:'')
            # It's not a wrapped type
            if mObject.hasFn(OM.MFn.kDagNode):
                # It's a DagNode derived
                mFn = OM.MFnDagNode()
                return DAGNode(mObject, mFn)
            else:
                # It's a generic dependency node
                mFn = OM.MFnDependencyNode()
                return DGNode(mObject, mFn)   

        # Now call the __init__ of the right class
        return MuNode.wrappedNodeTypes[mObject.apiType()][1](mObject, mFn)









class MuPlug(object):
    """
    Getters:
      node.plug.get(*args, **kwargs)

    Setters:
      node.plug.set(<value>  [, **kwargs])
               .set(<DGNode> [, **kwargs])
               .set(<MuPlug> [, **kwargs])
               .set(<string> [, **kwargs])



    Array:
      node.arrayPlug
      node.arrayPlug[i] --> node.arrayPlug.__getitem__(i)

    [TO DO] Compounds:
      node.parentPlug
      node.parentPlug.childPlug --> node.parentPlug.__getattr__('childPlug')

    >>> This will become legal:
        - cam.renderLayerInfo[0].renderLayerId
          i.e. cam.renderLayerInfo.__getitem__(0).__getattr__('renderLayerId')
        - sphere.t.tx
        - cam.boundingBox.boundingBoxMin.boundingBoxMinX



    Connectors (force=True):
      <MuPlug> >> <MuPlug>
      <MuPlug> << <MuPlug>
      <MuPlug> >> <string>
      <string> << <MuPlug> (??? Is it possible???)

      Allow fluency:
      plug1 >> plug2 >> plug 3

    """

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    TO DO:

    This is really heavy:
    - newController.rz.setLocked().setVisible(False) # .lock().hide()
    - newController.ry.setLocked().setVisible(False)
    - newController.rz.setLocked().setVisible(False)

    If possible, replace with this:
    - INVALID SYNTAX newController.('rx', 'ry', 'rz').lock().hide()
    - newController.getPlugs('rx', 'ry', 'rz').lock().hide()

    - myNode.getPlugs('plug1', 'plug2', ...) --> <List> or <PlugList>
    Note that we're gonna need MASSIVES!!!

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


    def __init__(self, plugArg):
        """
        DESCRIPTION 
          The public initializer/binder:
          myWrappedPlug = MuPlug('myNode.myPlug')


        ARGUMENTS
          plugArg <MPlug>|<string>
        """
        if isinstance(plugArg, OM.MPlug):
            # <MPlug> passed: private initializer    
            self._mPlug = plugArg

        else:
            # <string> passed: public initializer    
            # 'nodeName.plugName*'
            selList = OM.MSelectionList()
            try:
                selList.add(plugArg)
                mPlug = OM.MPlug()
                selList.getPlug(0, mPlug)                
            except:
                # '.add' and '.getPlug' can both fail (ex, you passed a 
                # name of a node, not of a plug)... Not really important!
                MC.error('The name "{}" can\'t be bound to an existing plug!'.format(plugArg))

            self._mPlug = mPlug







    def __rshift__(self, other):
        """
        <MuPlug> >> <MuPlug>|<string>|<iterable of <MuPlug>s>

        Ex:
        - myNode.myPlug >> otherNode.otherPlug
        - myNode.myPlug >> 'pippo.tx'
        - myNode.myPlug >> node1.plug1, node2.plug2, ...

        """


        """ IT DOESN'T WORK WITH STRINGS... only wuth <MuPlugs> """
        selfPlugName  = self.name()


        if not isinstance(other, (List, Set, list, set, tuple)):
            """ For the moment it's just a MuPlug   """
            """ (don't forget to extend to strings) """
            plugIterable = [other]
        else:
            plugIterable = other


        for plug in plugIterable:
            plugName = plug.name()
            try:
                MC.connectAttr(selfPlugName, plugName, force=True)            
            except RuntimeError:
                # Exception to swallow: "Warning: 'xxx.aaa' is already connected to 'xxx.yyy'."
                # Unluckily, it raises the same exception 'RuntimeError' than 'locked attribute' 
                if MC.isConnected(selfPlugName, plugName, ignoreUnitConversion=True):
                    # It will nonetheless show the 'warning', but swallow the exception
                    pass
                else:
                    # A genuine error: reraise!
                    raise    
        
        # As concerning 'fluency':
        # - for a 'simple' connect return  the last MuPlug (ex: a.tx >> b.sx >> c.rx >> ...)
        # - for a 'massive' connect return None
        return other





    def __lshift__(self, other):
        # self << other
        MuPlug.__rshift__(other, self)

        # Allow fluency (a.tx << b.sx << c.rx << ...)
        return other





    def __getitem__(self, index):
        """
        ---------------------------------------------------------------------------
        DESCRIPTION
          Access to the itemPlugs of an arrayPlug:
            myNode.myArrayPlug
            myNode.myArrayPlug[i] --> myNode.myArrayPlug.__getitem__(i)

        RETURN <MuPlug>
        ---------------------------------------------------------------------------
        """
        if not self._mPlug.isArray():
            MC.error(self.name() + ' is not an array plug!')

        """ >>> A little of safety wouldn't bad at all:) <<< """
        # logicalIndex == the sparse index (used by the commandEngine)
        return MuPlug(self._mPlug.elementByLogicalIndex(index))    





    """ 
     ||
    \  /
     \/
    Don't EVER catch with 'except Exception as ...'!!!   
    CATCH EXACTLY WHAT YOU NEED BUT NOT EVERYTHING
    EAFP: it's (E)asier to (A)sk for (F)orgiveness than (P)ermission
    But a bare except is simply STUPID
    """
        
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #
    # plugName = nodeMinimalName . attributeName    
    #            |root|superNode . myAttr
    #
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



    def nodeName(self):
        """
        AND WHAT HAPPENS IF THE POINTER HAS BECOME INVALID???
        """
        mObj = self._mPlug.node() # --> MObject

        if mObj.hasFn(OM.MFn.kDagNode):
            # It's a DagNode: recover its minimal name
            ptr = OM.MFnDagNode(mObj)
            return ptr.partialPathName()

        else:
            ptr = OM.MFnDependencyNode(mObj)
            return ptr.name()    


        '''
        NO: YOU NEED TO PASS FOR THE MFN; or on creation put a reference to the original node
        try:
            # It's a Dag
            return mObj.partialPathName()
        except AttributeError:
            # 
            return mObj.name()
        '''
        #if mObj.hasFn(OM.MFn.kDagNode):
        #    # It's a DagNode: recover its minimal name
        #    ptr = OM.MFnDagNode(mObj)
        #    return ptr.partialPathName()
        #else:
        #    return ptr.name() 



    def node(self):
        # Return the MuNode of this plug
        """ HORRID """
        return MuNode(self.nodeName())


    def attributeName(self):
        """ (object)--(class) is like (plug)--(attribute)  """
        return self._mPlug.partialName()


    def name(self):
        # Can't find a way to get the complete plug name in case of 
        # Dag ambiguity; am I missing something?
        return self.nodeName() + '.' + self.attributeName()  


    def type(self):
        return MC.getAttr(self.name(), type=True)




    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #skipConversionNodes=False scn
    #shapes=False sh
    #nodeType = type
    #exactType =
    #connections =




    def inputPlug(self, **kwargs):
        """ 
        WHAT HAPPENS FOR AN ARRAY/COMPOUND PLUG??? 
        ------------------------------------------
        Could this return a list of plugs???
        """

        """ ==> Caso facile, a 'simple' plug (not array or compound) """
        type_               = kwargs.get('t',   kwargs.get('type',                ''))
        exactType           = kwargs.get('et',  kwargs.get('exactType',           False))
        skipConversionNodes = kwargs.get('scn', kwargs.get('skipConversionNodes', False))
        
        inputPlugNames = MC.listConnections(
            self.name(), 
            source=True, 
            destination=False, 
            plugs=True, 
            type=type_, 
            exactType=exactType,
            skipConversionNodes=skipConversionNodes
        ) or []

        if len(inputPlugNames) == 0:
            # No input plug
            return None 
        elif len(inputPlugNames) > 1:
            # NOT IMPLEMENTED (array or compounds???)
            MC.error('COMPOUND or ARRAY')    
        else:
            # Return a MuPlug
            # (Apparently <MPlug> has a way to get all plug connected, but then it's
            #  up to you to filter them...)
            return MuPlug(inputPlugNames[0])



    """
    def outputPlugs(self, type=None, exactType=None, shapes=True, skipConversionNodes):
        kwargs.pop(kwargs.pop(p, True))
        outputPlugNames = MC.listConnections(
            self.name(), 
            source=False, 
            destination=True, 
            plugs=True,
            type=???, 
            exactType=???, 
            shapes=???,
            skipConversionNodes=???
        ) or []
    """    






    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>





    def get(self):
        return MC.getAttr(self.name())


    def set(self, *args, **kwargs):
        """
        .set(<value>|<DGNode>|<MuPlug>|<str> [, **kwargs])
        
        myNode.myPlug.set(69.69)               --> Direct mutation
        myNode.myPlug.set(otherNode)           --> Check if otherNode has the same plug and copies its value
                                                   (it should copy even the eventual incoming connection....)
        myNode.myPlug.set(otherNode.otherPlug) --> MuPlug Syntax
        myNode.myPlug.set('node2.fuck')        --> String syntax

        """
        plugName = self.name()
        plugType = self.type()


        #--------------------------------------
        # Syntax: myNode.myPlug.set(<DGNode>)
        #--------------------------------------
        if len(args) == 1 and issubclass(type(args[0]), DGNode):
            # Only one positional argument which is a DGNode
            #args = [MC.getAttr(args[0].name() + '.' + self.attrName)]
            args = [args[0].getPlug(self.attributeName()).get()]


        if plugType == 'string':
            # 'string' attributes need a special syntax
            MC.setAttr(plugName, *args, type='string')
        else:
            MC.setAttr(plugName, *args)     
        

        # Enable fluency
        return self




    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    HUGE WARNING...
    Check the API doc, because you haven't yet undestood what 
    - keyable
    - visible
    - locked
    - channelbox 

    mean... it's slightly more confused than this shit!!!
    "Being non-keyable is not a hard block against adding keys to an attribute."
    ChannelBox flag "Sets whether this plug is displayed in the channel box. This overrides the 
    default display of a plug set with MFnAttribute::setChannelBox. Keyable attributes 
    are always shown in the channel box so this flag is ignored on keyable plugs."

    
    So, LOCKED and CHANNELBOX are only visual gimmicks, not real constraints

    KEYABLE (not a real block, just a gimmick of the channelBox)
    - A 'nonKeyable' plug can still have an animation connected... 
    - credo che sia solo una questione di channelBox, per impedire che il set key 
      ci metta sopra un'animawione... ma puoi connetterci o meno una curva d'anim
      a prescindere che sia 'keyable' or not...
    
    LOCKED (a True block)
    - a locked attribute cant have incoming connections
    - In reality, LOCK means that the plug 'value' can't be altered:
      1'  if the plug had no incoming connection, it's static value its unmodifiable
      2'  if the plug was connected, nothing change. BUT THE CONNECTION CAN'T BE BROKEN
    
    - LOCKED blocks every -->INPUT<-- deconnection, reconnection, manual set Key...
      It's BLOCKING!!!
    
    - but LOCKED doesn't do anything to the OUTPUT connections!


    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    IT'S MORE RELATED TO THE PLUG MUTABILITY (LOCKED PLUG <==> a tuple is immutable):
    - if it's a pure value, it can't change
    - if it derives from a connection, it's teh connection that can't be broken, 
      BUT THE VALUE WILL CHANGE (exactly as in a tuple holding mutable and immutable objects in Python)
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


    --> SO, LOCKED is indeed the IMMUTABILITY for the plug (value or connection)
        (a LOCKED plug can change it's value if it was connected to something before
         the locking...) 

    NOTE THAT THIS IS PLAIN UTTERLY FALSE:
    "LOCKED: Sets the locked state for this plug's value. A plug's locked 
    state determines whether or not the plug's value can be changed."

    Seriously autodesk...


    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    """
    plug.setLocked(True)
    # Even if there's a link between visible and keyable, try to limit the shit
    plug.setVisible(False)
    plug.setKeyable(True) # --> it's visible
    plug.setKeyable(False) # --> it stays visible if it was visible!!!

    # Visible + Unkeyable:
    MC.setAttr('null1.XXX', keyable=False, channelBox=True)

    # Visible + Keyable:
    MC.setAttr('null1.XXX', keyable=True) # The channelBox flag is ignored on keyable attributes. 

    # Invisible
    MC.setAttr('null1.XXX', keyable=False, channelBox=False)
    """



    def isLocked(self):
        return self._mPlug.isLocked()

    def setLocked(self, lockStatus=True):
        """
        plug.setLocked() --> it's locked!
        """
        self._mPlug.setLocked(lockStatus)
        return self



    def isKeyable(self):
        return self._Mplug.isKeyable()

    def setKeyable(self, keyableStatus=True):
        if keyableStatus:
            self._mPlug.setKeyable(True)
            self._mPlug.setChannelBox(True)
        else:
            self._mPlug.setKeyable(False)
            self._mPlug.setChannelBox(True)        
        return self    



    def isVisible(self):
        return self._mPlug.isChannelBoxFlagSet()
    
    def setVisible(self, visibleStatus=True):
        print 'NOT IMPLEMENTED, no idea...'
        #oldKeyableStatus = self._mPlug.isKeyable()
        return self


    """ BETTER AND EASIER """
    #----------------------------------
    def lock(self):
        self._mPlug.setLocked(True)
        return self
  

    def hide(self):
        self._mPlug.setChannelBox(False)  
        self._mPlug.setKeyable(False) 
        return self


    def unlock(self):
        pass  
    def show(self):
        pass
    def keyable(self):
        pass
    def unkeyable(self):
        pass            
    #----------------------------------


    def __call__(self, *args, **kwargs):
        """ NOT REALLY NECESSARY """
        # myShit.sx(999, ws=True)  -->  myShit.sx.set(999, ws=True)
        pass

     






class MuSignal(object):
    """
    RULES
    - if an object 'myObj' has a MuSignal 'mySignal' you can connect outside it with:
        myObj.mySignal.connect(callback)
        myObj.mySignal.connect(callback, isGeneric=False)
      The first sintax is a 'generic' connect; the callback can't recover myObj;
      with the secon syntax, mySignal will call (when myObj emit mySignal) the callback
      by adding a new kwarg 'MuEmitter=myObj'. Thus the callback must have a signature
      that accepts it, ex:
        myCallback(...., MuEmitter=None)

    - inside myObj there are two ways to emit a MuSignal:
        self.mySignal.emit(...)
        self.mySignal.emit(..., MuEmitter=self)
      It's up to the .connect to specify with the 'isGeneric' if the callback 
      desires to receive the caller object. 
      A callback who wanna know the emitter object, must add to its signature:
        def curiousCallback(*args, MuEmitter=None, **kwargs): ...

    """

    # QtSIGNALS AS CALLBACK CONTAINERS (INTERFACE)
    #-------------------------------------------------------------------
    # A 'Signal' is simply a 'callback container'!
    # It allows to add callback from the outside of the object.
    # Then, something inside may 'emit' it and the <SignalInstance>
    # calls all the added callbacks
    #
    # YOU CAN ADD/REMOVE CALLBACKS FROM OUTSIDE
    # (but somebody inside the object must ask the container to execute)
    #
    # It's "reason d'etre" is the ability to add callbacks from the 
    # outside. When you wanna react to an event occurring in an object
    # (implemented, by a cutom signal and the proper emission) you just
    # do:
    #  
    #  (OUTSIDE) myObj.customSignal.connect(myCallback)
    #   (INSIDE) myObj.customSignal.emit()
    #
    #  myObject.visibilityChanged.connect(interestedObj1.setVisibility)
    #  myObject.visibilityChanged.connect(interestedObj2.setVisibility)
    #
    #  Inside myObject, somebody will call 
    #  
    #  self.visibilityChanged.emit(True)
    #  self.visibilityChanged.emit(True)
    #  
    #  The methods put into .connect(...) can be predefined slots or 
    #  whatever is callable and respect the signal signature
    # DOC: 
    # mySignal() --> emitted when the object does...

    # It belongs to the object interface and you don't need to know
    # its inner implementation (but don't forget that something inside
    # the object will have to talk to the callback container, 
    # i.e. 'emit' the 'signal')


    def __init__(self):
        # self._callbackList = [
        #     {'funcObj': <funcObj>,      'isGeneric': <bool>},
        #     {'funcObj': myCallbackObj1, 'isGeneric': True}, 
        #     {'funcObj': myCallbackObj2, 'isGeneric': False}, 
        #     ...
        # ]
        self._callbackList = []



    def emit(self, *args, **kwargs):
        for callback in self._callbackList: 
            # Check if the emitter has to be sent
            if callbackPair['isGeneric']:
                kwargs.pop('MuEmitter')

            callback(*args, **kwargs)


            
    def connect(self, funcObj, isGeneric=True):
        self._callbackList.append({'funcObj': funcObj, 'isGeneric': isGeneric})



    def listConnections(self):
        pass


    def hasCallback(self, callbackId):
        callbackFound = False
        for callback in self._callbackList.keys():
            callbackObj = callback['funcObj']
            # Check if the funcObj is found, by obj or by name
            if callbackId in (callbackObj, callbackObj.__name__):
                callbackFound = True
                break
        
        return callbackFound                



    def disconnect(self, callbackId):
        """
        ----------------------------------------------------------
        DESCRIPTION


        ARGUMENTS
          callbackId <funcObj>|<str>
            myObj.mySignal.disconnect(funcObj)
            myObj.mySignal.disconnect('funcName')    
        ---------------------------------------------------------
        """
        if self.hasCallback(callbackId):
            self._callbackList.pop(callback)






class Namespace(object):
    def __init__(self, namespaceName):
        self._namespace = namespaceName 



    def __repr__(self):
        """
        -------------------------------------        
        repr(obj)  <-->  obj.__repr__()
        -------------------------------------        
        I don't care about 'eval'; I use __repr__ for easy console log!
        """
        # A more informative representation
        return '"{}"<Namespace>'.format(self._namespace)    



    def __str__(self):
        """
        -------------------------------------
        str(obj)  <-->  obj.__str__()
        -------------------------------------
        This is used to avoid clumsy:
         - ref.namespace().name()
         - ref.namespaceAsStr()
        
        A simpler:
         - str(ref.namespace())
        """
        return self._namespace



    def nodes(self):
        nodes = MC.namespaceInfo(self._namespace, listOnlyDependencyNodes=True)
        return List(nodes)



    def name(self):
        return self._namespace

    # MC.namespace(rename=['oldNamespace', 'newNamespace'])
    # MC.namespaceInfo(listOnlyDependencyNodes=True) --> get the list of nodes in the current namespace
    # MC.referenceQuery(xxx, nodes=True, dagPath=True) --> get the nodes
    #
    # HERE CHECK IF THE NEW NAMESPACE EXISTS (the '__TEMP__' is to get idempotency)
    # MC.file(fileName, edit=True, namespace='__TEMP__')
    # MC.file(fileName, edit=True, namespace='newNamespace')
    # MC.file(file???, edit=True, namespace='newNamespace'  --> to modify a referenced file namespace (the new one must not exist)


















































#------------------------------------------------------------------------------
# Module loaded!
Utils.moduleLoadedMessage()
#------------------------------------------------------------------------------



























"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
===============================================================================================================================================
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

TO DO...

_______________________________________________________________________________________________________________________________________________
===============================================================================================================================================
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

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
    attrs = MC.listAttr(obj.name(), userDefined=True, string="*")
    attrDict = {}
    for attr in attrs:
        try:
            tipo = MC.getAttr(obj.name() + "." + attr, type=True)
            num = MC.attributeQuery(attr, n=obj.name(), numberOfChildren=True)
            multi = MC.attributeQuery(attr, n=obj.name(), multi=True)
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
        # self._apiObj.name()
        
        # Pointer to the original Maya node
        self._apiObj = OM.MFnDependencyNode(mObj)

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
            raise PlugFatality("flag 'type' (t) is mandatory!")                               
        
        # Just once please (don't trigger API methods for nothing)
        # Here we don't modify the DAG, hence we can revert to the commandEngine
        nodeName = self._apiObj.name() 
        
        if attrType not in Metadata._supportedTypes:
            raise PlugFatality("The attribute type <" + attrType + "> is unknown!")                               
        
        # Check if already exists
        if MC.attributeQuery(attrName, node=nodeName, exists=True):
            raise PlugFatality("MayaNode " + nodeName + " has already a <metaAttribute> named " + attrName)  
        
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
        nodeName = self._apiObj.name()
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
        nodeName = self._apiObj.name()
        
        metaAttrs = MC.listAttr(nodeName, userDefined=True, string="META_*") or []
        result = {}
        for attr in metaAttrs:
            plug = nodeName + "." + attr
            # Attribute type (string)
            attrType = MC.getAttr(plug, type=True)
            
            # Is it <multi> (type == "TdataCompound")
            isMulti = MC.attributeQuery(attr, node=nodeName, multi=True)
            
            # Is it <compound>? ("TdataCompound" is NOT...)
            #isCompound = MC.attributeQuery(attr, node=self.name(), numberOfChildren=True)
            
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
    attrs = MC.listAttr(obj.name(), userDefined=True, string="*")
    attrDict = {}
    for attr in attrs:
        try:
            tipo = MC.getAttr(obj.name() + "." + attr, type=True)
            num = MC.attributeQuery(attr, n=obj.name(), numberOfChildren=True)
            multi = MC.attributeQuery(attr, n=obj.name(), multi=True)
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
        self._apiObj = OM2.MFnDependencyNode(mObj)
        
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
        return MC.getAttr(self._apiObj.name() + ".samples")


    @samples.setter
    def samples(self, numSamples):
        MC.setAttr(self._apiObj.name() + ".samples", numSamples)


    @property
    def spread(self):
        return MC.getAttr(self._apiObj.name() + ".spread")


    @spread.setter
    def spread(self, spreadValue):
        MC.setAttr(self._apiObj.name() + ".spread", spreadValue)


    @property
    def maxDistance(self):
        return MC.getAttr(self._apiObj.name() + ".max_distance")


    @maxDistance.setter
    def maxDistance(self, maxDistanceValue):
        MC.setAttr(self._apiObj.name() + ".max_distance", maxDistanceValue)


    @property
    def falloff(self):
        return MC.getAttr(self._apiObj.name() + ".falloff")


    @falloff.setter
    def falloff(self, falloffValue):
        MC.setAttr(self._apiObj.name() + ".falloff", falloffValue)


    @property
    def includeExclude(self):
        return MC.getAttr(self._apiObj.name() + ".id_inclexcl")


    @includeExclude.setter
    def includeExclude(self, includeExcludeValue):
        MC.setAttr(self._apiObj.name() + ".id_inclexcl", includeExcludeValue)


    @property
    def nonSelf(self):
        return MC.getAttr(self._apiObj.name() + ".id_nonself")


    @nonSelf.setter
    def nonSelf(self, nonSelfValue):
        MC.setAttr(self._apiObj.name() + ".id_nonself", nonSelfValue)

    @property
    def nonSelf(self):
        return MC.getAttr(self._apiObj.name() + ".id_nonself")


    @nonSelf.setter
    def nonSelf(self, nonSelfValue):
        MC.setAttr(self._apiObj.name() + ".id_nonself", nonSelfValue)





'''

import maya.OpenMaya as OM
mayaState = OM.MGlobal.mayaState()
"""
mayaState() flags:
     maya  0  OM.MGlobal.kInteractive
mayaBatch  1  OM.MGlobal.kBatch
   mayapy  2  OM.MGlobal.kLibraryApp
      ???  3  OM.MGlobal.kBaseUIMode
"""  

# maya.exe -prompt --> MEL command line
# mayabatch.exe    --> maya -batch: open maya, executes a command, close maya
# Render.exe

# maya.exe -log fileFullPath --> stdout and sterr in a chosen file
'''



"""
An instanced node is a SINGLE NODE that is 'pointed' more than once;
But there's ONLY ONE NODE; hence the mObject CAN'T be enough!
YOU NEED THE DAGPATH (there's only ONE node, hence only a real pointer!!!)

Should I really care???
"""
