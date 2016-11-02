__version__ = '1.1.0'
print '--> Executing "{0}" (version {1})...'.format(__name__, __version__)






from MuTools.MuUtils import *
from MuTools.MuCore  import * 
"""
Import MuTools core modules without namespace (JUST WATCH OUT FOR INTERNAL COLLISIONS!)
(try an 'from MuTools import *' by defining __all__ in the __init__ of MuTools)
"""
import MuTools.MuUI    as UI
import MuTools.MuScene as Scene

import maya.cmds as MC

import sys
import re


log = Log() # --> "c:\users\guido~1.pol\appdata\local\temp\MULOGS\finalizeLayoutBuild.log"



def getProperEpisodeShotName(*args): 
    """
    ---------------------------------------------------------------------------    
    RETURN (<str>, <str>)|(None, None) 
      ('BDG###', '###')    <--  'BDG###_###'    
                                'BDG###_###_*'
      ('BDG###", "###_@')  <--  'BDG###_###_@'  
                                'BDG###_###_@_*'
      (None, None)         <--  Invalid scene name!    
    ---------------------------------------------------------------------------
    """
    
    # Ex: 
    #'BDG100_006_A_lay_007.ma'  -->  ['BDG100', '006', 'A', 'lay', '007']
    sceneName = MC.file(q=True, sceneName=True, shortName=True)
    tokens = sceneName.rstrip('.ma').rstrip('.mb').split('_')

    episode, shot = None, None
    
    if len(tokens) >= 2:
        # tokens[0] --> 'BDG###'
        if re.match(r'^BDG[0-9]{3}$', tokens[0]):    
            # tokens[1] --> '###'
            if re.match(r'^[0-9]{3}$', tokens[1]):
                episode = tokens[0]
                shot    = tokens[1]        
                # tokens[2] --> '@' (if any)
                if len(tokens) >= 3:
                    if re.match(r'^[A-Z]{1}$', tokens[2]):
                        shot = shot + '_' + tokens[2]                        
    
    return (episode, shot)





class ShotgunBadgers(object):
    """
    ---------------------------------------------------------------------------    
    DESCRIPTION
    Try to instantiate shotgun; it will NEVER raise an exception.
    Instead check if .isActive() 

    NOTE: --> EVERY POSSIBLE EXCEPTION MUST BE SILENCED!!!
    ---------------------------------------------------------------------------
    """
    
    def __init__(self):
        self._projectId = 73 # Badgers Id
        self._handle    = None
        self._lastError = None
             
        try:
            shotgunPath = r'R:\01_SAISON_1\00_PROGRAMMATION\shotgun_pipeline'
            if shotgunPath not in sys.path:
                sys.path.append(shotgunPath)
            
            # Import the shotgunApi            
            from shotgun_api3 import shotgun
        
            # Instantiate shotgun
            shotgun.NO_SSL_VALIDATION     
            serverPath   = 'https://ellipsanime.shotgunstudio.com/'
            scriptName   = 'ellipse_packager'
            scriptKey    = '874c205a45e841393046a7e871cda1f24a2922cd06becc39ee3584246392bc36'
            self._handle = shotgun.Shotgun(serverPath, scriptName, scriptKey)
    
            # Success:)
            self._lastError = None
            
        except Exception as exc:
            # Impossible to connect to shotgun (DON'T raise anything!)
            self._lastError = str(exc)
        

    def isActive(self):
        # Return True iff the shotgun instance was successfully created.
        return self._handle is not None
    
    
    def lastError(self):
        return self._lastError
            
    
    def getShotCameraType(self, episode=None, shot=None):
        """
        ---------------------------------------------------------------------------
        DESCRIPTION
           If no argument is provided, it takes the name of the actual scene and 
           tries to recover episode and shot name!
           
           
        ARGUMENTS
          epidode=None <str>
            'BDG###' 
          shot=None <str>  
            'sh###'|'sh###_@'
        
        
        RETURN <str>|None
          'HD'|'PROJ' if camera is set.
          None if unable to detect the camera type.
        ---------------------------------------------------------------------------            
        """
        
        cameraType = None

        if not self.isActive():
            # No valid shotgun instance
            return
                
        try:
            if episode is None or shot is None:
                episode, shot = getProperEpisodeShotName()
                # Shotgun requires episode --> 'sh###'
                shot = 'sh' + shot            
            
            episodeDict = self._handle.find_one(
                'CustomEntity01', 
                [['project', 'is', {'type': 'Project', 'id': self._projectId}], ['code', 'is', episode]], 
                []
            )
            filters = [
                ['project', 'is', {'type': 'Project', 'id': self._projectId}],
                ['sg_episode', 'is', episodeDict],
                ['sg_shortname', 'is', shot]
            ]
            cameraType = self._handle.find_one('Shot', filters, ['sg_cam_type'])['sg_cam_type']

            # Success:)
            self._lastError = None
            
        except Exception as exc:
            # Impossible to get the camera type from shotgun (DON'T raise anything!)
            self._lastError = str(exc)
        
        return cameraType         
        
        



