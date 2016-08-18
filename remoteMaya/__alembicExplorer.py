import alembic as AL
INDENT = 2
LIMITER = 999 # 



def visitSmallArraySamples(prop, depth):
    print "SMALL ARRAY"
    for i, s in enumerate(prop.arraySamples):
        print " "*depth,
        if s is None:
            print "XX"
        else:
            for j in s:
                print j,
            print
    
        if i > LIMITER:
            break

def visitScalarSamples(prop, depth):
    for i, s in enumerate(prop.scalarSamples):
        print " "*depth + str(s)
        if i > LIMITER:
            break     

def visitArraySamples(prop, depth):
    for i, s in enumerate(prop.samples):
        print " "*depth,
        if s is None:
            print "XX"
        else:
            for j in s:
                print j,
            print 

        if i > LIMITER:
            break
            
def visitCompoundProperty(prop, depth):
    print " "*depth + "[" + prop.getName() + "] COMPOUND", prop.getMetaData().get("schema")
    if prop.getName() == ".geom" or "faceset" in prop.getName():
        pass
        #print " "*depth + "  TOO LONG"
        #return 
    visitProperties(prop, depth + INDENT)

def visitSimpleProperty(prop, depth):
    propType = "SCALAR" if prop.isScalar() else "ARRAY"
    print " "*depth + "[" + prop.getName() + "]", propType, prop.getDataType(), prop.getNumSamples() 
    

    if prop.isScalar():
        if prop.getDataType().getExtent() == 1:
            visitScalarSamples(prop, depth + INDENT)
        elif len(prop.getMetaData().get("interpretation")) > 0:
            visitScalarSamples(prop, depth + INDENT)
        else:          
            visitSmallArraySamples(prop, depth+2)
    else:
        visitArraySamples(prop, depth+2)

def visitProperties(object, depth):
    for header in object.propertyheaders:
        prop = object.getProperty(header.getName()) # --> ICompoundProperty

        if header.isCompound():
            visitCompoundProperty(prop, depth)
        elif header.isScalar() or header.isArray():
            visitSimpleProperty(prop, depth)

def visitIObject(object, depth=0):
    print " "*depth + "[" + object.getName() + "]"
    visitProperties(object.getProperties(), depth)
    print ""
    for child in object.children:
        visitIObject(child, depth + INDENT)

def visitIArchive(path):
    visitIObject(AL.Abc.IArchive(path).getTop())
    
    
class AlembicNavigator(object):
    def __init__(self, path):
        self._ia = AL.Abc.IArchive(path)
        #self.name = self._ia.getName() # Archive path
        self.root = self._ia.getTop() # --> <IObject>
        #print self.root.getName(), self.root.getFullName() 
        # ex:
        # fur03 /rig_group/Geometries/fur/fur03

        
#pippo = AlembicNavigator("Y:/01_SAISON_4/07_WIP/3D/__DEBUG_PROD/ALEMBIC/palla.abc")    


path = "Y:/01_SAISON_4/07_WIP/3D/__DEBUG_PROD/wolve_test.abc"
root = AL.Abc.IArchive(path).getTop()



def visitIObject(object, depth=0):
    # skip the root, which is an anomaly:
    if depth != 0:
        metaData = object.getMetaData() # --> <MetaData>... kinda dictionary
        schemaTag = metaData.get("schema")
        print "  "*depth + "" + object.getName() + "(" + schemaTag + ")"
    
        props = object.getProperties() # --> <ICompoundProperty>
        for i in range(props.getNumProperties()):
            prop = props.getProperty(i) # --> <ICompoundProperty>

            # Stuff from  <AL.Abc.IBaseProperty_Compound>
            """
            print prop.getName()
            print prop.isArray()
            print prop.isCompound()
            print prop.isScalar()
            print prop.isSimple()
            """
            info =  "  "*depth + "-" + prop.getName() + "  " + ("COMP" if  prop.isCompound() else "SIMPLE") 
            print info
            for i in range(prop.getNumProperties()):
                subProp = prop.getProperty(i)
                info2 =  "  "*depth + " -" + subProp.getName() + "  " + ("COMP" if  subProp.isCompound() else "SIMPLE") 
                print info2
                
                for bof, samp in enumerate(subProp.samples):
                    if bof > 4:
                        break
                    print "  "*depth + "  -", str(samp) 
                print

    
        print
    # "schema=fuckYou; ..."
    
    """
    metaDataString = metaData.serialize() # a string
    tokens = metaDataString.split(";")
    for token in tokens:
        data = token.split("=")
        print "  "*(depth) + "-" + data[0] + " -> " + data[1]
        metaTags.add(data[0])
    
    print 
    """
    for child in object.children:
        visitIObject(child, depth + 1)

