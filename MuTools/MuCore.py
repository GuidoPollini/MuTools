import MuTools.MuUtils as MUT
reload(MUT)

import maya.cmds         as MC
import maya.OpenMaya     as OM

"""
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








DEBUG = False
def printDebug(*args):
    if DEBUG:
        print '#[DEBUG]',
        for arg in args:
            print arg,
        print    






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



"""
MAYA_TYPES = [
    'kTransform',
    'kMesh'
]
"""

class MuNode(object):
    #-----------------------------
    # CONSTRUCTOR
    #-----------------------------
    
    """
    implementedTypes = {
        'kTransform': Transform
    }   
    """

    def __new__(cls, nodeName):
        printDebug('MuNode.__new__')

        selList = OM.MSelectionList()
        try:
            # The API method .add fails if node doesn't exist or there's 
            # a DAG ambiguity, but MC.objExists doesn't in case of ambiguity!!!
            selList.add(nodeName)     

        except:
            # 'nodeName' is not bound to a Maya node...
            # It could be an attribute??? No idea 
            raise NameFatality(nodeName)  
        
        mObject = OM.MObject()
        selList.getDependNode(0, mObject)
        
        nodeAPIType = mObject.apiTypeStr() 
        
        if nodeAPIType == 'kTransform':
            # A transform
            return Transform(mObject)
        
        if nodeAPIType == 'kMesh':
            # A mesh
            return Mesh(mObject)

        elif mObject.hasFn(OM.MFn.kDagNode):
            # Generic DAGNode
            return DAGNode(mObject)

        else:
            # Generic DGNode    
            return DGNode(mObject)    


            




class DGNode(object):
    """
     .name      =  the minimal unique name
     .longName  =  the full DAGPath

    ... And something you won't really need: 
    .shortName  =  the bare nodeName
    """ 



    #-----------------------------
    # STATIC/CLASS METHODS
    #-----------------------------
    @classmethod    
    def create(cls, *args, **kwargs):
        pass



    #-----------------------------
    # INITIALIZER
    #-----------------------------
    def __init__(self, mObject):
        printDebug('DGNode.__init__')
        # Do you really need these wrappers?
        #   MU.DGNode('woah')
        #   MU.Transform('woah')
        #   MU.Mesh('woah')
        #
        # I prefer a generic wrapper:
        #   MU.MuNode('woah')
        #
        # And for creation these are probably better:
        #      MU.DGNode.create(...)   --> generic
        #   MU.Transform.create(...)   --> with specific arguments
        #        MU.Mesh.create(...)   --> with specific arguments
        
        # Hence, the initializer will accept only an MObject



        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
         <<< THIS IS ATROCIOUS >>>
        the MuNode.__new__ already did this check...

        But it's a fine example: if you respect the interface, you can use it, even if
        it's shitty inside: "IT QUACKS/SHITS LIKE A DUCK, IT'S A DUCK" or:

        <<PROGRAM TO INTERFACES, NOT IMPLEMENTATIONS>>
        <<PROGRAM TO INTERFACES, NOT IMPLEMENTATIONS>>
        <<PROGRAM TO INTERFACES, NOT IMPLEMENTATIONS>>        
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""   

        _type = mObject.apiTypeStr()
        
        if _type == 'kTransform':
            self._pointer = OM.MFnTransform(mObject)
        
        elif _type == 'kMesh':
            self._pointer = OM.MFnMesh(mObject)

        elif mObject.hasFn(OM.MFn.kDagNode):
            self._pointer = OM.MFnDagNode(mObject)

        else: 
            self._pointer = OM.MFnDependencyNode(mObject)
        


        self.type = self._pointer.typeName()

        """
        Here you should check for MObjectHandle... apparently 
        it's more stable and proper!
        """

        """
        Note:
        This is not gonna work with instances. If you save only the pointer, you'll have just a node.
        But since it's shared, all DAG methods (getParent, getChildren) will fail.

        To work with instances, you need to save the DAGPath (of course...)
        """


    #-----------------------------
    # MAGIC METHODS
    #-----------------------------
    def __repr__(self):
        # Format: "name"<Type>
        return '"{0}"<{1}>'.format(self.name, self.type)      




    #-----------------------------
    # METHODS
    #-----------------------------

    @property
    def longName(self): 
        return self._pointer.name()


    @property
    def name(self): 
        # To allow loop on generic nodes and DAGs
        return self._pointer.name()


    @property
    def shortName(self): 
        return self._pointer.name()




 
class DAGNode(DGNode):
    #-----------------------------
    # INITIALIZER
    #-----------------------------       
    def __init__(self, mObject):
        printDebug('DAGNode.__init__')
        super(DAGNode, self).__init__(mObject)
        



    #-----------------------------
    # MAGIC METHODS
    #-----------------------------



    #-----------------------------
    # METHODS
    #-----------------------------
    def getParent(self):
        """ By returning a full-fledged node, there's no need for the 'longName' option! """

        if self.isInstanced():
            # Remember, it fails with instances...
            MC.error('INSTANCED!!!')

        parentList = MC.listRelatives(self.name, parent=True, path=True) or [] 
        try:
            return MuNode(parentList[0])
        except:
            # Child of the world
            return None    



    def isInstanced(self, indirect=False):
        """
        NOTE 

          Every DAGNode (except lights) can be instantiated! 
          - Transforms, joints, constraints...
          - Cameras, meshes, nurbsCurve, locators...

          But remember:
          - LIGHTS CANNOT BE INSTANTIATED!!!
        """        
        return self._pointer.isInstanced(indirect)



    @property
    def longName(self):     
        return self._pointer.fullPathName()

        

    @property
    def name(self): 
        return self._pointer.partialPathName()



    @property
    def shortName(self): 
        return self._pointer.name()






