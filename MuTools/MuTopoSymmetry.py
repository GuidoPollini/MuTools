import maya.OpenMaya     as OM
import maya.api.OpenMaya as OM20
import maya.cmds         as MC

import MuTools.MuUtils   as Utils
import MuTools.MuCore    as Core
import MuTools.MuScene   as Scene


"""
from math import sqrt
def minDist_bruteForceTriple(triple):
    #triple = ((x1, y1, z1), (x2, y2, z2), (x3, y3, z3))   
    u, v, w = triple
    return sqrt(min((u[0] - v[0])**2 + (u[1] - v[1])**2 + (u[2] - v[2])**2,
                    (u[0] - w[0])**2 + (u[1] - w[1])**2 + (u[2] - w[2])**2,
                    (v[0] - w[0])**2 + (v[1] - w[1])**2 + (v[2] - w[2])**2))
"""


def analyze(node):    
    # node --> <DAGNode>
    
    if node.type() != 'mesh' and not node.isMeshTransform():
        MC.error('Invalid node!')

    mesh = node.mesh()
    print '> Analyzing:', mesh.name()

    # bb = MC.polyEvaluate(nodeName, boundingBox=True, accurateEvaluation=True)
    # BBMin = (bb[0][0], bb[1][0], bb[2][0])
    # BBMax = (bb[0][1], bb[1][1], bb[2][1])
    
    # Note: this is the boundingBox in the coordinate space of this node (i.e. local)
    #       The viewport will draw the transformed boundingBox

    geoEpsilon = 0.001       # 
    epsilon    = 0.00000001  # 

    minBB    = mesh.boundingBoxMin.get()[0]
    maxBB    = mesh.boundingBoxMax.get()[0]
    centerBB = mesh.center.get()[0]

    widthBB, heightBB, depthBB = [maxBB[i] - minBB[i] for i in (0, 1, 2)]
    


    """
    bbName = '_boundingBox_' + mesh.name()
    if MC.objExists(bbName):
    	MC.delete(bbName)
    cube = Core.MuNode(MC.polyCube(name=bbName, width=widthBB, height=heightBB, depth=depthBB, constructionHistory=False)[0])
    cube.t.set(*centerBB)
    Scene.select()
    """



    selList = OM20.MSelectionList()
    selList.add(mesh.name())
    
    mObj = selList.getDependNode(0)
    DAGPath = selList.getDagPath(0)

    ptr = OM20.MFnMesh(mObj)

    mPoints = ptr.getPoints(space=OM20.MSpace.kObject) # --> a list of MPoints
    points = [(p.x, p.y, p.z) for p in mPoints]
    print len(points)
    #print points


    numDivisions = 40 # Must be even
    stepX = widthBB/float(numDivisions)
    stepY = heightBB/float(numDivisions)
    stepZ = depthBB/float(numDivisions)

    cube = [[[[] for indZ in range(numDivisions)] for indY in range(numDivisions)] for indX in range(numDivisions)]
    # cube[indX][indY][indZ] for indX, indY, indZ=0, ..., numDivisions    

    #nonEmptyCubes = []
    for i, point in enumerate(points):
        indX = int((point[0] - minBB[0]) // stepX)
        indY = int((point[1] - minBB[1]) // stepY)
        indZ = int((point[2] - minBB[2]) // stepZ)
        try:
            cube[indX][indY][indZ].append(i)
            #nonEmptyCubes.append((indX, indY, indZ))
        except:
            print 'BORDER ERROR:', indX, indY, indZ

    vertices = OM.MIntArray()    
    #for ijk in nonEmptyCubes:
    #    if cube[ijk[0]][ijk[1]][ijk[2]]:
    #        vertices.extend(cube[ijk[0]][ijk[1]][ijk[2]])
    
    for indX in range(numDivisions // 2):
        for indY in range(numDivisions):
            for indZ in range(numDivisions):
                if cube[indX][indY][indZ]:
                    #vertices.extend(cube[indX][indY][indZ])
                    for x in cube[indX][indY][indZ]:
                        vertices.append(x)


    component = OM.MFnSingleIndexedComponent()
    mObjComponent = component.create(OM.MFn.kMeshVertComponent)
    component.addElements(vertices)

    selList = OM.MSelectionList()
    selList.add(mesh.name())
    dagPath = OM.MDagPath()
    selList.getDagPath(0, dagPath)
    selList = OM.MSelectionList()
    selList.add(dagPath, mObjComponent)
    OM.MGlobal.setActiveSelectionList(selList)
    # HOW TO SELECT THINGS WITH THE API 2.0?????
    # the shitty MGlobal has practically nothing and MSelectionList no selection...
    # Im missing somethign or is it REALLY A BIG PILE OF SHIT (incomplete)???
    #x = OM20.MSelectionList()
    #for l in dir(x):
    #    print l
    #OM20.MGlobal.setActiveSelectionList(selList)



    #verticeNames = ['body.vtx[{}]'.format(x) for x in vertices]
    #MC.select(verticeNames, r=True)