class CameraPlatesLinker(object):
    def __init__(self):
        self._linkErrors = []


    def _getOrInvalidate(self, nodeName):
        """ --> you should check for camera namespace integrity <-- """

        candidates = Scene.listObjects(nodeName)
        if len(candidates) != 1:
            self._linkErrors.append('Name error for "{}"! Can\'t proceed.'.format(nodeName))
            return None
        else:
            return candidates[0]
              

    def link(self):
        print 'Linking'
        





        #----------------------------------------------------------------------
        # Collect the required nodes
        #----------------------------------------------------------------------
        
        # No namespace, no Dag-ambiguity and worldChildren
        # (the leading "|" forces an complete fullDagPath: it can't be partial)
        cameraFolder         = self._getOrInvalidate('|__CAMERA__')
        platesFolder         = self._getOrInvalidate('|__SET__')
        

        # Always namespaced, but no Dag-ambiguity allowed!
        controllerTemplate   = self._getOrInvalidate('*:plate_controller')
        pivotTemplate        = self._getOrInvalidate('*:plate_pivot')

        cameraAim            = self._getOrInvalidate('*:camera_aim')
        cameraGlobal         = self._getOrInvalidate('*:camera_global')

        camerasHolder        = self._getOrInvalidate('*:cameras_holder')
        cameraBG             = self._getOrInvalidate('*:cameraBG')
        
        cameraHD             = self._getOrInvalidate('*:cameraHD')
        cameraHDController   = self._getOrInvalidate('*:cameraHD_controller')

        cameraPROJ           = self._getOrInvalidate('*:cameraPROJ')
        cameraPROJController = self._getOrInvalidate('*:cameraPROJ_controller')

        if self._linkErrors:
            print 'FATAL -->', self._linkErrors
            return

        # Extra
        cameraImagePlanes = cameraFolder.children(type='imagePlaneTransform')
        if len(cameraImagePlanes) != 1:
            print 'FATAL --> Animatic image plane, missing or ambiguous'
            return
        animaticImagePlane = cameraImagePlanes[0]
                     

        


            
        #----------------------------------------------------------------------
        # First check on plates
        #----------------------------------------------------------------------

        plates = platesFolder.children(type='locatorTransform')
        if not plates:
            print 'FATAL --> No plates to link, sorry'
            return 

        numPlates = len(plates)
        platesList = [None] * numPlates # The plate list with correct order
        
        # Order plates by 'priority'
        for plate in plates:
            # Plate priority is the third tag from left: XXXXXXX_###_GlobalSRT_XXXXXXX
            priority = int(plate.name().split('_')[-3])
            platesList[numPlates - priority] = plate 
           




        #----------------------------------------------------------------------
        # platesHolder
        #----------------------------------------------------------------------

        platesHolder = Transform.create(name='platesHolder', parent=platesFolder)

        platesHolder.addPlug(name='size', type='double', defaultValue=1)
        #platesHolder.size.setKeyable(False)

        platesHolder.size >> (platesHolder.sx,
                              platesHolder.sy)

        cameraBGFocalFactor = self._getOrInvalidate('*:cameraBGFocalFactor')
        cameraBGFocalFactor.outputX >> platesHolder.size

        # Put the 'placeHolder' where the fartest plate is
        platesHolder.tz.set(-100 * (numPlates - 1))




        #----------------------------------------------------------------------
        # Manage cameras
        #----------------------------------------------------------------------
        
        # Move the whole rig far fro the origin
        cameraGlobal.t.set(0, 0, 100)
        cameraGlobal.r.set(0, 0, 0)

        # Set the aim in the same position of 'placeHolder'
        cameraAim.t.set(0, 0, -100 * (numPlates - 1) - 100)

        
        #camerasHolder.t.set(0, 0, 0)
        # Badgers has very large assets
        camerasHolder.controllers_size.set(4.5)

        # 'platesHolder' must follow 'cameraAim'
        'UNWRAPPED'; MC.parentConstraint(cameraAim.name(), 'platesHolder', mo=True)
        
        # ???
        cameraMarker = Transform.create(name='cameraMarker', parent=platesHolder)

        'UNWRAPPED'; MC.pointConstraint(camerasHolder.name(), 'cameraMarker', mo=False) 
        



        #----------------------------------------------------------------------
        # Plates
        #----------------------------------------------------------------------
        
        'DEV'; sizeList = []

        maxWidth  = 0.0
        maxHeight = 0.0

        for i, plate in enumerate(platesList):

            # Get the plate size (by its boundingBox)
            plateWidth  = plate.bbsx.get()
            plateHeight = plate.bbsy.get()
            maxWidth  = max(maxWidth,  plateWidth)   
            maxHeight = max(maxHeight, plateHeight) 
            'DEV'; sizeList.append((plateWidth, plateHeight))


            # Hide the locator of the plate 
            # (Note that plate is a pure <locatorTransform>)
            plate.shapes()[0].hide()
            



            #-------------------------------------------------------------------------------
            # Plate controller/pivot creation
            #-------------------------------------------------------------------------------
            """
            def customDuplicate(originalName):
                newName = originalName + str(numPlates - 1)
                'UNWRAPPED'; MC.duplicate(originalName, n=newName)
                newObj = MUNode(newName)
                
                # Lock and hide teh visibility
                newController.visibility.setLocked()\
                                        .setVisible(False)
                return 
            """

            newControllerName = controllerTemplate.name() + str(numPlates - i)
            #newPivotName      = pivotTemplate.name()      + str(numPlates - i) 
            
            #customDuplicate


            'UNWRAPPED'; MC.duplicate(controllerTemplate.name(), n=newControllerName)
            #'UNWRAPPED'; MC.duplicate(pivotTemplate.name(),      n=newPivotName)            
            newController = MuNode(newControllerName)
            #newPivot      = MuNode(newPivotName)
            

            # LOck/hide/make unkeyable 
            newController.visibility.lock().hide()
            newController.rx.lock().hide()
            newController.ry.lock().hide()
            newController.rz.lock().hide()
            newController.showPlate.setKeyable(False)
            newController.showPivot.setKeyable(False)

            
            newController.tz.set(-100 * i)
            
            newControllerOffset = newController.incapsulate(newController.name() + "_offset")
            
            # Create cluster for rescaling Interface
            newControllerShapeNames = [x.name() for x in newController.shapes()]
            'UNWRAPPED'; MC.select(newControllerShapeNames, r=True)
            'UNWRAPPED'; clusterTransform = MuNode(MC.cluster(name=newController.name() + "Clustering", relative=True)[1])
            
            clusterTransform.hide()

            camerasHolder.controllers_size >> (clusterTransform.sx, 
                                               clusterTransform.sy)

            """ EASY PLUG 
            clusterSzCorrection = MultiplyDivide.create(newController.name() + '__szCorrection', 
                operation='division',
                input1X=1,
                input2X=camerasHolder.controllers_size,
                outputX=clusterTransform.sz
            )
            SOUNDS BETTER, AH? :)
            """
            # To avoid z-deformation of the controller, inverse the controllers' size
            clusterSzCorrection = DGNode.create('multiplyDivide', name=newController.name() + '__szCorrection')
            clusterSzCorrection.operation.set(2) # Division
            clusterSzCorrection.input1X.set(1)
            camerasHolder.controllers_size >> clusterSzCorrection.input2X
            clusterSzCorrection.outputX >> clusterTransform.sz 


            clusterTransform.setParent(newControllerOffset, absolute=False)


            newControllerOffset.setParent(platesHolder, absolute=True)





            # MAKE PLATES DYNAMIC
            # Add the Zs of controller and offset to get the Z relative to "platesHolder"
            zCoordNode = DGNode.create('addDoubleLinear', name=newController.name() + '_zCoord')
            newController.tz       >> zCoordNode.input1
            newControllerOffset.tz >> zCoordNode.input2
            
            """ EASY PLUG
            zCoordNode = addDoubleLinear.create(newController.name() + '_zCoord', 
                input1=newController.tz,
                input2=newControllerOffset.tz
            )
            """

            # Compute orthogonal distance 
            zDistanceNode = DGNode.create('plusMinusAverage', name=newController.name() + '_zDistance')
            zDistanceNode.operation.set(2) # Subtract
            

            # zDistanceNode.__getattr__('input1D').__getitem__(0), the second one being a method of MuPlug
            cameraMarker.tz   >> zDistanceNode.input1D[0] 
            zCoordNode.output >> zDistanceNode.input1D[1]


            # Create a factorNode to have a first approximation of size
            factorNode = DGNode.create('multDoubleLinear', name=newController.name() + '_factor')
            zDistanceNode.output1D >> factorNode.input1 # Branch HERE the FOCAL LENGHT
            factorNode.input2.set(.001) # <-- plug the factor HERE!!!
            
            factorNode.output >> (newControllerOffset.sx,
                                  newControllerOffset.sy)



            # The real plate is still unlinked to solve the rotation bug; do constraint now
            'UNWRAPPED'; MC.parentConstraint(newController.name(), plate.name(), mo=False)        

            # Get the meshTransform child of the plate
            meshTrans = plate.children(type='meshTransform')[0]
            









            #-------------------------------------------------------------------------------
            # Fake mesh (<imagePlane>) creation
            #-------------------------------------------------------------------------------

            # NOTE: this create returns the wrapped shape, not the extra transform
            fakeMesh = DGNode.create('imagePlane', name=meshTrans.name() + '__fakeMeshShape')
            fakeMesh.lockedToCamera.set(False)
            fakeMesh.width.set(plateWidth)
            fakeMesh.height.set(plateHeight)

            # Hide frame, display referenced
            fakeMesh.frameVisibility.set(0)
            fakeMesh.overrideEnabled.set(1)
            fakeMesh.overrideDisplayType.set(2) # 2 --> Reference

            shadingEngine   = meshTrans.mesh().shadingEngine()
            shader          = shadingEngine.surfaceShader.inputPlug().node()
            fileTextureNode = shader.color.inputPlug().node()

            # - myNode.myPlug.set(otherNode.otherPlug.get())
            # VS
            # - myNode.myPlug.set(otherNode.otherPlug)
            #
            # Without the need to use the .get() when passing another MuPlug
            # MuPlug.set(<str>|<value>|<MuPlug>)
            # - <str>    myPlug.set('node.plug')
            # - <value>  myPlug.set(999)
            # - <value>  myPlug.set(otherPlug.get())
            # - <MuPlug> myPlug.set(otherPlug)

            fakeMesh.imageName.set(fileTextureNode.fileTextureName.get())

            fakeMesh.textureFilter.set(1) # 1 --> Bilinear

            
            fakeMeshParent = fakeMesh.parent()
            fakeMeshParent.rename(meshTrans.name() + '__fakeMesh')\
                          .setParent(meshTrans, absolute=False)
            """
            Or:
            fakeMesh.parent().rename(meshTrans.name() + '__fakeMesh')\
                             .setParent(meshTrans, absolute=False)
            """


            # Visibility control
            newController.showPlate >> fakeMesh.visibility

            # Make the original mesh invisible
            meshTrans.mesh().hide()







            """
            PIVOT CHANGE
             - pPlane2.transMinusRotatePivotX:   0.0 --> -23.2399443858
             - pPlane2.transMinusRotatePivotZ:   0.0 --> 11.6290221059
             - pPlane2.scalePivotZ:   0.0 --> -11.6290221059
             - pPlane2.scalePivotX:   0.0 --> 23.2399443858
             - pPlane2.rotatePivotX:   0.0 --> 23.2399443858
             - pPlane2.rotatePivotZ:   0.0 --> -11.6290221059
            """



            # Connect visibility and lock to the controller
            newController.rotX      >> meshTrans.rx
            newController.rotY      >> meshTrans.ry
            newController.rotZ      >> meshTrans.rz

           

            # multiply togheter the dynamic plate scale with the controller scale
            trueSx = DGNode.create('multDoubleLinear', name=plate.name() + '_trueScaleX')
            trueSy = DGNode.create('multDoubleLinear', name=plate.name() + '_trueScaleY')
            trueSz = DGNode.create('multDoubleLinear', name=plate.name() + '_trueScaleZ')
            


            """"""""""""""""""""""""""""""""""""""""""""""""""""""""" 
            MORE READABLE???

            trueSx, trueSy, trueSz = DGNode.create('multDoubleLinear', names=[
                plate.name() + '_trueScaleX', 
                plate.name() + '_trueScaleY', 
                plate.name() + '_trueScaleZ'
            ])
            """""""""""""""""""""""""""""""""""""""""""""""""""""""""


            newController.sx >> trueSx.input1
            newController.sy >> trueSy.input1
            newController.sz >> trueSz.input1
            
            factorNode.output >> (trueSx.input2, 
                                  trueSy.input2, 
                                  trueSz.input2)

            # Don't forget the focal correction of PROJ
            focalTrueSx = DGNode.create('multDoubleLinear', name=plate.name() + '_focal_trueScaleX')
            focalTrueSy = DGNode.create('multDoubleLinear', name=plate.name() + '_focal_trueScaleY')
            focalTrueSz = DGNode.create('multDoubleLinear', name=plate.name() + '_focal_trueScaleZ')
 

            """"""""""""""""""""""""""""""""""""""""""""""""""""""""" 
            MORE READABLE??? ... Nope

            focalTrueSx, focalTrueSy, focalTrueSz = DGNode.create('multDoubleLinear', names=[
                plate.name() + '_focal_trueScaleX', 
                plate.name() + '_focal_trueScaleY',
                plate.name() + '_focal_trueScaleZ'
            ])
            """""""""""""""""""""""""""""""""""""""""""""""""""""""""

            trueSx.output >> focalTrueSx.input1
            trueSy.output >> focalTrueSy.input1
            trueSz.output >> focalTrueSz.input1
            
            # It HAS to be the full S scale
            # Otherwise, the bug's still there
            platesHolder.sx >> (focalTrueSx.input2, 
                                focalTrueSy.input2, 
                                focalTrueSz.input2)

            # finally link all together...
            focalTrueSx.output >> plate.sx
            focalTrueSy.output >> plate.sy
            focalTrueSz.output >> plate.sz

        
        # Hide controller template
        controllerTemplate.hide()
        
        'DEV';
        for x in sizeList: 
            print x
        '/DEV';


        # ??? Scale the plane following the frustum
        # ??? mayaUnits=cm, focalLenght=mm, cameraAperture=inches, 1inch=2.54cm
        apertureX = (maxWidth  * 0.1 * 6.0) / (100 * 2.54) # The size in cm of the first plate (1/10 always)
        apertureY = (maxHeight * 0.1 * 6.0) / (100 * 2.54) # Divide for 100cm, multiply for 6cm and convert in inches
        
        for cam in (cameraHD, cameraPROJ):
            camShape = cam.shapes()[0]
            camShape.horizontalFilmAperture.set(apertureX)
            camShape.verticalFilmAperture.set(apertureY)
        
        """
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
        """





linker = CameraPlatesLinker()
with UndoChunkOpen('link'):
    linker.link()









'''
def _OLD_linkCameraAndPlates(*args):
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








    #-> BETTER <--
    #--> capsule = trans.incapsulate(trans.name() + '_holder') # It works with pivots too:)
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
'''    
    


