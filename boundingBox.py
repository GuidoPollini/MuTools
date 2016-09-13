import maya.cmds as MC
meshName = 'bodyShape'


# ((xmin,xmax), (ymin,ymax), (zmin,zmax))
bb = MC.polyEvaluate(meshName, boundingBox=True, accurateEvaluation=True)
_BBMin = (bb[0][0], bb[1][0], bb[2][0])
_BBMax = (bb[0][1], bb[1][1], bb[2][1])

BBMin = MC.getAttr(meshName + '.boundingBoxMin')[0]
BBMax = MC.getAttr(meshName + '.boundingBoxMax')[0]
BBCenter = MC.getAttr(meshName + '.center')[0]


print BBMin
print _BBMin

print BBMax
print _BBMax

print BBCenter
