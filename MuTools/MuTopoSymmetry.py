import maya.OpenMaya     as OM
import maya.api.OpenMaya as OM20
import maya.cmds         as MC

print ">>> 'MuTopoSymmetry' reloaded!"

def analyze(meshName):
    print '> Analyzing:', meshName
    

    # bb = MC.polyEvaluate(meshName, boundingBox=True, accurateEvaluation=True)
    # BBMin = (bb[0][0], bb[1][0], bb[2][0])
    # BBMax = (bb[0][1], bb[1][1], bb[2][1])
    
    # Note: this is the boundingBox in the coordinate space of this node (i.e. local)
    #       The viewport will draw the transformed boundingBox
    minBB    = MC.getAttr(meshName + '.boundingBoxMin')[0]
    maxBB    = MC.getAttr(meshName + '.boundingBoxMax')[0]
    centerBB = MC.getAttr(meshName + '.center')[0]

    widthBB, heightBB, depthBB = [maxBB[i] - minBB[i] for i in (0, 1, 2)]

    bbName = '_boundingBox'
    if MC.objExists(bbName):
    	MC.delete(bbName)
    cube = MC.polyCube(name=bbName, width=widthBB, height=heightBB, depth=depthBB, constructionHistory=False)[0]
    MC.setAttr(bbName + '.t', *centerBB)
    MC.select(cl=True)


    
    

    """
    selList = OM20.MSelectionList()
    selList.add(meshName)
    mObj = selList.getDependNode(0)
    ptr = OM20.MFnMesh(mObj)

    points = ptr.getPoints()
    """

