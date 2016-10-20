'''
def loggedMuNode(nodeName, errorLog):
    """
    Return the MuNode wrapper if possible, 
    otherwise None and put the nodeName in the passed
    list...
    """

    node = None
    
    try:
        node = Core.MuNode(nodeName)
    except:
        errorLog.append(nodeName)
    
    return node

errorLog = []
cameraRigFolder = loggedMuNode('__CAMERA__', errorLog) 
camera_global   = loggedMuNode('camera_global', errorLog)
...

if len(errorLog) > 0:
    # Somewhere it failed!!!
    pass
else:
    pass
    everything went well!!!    

'''

# Nullify exceptions:

'''
from MuTools.MuCore import *
nullifyExceptions = Utils.nullifyExceptions()

cameraRigFolder = nullifyExceptions.MuNode('__camera__')
cameraRigFolder = nullifyExceptions.MuNode('__camera__')
cameraRigFolder = nullifyExceptions.MuNode('__camera__')
cameraRigFolder = nullifyExceptions.MuNode('__camera__')

if nullifyExceptions.exceptions ius not None:
    # it failed somewhere
'''



import MuTools.MuUtils as Utils
import MuTools.MuCore  as Core
import MuTools.MuUI    as UI

# Or better (NOPE :(... ): 
from MuTools import Utils, Core, UI

import sys
muPath = r"C:\Users\guido.pollini\Desktop\MuTools"
if muPath not in os.sys.path:
    sys.path.append(muPath)






import maya.cmds as mc

# ROTATION BUG SOLVED!!!