visitIObject(root)
for i in AL.AbcCoreAbstract.MetaData.mro():
    print i
    
    
"""
object -> Boost.Python.instance -> AL.Abc.IObject
object -> Boost.Python.instance -> AL.AbcCoreAbstract.MetaData
object -> Boost.Python.instance -> AL.Abc.IBaseProperty_Compound -> AL.Abc.ICompoundProperty
"""
#visitIArchive("Y:/01_SAISON_4/07_WIP/3D/__DEBUG_PROD/ALEMBIC/palla.abc")    
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------





















def traverseXForms(IObject, dataToDump):
    floatingPointLimit = 1e-11 
    metaData= IObject.getMetaData()
    # check if it's an XForm
    if AL.AbcGeom.IXform.matches(metaData):
        IXformWrap = AL.AbcGeom.IXform(IObject, AL.Abc.WrapExistingFlag(1)) 
        numSamples = IXformWrap.getSchema().getNumSamples()
        
        if ALEMBIC_DEBUG: print IObject.getName(), numSamples 
        xformName = IObject.getName()
        if IXformWrap.getSchema().isConstant():
            # STATIC, just get the first value
            scaleValue = IXformWrap.getSchema().getValue(AL.Abc.ISampleSelector(0)).getScale()[0]
            if 0 < scaleValue < floatingPointLimit:
                # zero is correct...
                # we found an anomaly; save the correction
                dataToDump[xformName] = floatingPointLimit
                if ALEMBIC_DEBUG: print "STATIC", scaleValue 
        else:
            if ALEMBIC_DEBUG: print "ANIMATED"
            # ANIMATED!!!
            # now enter in the array and correct all the small numbers...
            # !!! Exocortex fails only if there's an <1e-12... otherwise is a valid bake
            isValidBake = True
            bake = []
            for i in range(numSamples):
                #        IXform -> IXformSchema -> XformSample        
                
                #scaleSample = IXformWrap.getSchema().getValue(AL.Abc.ISampleSelector(i)).getScale()[0]
                scaleSample = IXformWrap.getSchema().getValue(i).getScale()[0]

                #print "FUCK ", IXformWrap.getSchema().getValue(i).getScale()
                
                #print "[" + str(i) + "] = " + str(scaleSample)
                if 0 < scaleSample < floatingPointLimit:
                    # there's an invalid value
                    bake.append(0)
                    isValidBake = False
                else:
                    # dion't change
                    bake.append(scaleSample)     
            
            if not isValidBake:
                # exocortex will fail: save the corrected bake
                print "\nxformName = ", xformName
                print "bake = ", bake
                dataToDump[xformName] = bake
    # now proceed to its children
    for IObjectChild in IObject.children:
        traverseXForms(IObjectChild, dataToDump)

