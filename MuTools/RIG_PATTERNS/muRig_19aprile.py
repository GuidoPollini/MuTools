=======================================================================================

niente MALE!!!
    
oppure
W = Wrap
A = PyNode("A")
B = PyNode("B")
C = PyNode("C")

W("CAZZONE.tx",  
  "CAZZONE.ty", 
  "CAZZONE.tz", 
  "CAZZONE.rx", 
  "CAZZONE.ry", 
  "CAZZONE.rz").unlock()\
               .setValue(12)\
               .lockHide()\

Wrap("CAZZONE.tx", 
     "CAZZONE.ty", 
     "CAZZONE.tz", 
     "CAZZONE.rx", 
     "CAZZONE.ry", 
     "CAZZONE.rz").unlock()\
                  .setValue(12)\
                  .lock()




=======================================================================================



import pymel.core as PC
import pymel.core.datatypes as DT
def _getParent(self):
    print "new getParent"
def _getWorldTRS(self):
    print "new getWorldTRS" 

class Wrap(list):
    def __init__(self, *args):
        if len(args) <= 1:
            super(Wrap, self).__init__(*args)
        else:
            # It's an explicit initialization, e.g.:
            # Bundle("x", "y", "w", "k").porcoDio()
            tempList = args
            super(Wrap, self).__init__(tempList)
    
    def lock(self):
        for i in range(len(self)):
            attr = PC.PyNode(self[i])
            #if isinstance(self[i], PC.general.Attribute):
            try:    
                attr.lock()
            except Exception as exc:
                print "pleaseDie", str(exc)
        # To allow concatenation        
        return self
         
    def unlock(self):
        for i in range(len(self)):
            attr = PC.PyNode(self[i])
            #if isinstance(self[i], PC.general.Attribute):
            try:    
                attr.unlock()
            except Exception as exc:
                print "pleaseDie", str(exc)
        # To allow concatenation        
        return self         
        
                
    def getValue(self):
        if len(self) == 1:
            pass
        result = []
        for i in range(len(self)):
            attr = PC.PyNode(self[i])
            result.append(attr.get())    
        return result
                
    def setValue(self, *args):
        if len(self) == len(args):
            # It's a massive "setValue"
            for i in range(len(self)):
                attr = PC.PyNode(self[i])
                attr.set(args[i])
                
        if len(args) == 1 and not isinstance(args[0], list):
            # One value to rule them all!
            for i in range(len(self)):
                attr = PC.PyNode(self[i])
                attr.set(args[0])                                   
            
            
        if len(args) == 1 and isinstance(args[0], list):
            for i in range(len(self)):
                attr = PC.PyNode(self[i])          
                attr.set(args[0][i])       
        return self
                
                
    def getVisibility(self):
        result = list()
        for i in range(len(self)):
            result.append(self[i].isVisible())
        return result
        
    def setParent(self, parent):
        for i in range(len(self)):
            print "parenting"
            PC.parent(self[i], parent)
           
    
def _listSetVisibility(self):
    print "list SetVisibility"
    
    
Wrap("CAZZONE.tx", 
     "CAZZONE.ty", 
     "CAZZONE.tz", 
     "CAZZONE.rx", 
     "CAZZONE.ry", 
     "CAZZONE.rz").unlock()\
                  .setValue(12)\
                  .lock()
 
""" IS THERE A WAY TO ELIMINATE THE UGLY USELESS "WRAP"??? """ 


print Wrap("CAZZONE.tx", "CAZZONE.ty", "CAZZONE.tz").getValue()

    
"""
FIND THE MOST ELEGANT WAY TO DO THIS... CHECK IF YOU'RE OVERRIDING A METHOD THAT SHOULDN'T BE OVERRIDED 
(e.g. setParent, getParent)
e cerca di estendere automaticamente i vari metodi atomici al Bundle (setWorldT, lockAttr... )
PUO ESSERE DAVVERO UTILE IL FATTO CHE ANCHE GLI ATTRIBUTI IN PYMEL SONO "pointers"

e fare una cosa dle genere:
Bundle("obj.x", "obj.y", "puppa.fava", "merda.shit").lockAttr()\
                                                    .hudeAttr()\
                                                    .setMaxValue(999)
 
"""    

"""
    
setattr(PC.nodetypes.Transform, "getWorldTRS", _getWorldTRS)
setattr(PC.nodetypes.Transform, "getParent", _getParent)
setattr(PC.nodetypes.Transform, "getVisibility", _getVisibility)

ptrA = PC.PyNode("A")
ptrB = PC.PyNode("B")
ptrC = PC.PyNode("C")
ptrD = PC.PyNode("D")
"""

#bof = [ptrA, ptrB, ptrC, ptrC]
#pippo = Bundle([ptrA, ptrB, ptrC, ptrC])

#Bundle([ptrA, ptrB, ptrC, ptrC]).setParent("CAZZONE")   

# better
#Bundle(ptrA, ptrB, ptrC, ptrC).setParent("CAZZONE")    
 
#fava = Bundle(1, 2, 3, 4)
#print fava[3]

#pippo.setParent("CAZZONE")

#attr1 = PC.PyNode("CAZZONE.tx")
#attr2 = PC.PyNode("CAZZONE.sx")
#attr3 = PC.PyNode("CAZZONE.rx")

"""
Wrap("CAZZONE.tx", 
     "CAZZONE.ty", 
     "CAZZONE.tz").lock()\
                  .unlock()
"""





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
        