def linkCameraAndPlates(*args):
    #Python has a "weak closure", i.e. a nested function can read outerScope variables but NOT modify them.
    #By using the ugly array trick, we get a full "strong closure" (read and write). Just use VAR[0]=...
    LINKING_REPORT = [""]    
    LINKING_STATUS = ["VALID"] 

    def abortLinking(message=""):
        if mc.window("linkingReport_WIN", ex=1):
            mc.deleteUI("linkingReport_WIN") 
        mc.window("linkingReport_WIN", t="LINKING REPORT", tlb=1, w=300, s=1, mb=0)
        0;mc.columnLayout(w=300) 
        0;  mc.button(l="FATAL ERROR", w=300, h=40, bgc=(1,0,0))
        0;  mc.text(l="")
        0;  mc.text(l=LINKING_REPORT[0], align="left", rs=True)
        0;  mc.text(l="")
        0;  mc.button(l="LINKING ABORTED", w=300, bgc=(1,0,0))
        0;  mc.setParent("..")
        mc.showWindow  ("linkingReport_WIN")
        mc.error("FATAL ERROR: linking aborted!")      








    --> BETTER <--
    --> capsule = trans.incapsulate(trans.name() + '_holder') # It works with pivots too:)
    """
    def incapsulateDAGNode(node, capsuleName):    
        capsule = mc.createNode("transform", n=capsuleName)
        parents = mc.listRelatives(node, parent=True)
        if parents != None:
            #Move the capsule at the same hierarchy position of node and then copyAttr
            mc.parent(capsule, parents[0])
        mc.copyAttr(node, capsule, values=True, at=["t","r","s"]) 
        mc.parent(node, capsule, absolute=True)    
    """




    def getOrInvalidate(object):
        #Look for the object XXXXXXobject (namespace irrelevant), invalidate an None if missing
        results = mc.ls("*" + object, recursive=True)
        if len(results) != 1:
            LINKING_REPORT[0] += " - \"" + object + "\" is missing!\n"
            LINKING_STATUS[0] = "INVALID"
            return None 
        else:
            return results[0]    

    #------------------------------------------------------------------
    #MAIN CONSTRUCTION
    #Gather keyObject names
    cameraRigFolder         = getOrInvalidate("__CAMERA__")
    camera_global           = getOrInvalidate("camera_global")
    cameras_holder          = getOrInvalidate("cameras_holder")
    cameraHD_controller     = getOrInvalidate("cameraHD_controller")
    camera_aim              = getOrInvalidate("camera_aim")
    realCameraHD            = getOrInvalidate("cameraHD")
    realCameraPROJ          = getOrInvalidate("cameraPROJ")
    controllerTemplate      = getOrInvalidate("plateCtrl") #It's inside the cameraRig
    platesFolder            = getOrInvalidate("__SET__")
    platesList              = []
        
    if LINKING_STATUS[0] == "INVALID":
        abortLinking()
    
    plateCandidates = mc.listRelatives(platesFolder, children=True, type="transform")
    numberOfPlates = len(plateCandidates)
    if numberOfPlates!= 0:
        platesList = [None] * numberOfPlates

        for candidate in plateCandidates:
            #Get the int ### from the pattern: XXXX_###_GlobalSRT_XXXX
            temp = candidate[:candidate.rfind("_GlobalSRT")]
            priority = int(temp[temp.rfind("_")+1:])
            platesList[numberOfPlates - priority] = candidate 
            
        # Create and connect platesHolder
        mc.createNode ("transform", n="platesHolder", p=platesFolder)
        mc.addAttr    ("platesHolder", ln="size", at="double", dv=1)
        mc.setAttr    ("platesHolder.size", e=True, keyable=True)
        mc.connectAttr("platesHolder.size", "platesHolder.sx")
        mc.connectAttr("platesHolder.size", "platesHolder.sy")
        mc.connectAttr(cameras_holder + ".focalCorrection", "platesHolder.size")
        mc.setAttr    ("platesHolder.tz", -100*(numberOfPlates-1))
        
        ###############################################################################

        #Constraint and connect

        #Set camera elements
        mc.setAttr(camera_global + ".t", 0, 0, 100)
        mc.setAttr(camera_global + ".r", 0, 0, 0)
        mc.setAttr(camera_global + ".controllersSize", 4.5)
        mc.setAttr(cameras_holder + ".t", 0, 0, 0) 
        mc.setAttr(camera_aim + ".t", 0, 0, -100*(numberOfPlates-1) - 100)   
        mc.parentConstraint(camera_aim, "platesHolder", mo=True)

        mc.createNode("transform", n="cameraMarker", p="platesHolder")
        mc.pointConstraint(cameras_holder, "cameraMarker", mo=False) 
        
        maxWidth  = 0.0
        maxHeight = 0.0
        for (i, plate) in enumerate(platesList):
            #Get the plate size with boundingBoxSize (in DAGNode)
            plateWidth  = mc.getAttr(plate + ".bbsx")
            plateHeight = mc.getAttr(plate + ".bbsy")
            maxWidth = plateWidth if plateWidth > maxWidth else maxWidth
            maxHeight = plateHeight if plateHeight > maxHeight else maxHeight
            
            # Build the new controller
            
            locatorShape = mc.listRelatives(plate, children=True, shapes=True)
            if locatorShape == None:
                #If it was not a locator, can't proceed...
                abortLinking("The transform \"" + plate + "\" has NOT a locatorShape!")
            
            # Hide locator shape
            mc.setAttr(locatorShape[0] + ".visibility", 0)
            
            # Create controller
            newController = controllerTemplate + str(numberOfPlates- i)
            mc.duplicate(controllerTemplate, n=newController)
            mc.setAttr(newController + ".visibility", lock=True, keyable=False, channelBox=False)
            mc.setAttr(newController + ".rx", lock=True, keyable=False, channelBox=False)
            mc.setAttr(newController + ".ry", lock=True, keyable=False, channelBox=False)
            mc.setAttr(newController + ".rz", lock=True, keyable=False, channelBox=False)
            mc.setAttr(newController + ".tz", -100 * i)
            incapsulateDAGNode(newController, newController + "_offset")

            # Create cluster for rescaling Interface
            mc.select(newController + "Shape", newController + "Shape1", 
                      newController + "|plusPlate|plusPlateShape", 
                      newController + "|minusPlate|minusPlateShape", r=True)
            clusterTransform = mc.cluster(name = newController + "Clustering", relative=True)[1]
            mc.setAttr(clusterTransform + ".visibility", 0)
            camera_global = getOrInvalidate("camera_global")
            mc.connectAttr(camera_global + ".controllersSize", clusterTransform + ".sx")
            mc.connectAttr(camera_global + ".controllersSize", clusterTransform + ".sy")
            mc.parent(clusterTransform, newController + "_offset", relative=True)

            # Connect resizingArrows visibility and finally reparent
            mc.connectAttr(newController + ".showResizingArrows", newController + "|resizingArrows.visibility")            
            mc.parent(newController + "_offset", "platesHolder", absolute=True)

            #mc.parent(plate, newController)
            
            # MAKE PLATES DYNAMIC
            #Add the Zs of controller and offset to get the Z relative to "platesHolder"
            zCoordNode = newController + "_zCoord"
            mc.createNode ("addDoubleLinear", n=zCoordNode)
            mc.connectAttr(newController + ".tz", zCoordNode + ".input1")
            mc.connectAttr(newController + "_offset.tz", zCoordNode + ".input2")
            #Compute orthogonal distance 
            zDistanceNode = newController + "_zDistance"
            mc.createNode ("plusMinusAverage", n=zDistanceNode)
            mc.setAttr    (zDistanceNode + ".operation", 2) #Subtract
            mc.connectAttr("cameraMarker.tz", zDistanceNode + ".input1D[0]")
            mc.connectAttr(zCoordNode + ".output", zDistanceNode + ".input1D[1]")
            #Create a factorNode to have a first approximation of size
            factorNode = newController + "_factor"
            mc.createNode ("multDoubleLinear", n=factorNode)
            mc.connectAttr(zDistanceNode + ".output1D", factorNode + ".i1") #Branch HERE the FOCAL LENGHT
            mc.setAttr    (factorNode + ".i2", .001) # <-- plug the factor HERE!!!
            mc.connectAttr(factorNode + ".output", newController + "_offset.sx")
            mc.connectAttr(factorNode + ".output", newController + "_offset.sy")

            # The real plate is still unlinked to solve the rotation bug; do constraint now
            mc.parentConstraint(newController, plate, mo=False)               
            DAGChildren = mc.listRelatives(plate, children=True, type="transform")
            if DAGChildren != None:
                    # Connect visibility and lock to the controller
                    mc.setAttr(DAGChildren[0] + ".overrideDisplayType", 2) #Reference
                    mc.connectAttr(newController + ".lockPlate", DAGChildren[0] + ".overrideEnabled")
                    mc.connectAttr(newController + ".showPlate", DAGChildren[0] + ".visibility")
                    mc.connectAttr(newController + ".rotX", DAGChildren[0] + ".rx")
                    mc.connectAttr(newController + ".rotY", DAGChildren[0] + ".ry")
                    mc.connectAttr(newController + ".rotZ", DAGChildren[0] + ".rz")
            
            # multiply togheter the dynamic plate scale with the controller scale

            mc.createNode ("multDoubleLinear", n=plate + "_trueScaleX")
            mc.createNode ("multDoubleLinear", n=plate + "_trueScaleY")
            mc.createNode ("multDoubleLinear", n=plate + "_trueScaleZ")

            mc.connectAttr(newController + ".sx", plate + "_trueScaleX.input1")
            mc.connectAttr(newController + ".sy", plate + "_trueScaleY.input1")
            mc.connectAttr(newController + ".sz", plate + "_trueScaleZ.input1")

            mc.connectAttr(factorNode + ".output", plate + "_trueScaleX.input2")
            mc.connectAttr(factorNode + ".output", plate + "_trueScaleY.input2")
            mc.connectAttr(factorNode + ".output", plate + "_trueScaleZ.input2")

            # Don't forget the focal correction of PROJ
            mc.createNode ("multDoubleLinear", n=plate + "_focal_trueScaleX")
            mc.createNode ("multDoubleLinear", n=plate + "_focal_trueScaleY")
            mc.createNode ("multDoubleLinear", n=plate + "_focal_trueScaleZ")

            mc.connectAttr(plate + "_trueScaleX.output", plate + "_focal_trueScaleX.input1")
            mc.connectAttr(plate + "_trueScaleY.output", plate + "_focal_trueScaleY.input1")
            mc.connectAttr(plate + "_trueScaleZ.output", plate + "_focal_trueScaleZ.input1")

            mc.connectAttr("platesHolder.sx", plate + "_focal_trueScaleX.input2") # It HAS to be the full S scale
            mc.connectAttr("platesHolder.sx", plate + "_focal_trueScaleY.input2") # Otherwise, the bug's still there
            mc.connectAttr("platesHolder.sx", plate + "_focal_trueScaleZ.input2")
            

            # finally link all together...
            mc.connectAttr(plate + "_focal_trueScaleX.output", plate + ".sx")
            mc.connectAttr(plate + "_focal_trueScaleY.output", plate + ".sy")
            mc.connectAttr(plate + "_focal_trueScaleZ.output", plate + ".sz")            
            
        ###############################################################################

        # Hide controller template
        mc.setAttr(controllerTemplate + ".visibility", 0)

        # scale the plane following the frustum
        # mayaUnits=cm, focalLenght=mm, cameraAperture=inches, 1inch=2.54cm
        apertureX = (maxWidth  * 0.1 * 6.0) / (100 * 2.54) # The size in cm of the first plate (1/10 always)
        apertureY = (maxHeight * 0.1 * 6.0) / (100 * 2.54) # Divide for 100cm, multiply for 6cm and convert in inches
        mc.setAttr(realCameraPROJ + "Shape.horizontalFilmAperture", apertureX)
        mc.setAttr(realCameraPROJ + "Shape.verticalFilmAperture", apertureY)
        
        # position the imagePlane correctly
        candidates = mc.listRelatives(cameraRigFolder, type="imagePlane", allDescendents=True)
        if candidates != None:
            # ImagePlane found: connect to cameraHD attributes
            imagePlaneShape = candidates[0]
            mc.connectAttr(cameraHD_controller + ".show", imagePlaneShape + ".visibility")
            # Alpha sensitivity
            mc.createNode("multiplyDivide", n="imagePlaneAlphaFactor")
            mc.connectAttr(cameraHD_controller + ".opacity", "imagePlaneAlphaFactor.input1X")
            mc.setAttr    ("imagePlaneAlphaFactor.input2X", 100)
            mc.setAttr    ("imagePlaneAlphaFactor.operation", 2) # Divide
            mc.connectAttr("imagePlaneAlphaFactor.outputX", imagePlaneShape + ".alphaGain")
            # Adapt depth (just put the imagePlane a bit farther than nearClippingPlane)
            mc.createNode("addDoubleLinear", n="depthCorrection")
            mc.setAttr    ("depthCorrection.input2", 0.01)
            mc.connectAttr(cameras_holder  + ".near", "depthCorrection.input1")
            mc.connectAttr("depthCorrection.output", imagePlaneShape + ".depth")
            # FilmGate offset moves the imagePlane too; correct:
            mc.connectAttr(realCameraHD + "Shape.horizontalFilmOffset", imagePlaneShape + ".offsetX")
            mc.connectAttr(realCameraHD + "Shape.verticalFilmOffset", imagePlaneShape + ".offsetY")
    
    else:    
        #No plate found: ABORT LINKING
        LINKING_REPORT[0] += " - the DAGFolder __SET__ is empty\n"
        abortLinking()

    if LINKING_STATUS[0] == "INVALID":
        #Something went wrong; stop linking
        abortLinking()
    
    


#--------------------------------------------------------------------------------------
def duplicatePlate(*args):
    pass 

def deletePlate(*args):
    pass         