def save3DsMaxData(*args):
    alembicPaths = set()

    # Here we cheat, gather all exocortex node and recover the file info
    exoNodes = MC.ls(type="ExocortexAlembicFile")

    for exoNode in exoNodes:
        
        # Avoid "ExocortexAlembicFile" parasites by checking output connections
        connections = MC.listConnections(exoNode + ".outFileName", source=False, destination=True) or []
        print "\nOUTPUT CONNECTIONS ", exoNode, " --> ", len(connections)
        if len(connections) == 0:
            # PARASITE: skip it
            print "PARASITE: skipped!!!"
            continue

        fileNameRaw = MC.getAttr(exoNode + ".fileName")
        print "EXONODE: ", exoNode, "\nFILERAW: ", fileNameRaw
        # the fucking $PROD_SERVER tag
        if "$PROD_SERVER" in fileNameRaw: 
            fileNameClean = fileNameRaw.replace("$PROD_SERVER", "Y:")
        else: 
            fileNameClean = fileNameRaw    
        print fileNameClean 

        tokens = fileNameClean.split("\\")
        # we need only CH and PR, nothing more
        if "_ch_" in tokens[-1] or "_pr_" in tokens[-1]:
            alembicPaths.add(fileNameClean)

    alembicPaths = list(alembicPaths) 

    # now perform a recursion and store the results in a dictionary
    dataToDump = {}    
    progressBarInitialize(len(alembicPaths))
    for alembicPath in alembicPaths:
        alembicName = (alembicPath.split("/"))[-1]
        printLog("EXTRACTING SCALE FROM ALEMBIC: " + alembicName)
        print "ALEMBIC FILE = ", alembicPath
        printLog("")

        try:
            IRoot = AL.Abc.IArchive(str(alembicPath)).getTop()        
        except Exception as error:
            fatality("ALEMBIC I/O ERROR: can't open the \".abc\" file (bad naming or missing)\nNODE = " + exoNode + "\nPATH = " + alembicPath)
                    
        traverseXForms(IRoot, dataToDump)
        progressBarIncrement()
    progressBarHide()    

    # dataToDump is ready to be "dumped"...
    dataFor3DSMax["scaleData"] = dataToDump



    #----------------------------------------------------
    #----------------------------------------------------
    # "PURE" TRANSFORM VISIBILITY
    #----------------------------------------------------
    #----------------------------------------------------
    printLog("CHECKING \"PURE TRANSFORMS\" VISIBILITY ANIMATION")

    dataFor3DSMax["pureTransformVisibility"] = {}

    allTransforms = MC.ls(type="transform")
    pureTransforms ={}
    for transform in allTransforms:
        shapes = MC.listRelatives(transform, shapes=True) or []
        if len(shapes) == 0:
            # It's a pureTransform
            pureTransforms[transform] = []

    startTime = int(MC.playbackOptions(query=True, minTime=True)) 
    endTime   = int(MC.playbackOptions(query=True, maxTime=True))
    
    try:
        MM.eval("paneLayout -e -manage false $gMainPane") 
        progressBarInitialize(endTime - startTime)

        for time in range(startTime, endTime + 1):
            for transform in pureTransforms:
                MC.currentTime(time, update=True)
                pureTransforms[transform].append(int(MC.getAttr(transform + ".visibility")))
            progressBarIncrement()
    
    finally:
        MM.eval("paneLayout -e -manage true $gMainPane")
        progressBarHide()    

    for x in pureTransforms:
        temp = set(pureTransforms[x])
        if len(temp) > 1:
            # It's animated, save it
            dataFor3DSMax["pureTransformVisibility"][x] = pureTransforms[x]
    
    # Simply delete the key if no pureTransforms' vis animation was found 
    if len(dataFor3DSMax["pureTransformVisibility"]) == 0:
        del dataFor3DSMax["pureTransformVisibility"]
     

    #----------------------------------------------------
    #----------------------------------------------------
    # SCENE DATA
    #----------------------------------------------------
    #----------------------------------------------------
    dataFor3DSMax["imageSize"] = [MC.getAttr("defaultResolution.width"), 
                                  MC.getAttr("defaultResolution.height")]

    episode, shot = getProperEpisodeShotName()
    if None not in (episode, shot):
        cameraType = getShotCameraType_shotGun(episode, "sh" + shot)
        try:
            cameraName = MC.ls("*camera" + cameraType, recursive=True)[0]
        except:
            fatality("Can't find the proper camera!")
        dataFor3DSMax["cameraName"] = cameraName # naming convention ("YKR405", "sh012")                               
    else:
        dataFor3DSMax["cameraName"] = None   



    #----------------------------------------------------
    #----------------------------------------------------
    # SMOOTHNESS
    #----------------------------------------------------
    #----------------------------------------------------
    dataFor3DSMax["renderingSmoothness"] = {}

    meshes = MC.ls(type="mesh", noIntermediate=True, long=True, visible=True) or [] # not really necessary here; LS returns not None, but []
    progressBarInitialize(numberOfTasks=len(meshes))

    for mesh in meshes:
        smoothness = MC.getAttr(mesh + ".renderSmoothLevel")
        parent = MC.listRelatives(mesh, parent=True, path=False)[0] # should return the "minimal" path required
        dataFor3DSMax["renderingSmoothness"][parent] = smoothness
        progressBarIncrement()
    progressBarHide()  

    
    if len(meshes) == 0:
        # nothing to do , return
        printLog("No valid mesh found!", "NULL")
        return
    
    # DEBUG
    #pprint(dataFor3DSMax["renderingSmoothness"])
    

    pprint(dataFor3DSMax)
    return
    
    #------------------------------------------------------
    #------------------------------------------------------
    # NOW SAVE 
    #------------------------------------------------------  
    #------------------------------------------------------
    
    # The name of the .txt has to be like this:
    #  "YKR405_012_DATAFOR3DSMAX.txt"
    #  "YKR405_012B_DATAFOR3DSMAX.txt"
    #  "YKR405_012_B_DATAFOR3DSMAX.txt"

    episode, shot = getProperEpisodeShotName()
