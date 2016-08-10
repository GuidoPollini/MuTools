
"""
----------------------------------------------------------------
================================================================
SIMPLIFIED (SIMPLE) ATTRIBUTES ACCESS

palla.v = False
palla.tx = cubbo.tx
palla.tx >> cubbo.tx
================================================================
----------------------------------------------------------------

idea pratica... ma forse non fattibile:

----------------------------------------
palla.v  = False
palla.tx = cubbo.tx
palla.tx >> cubbo.tx
  VS
palla.setAttr('v',  False)
palla.setAttr('tx', cubbo.getAttr('tx'))
palla.connect('tx', cubbo.name + '.tx')
----------------------------------------

Cioe' un rapido MC.setAttr e MC.getAttr e connectAttr()
Pero per evidenti ragioni, il seguente fallisce... forse chiedi troppo
class DGNode(object):
    def __init__(self, nodeName):
        if MC.objExists(nodeName):
            print 'UNO'
            # Si pianta qua. Infatti chiama __setatt__
            # che a sua volta chiama __getattr__ su un attributo che
            # non esiste ancora e va in loop infinito...
            self.name = nodeName
            print 'DUE'
        else:
            MC.error('Can\'t bind!')
    
    def __getattr__(self, attr):
        print "__getattr__ called!", attr
        return MC.getAttr(self.name + '.' + attr)
    def __setattr__(self, attr, value):
        print "__setattr__ called!", attr, value
        MC.setAttr(self.name + '.' + attr, value)
x = DGNode('xxx')
print x.tx #??
print x.tx.value #??

i piacerebbe una classe che onitora certi attributi (da registrare) 
dei nodi selezionati...





"""





"""=================================================================================================
================================================================================================="""


import maya.cmds as MC
def GP_incapsulateDAGNode(suffixName):
    objs = cm.ls (sl=1, type="transform")
    for obj in objs:
        newObj = cm.createNode ("transform", n=obj+suffixName)
        parentsObj = cm.listRelatives (obj, p=1)
        if parentsObj:
            # null if parent to the world
            cm.parent (newObj, parentsObj[0])
        # copyAttr copies even CONNECTIONS!!!
        cm.copyAttr (obj, newObj, v=1, at=["t","r"])
        if cm.nodeType (obj) == "joint":
            # se perenting for joint is different. it add a transform in a=1 mode
            cm.parent (obj, newObj, r=1)
            cm.setAttr (obj+".t",0,0,0)                         
            cm.setAttr (obj+".r",0,0,0) 
        else:    
            cm.parent (obj, newObj, a=1)
        cm.select (newObj, r=1)





     