class Transform(DAGNode):
    """=========================================================="""
    """ Only a <transform> (and its derived) can have "children" """
    """ ??? SURE ??? The DAGNodes have children methods...       """
    """=========================================================="""      

    #-----------------------------
    # INITIALIZER
    #-----------------------------  
    def __init__(self, mObject):
        printDebug('Transform.__init__')        
        super(Transform, self).__init__(mObject)


 
    #-----------------------------
    # METHODS
    #-----------------------------
    def getChildren(self, **kwargs):
        """
        Recycle the syntax of 'listRelatives(children=True, ...)'
        and correct the type/noIntermediate bug!
        """

        type_flag = kwargs.get("type", kwargs.get("t", None))

        if not type_flag:
            children = MC.listRelatives(self.name, children=True, path=True) or []
        else:
            children = MC.listRelatives(self.name, children=True, type=type_flag, path=True) or []

        return [MuNode(x) for x in children]
        #return Bundle(*children)



    def getMesh(self):
        """
        If nothing is found, returns None!
        If multiple meshes are present, it doesn't give a fuck: you get the first one!
        """
        try:
            return self.getMeshes()[0]
        except IndexError:
            return None
        



    def getMeshes(self, noIntermediate=True):
        """
        If nothing is found, returns []
        (to allow void loops, e.g. for x in node.getMeshes():...)
        """        
        # Probably useless... we return a list of Wrappers
        meshChildren = MC.listRelatives(self.name, children=True, type='mesh', path=True) or []
                                                                               
        if noIntermediate:
            meshChildren = [x for x in meshChildren if MC.getAttr(x + '.intermediateObject') == 0]
        
        return [MuNode(x) for x in meshChildren]
        #return Bundle(*meshChildren)
        


    def _isTypedTransform(self, allowedType='mesh', noIntermediate=True, onlyOne=True):
        """ Check if the transform has shapeChildren of an allowedType """
        # The flag combination 'shapes + noIntermediate' is valid, 
        # but not 'type + noIntermediate' (the latter is ignored)
        shapeChildren = MC.listRelatives(self.name, children=True, path=True, shapes=True, noIntermediate=noIntermediate) or []
        allowedShapeChildren = [x for x in shapeChildren if MC.nodeType(x) == allowedType]
        
        if onlyOne:
            return len(allowedShapeChildren) == 1
        else:
            return len(allowedShapeChildren) >= 1 



    def isPureTransform(self):
        """ A 'pure' transform has no shapeChildren """
        shapeChildren = MC.listRelatives(self.name, children=True, path=True, shapes=True, noIntermediate=False) or []
        return len(shapeChildren) == 0



    def isMeshTransform(self, onlyOneAllowed=True):
        """ Check if the transform has only one meshChild (or multiple, according to 'onlyOneAllowed') """
        return self._isTypedTransform(allowedType='mesh', noIntermediate=True, onlyOne=onlyOneAllowed)
    


    """
    def isLocatorTransform(self):
        return self.isTypedTransform(allowedType='locator', noIntermediate=True, onlyOne=True)


       
    def isNurbsCurveTransform(self):
        return self.isTypedTransform(allowedType='nurbsCurve', noIntermediate=True, onlyOne=False)
    """  






class Mesh(DAGNode):
    #-----------------------------
    # INITIALIZER
    #-----------------------------
    def __init__(self, mObject):
        printDebug('Mesh.__init__')        
        super(Mesh, self).__init__(mObject)



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
    

    def getSmoothMeshDict(self):
        meshName = self.shortName
        smoothDict = {}
        for attr in Mesh._smoothMeshAttributes:
            smoothDict[attr] = MC.getAttr(meshName + "." + attr)
        return smoothDict    


    def setSmoothMesh(self, *args, **kwargs):
        meshName = self.shortName

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
















































#------------------------------------------------------------------------------
# Module loaded!
MUT.moduleLoadedMessage()
#------------------------------------------------------------------------------