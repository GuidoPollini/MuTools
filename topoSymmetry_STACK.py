import maya.cmds as MC
from pprint import pprint





MESH_TRANSFORM = "XXX"



def getEdgesFromFace(face):
    # Format:
    # [u'FACE    110:    261    263   1744    260 \n']
    edges = MC.polyInfo(MESH_TRANSFORM + ".f[" + face + "]", faceToEdge=True)[0].split()[2:]
    return edges
    
def getFacesFromEdge(edge):
    # Format:
    # [u'EDGE    335:    388    412 \n']   
    faces = MC.polyInfo(MESH_TRANSFORM + ".e[" + edge + "]", edgeToFace=True)[0].split()[2:]
    return faces
    
def getVerticesFromEdge(edge):
    # Format:
    # [u'EDGE   2091:    336    660 \n']  
    vertices = MC.polyInfo(MESH_TRANSFORM + ".e[" + edge + "]", edgeToVertex=True)[0].split()[2:]
    return vertices

def getOrderedEdges(face, startEdge, startVertex):
    # BE HYPERFAST HERE!!!
    edges = getEdgesFromFace(face)
    numEdges = len(edges)
    edgesData = [None] * numEdges 
    
    temp = getVerticesFromEdge(startEdge)
    nextVertex = temp[0] if temp[0] != startVertex else temp[1]
    orderedEdges = []
    
    ind = 0
    for i in range(numEdges):
        if edges[i] == startEdge:
            continue
        vtx = getVerticesFromEdge(edges[i])
        edgesData[ind] = [edges[i], vtx[0], vtx[1]]
        ind += 1
        
    orderedEdges = list()
    for i in range(numEdges - 1):
        for j in range(numEdges - 1):
            if edgesData[j][0] is None:
                continue
            
            for index in [1, 2]:
                if nextVertex == edgesData[j][index]:
                    tmp = getFacesFromEdge(edgesData[j][0])
                    if len(tmp) == 1:
                        # BOUNDARY
                        nextFace = ""
                    else:
                        nextFace = tmp[0] if tmp[0] != face else tmp[1]
                    orderedEdges.append((nextFace, edgesData[j][0], nextVertex))
                    
                    nextVertex = edgesData[j][3 - index]
                    edgesData[j][0] = None
                    
                    break
                
    return orderedEdges
    
#pprint(getOrderedEdges("45", "109", "53"))    
       

    
        


#---------------------------------------------------------------------------------------
# CORE
#---------------------------------------------------------------------------------------

VTX_CENTER = [] # [c0, c1, ...]
VTX_LEFT   = [] # [l0, l1, l2, l3, ...]
VTX_RIGHT  = [] # [r0, r1, r2, r3, ...]

EDGE_CENTER = [] # [c0, c1, ...]
EDGE_LEFT   = [] # [l0, l1, l2, l3, ...]
EDGE_RIGHT  = [] # [r0, r1, r2, r3, ...]

def symmetricTraversal(L_face, L_edge, L_vertex, 
                       R_face, R_edge, R_vertex):

    MC.select(MESH_TRANSFORM + ".f[" + L_face + "]", MESH_TRANSFORM + ".f[" + R_face + "]", add=True)
    MC.refresh()

    # list or corresponding edges, well ordered!    
    L_orderedEdges = getOrderedEdges(L_face, L_edge, L_vertex) # [(face1, edge1, vertex1, vertex2), ...]
    R_orderedEdges = getOrderedEdges(R_face, R_edge, R_vertex) # [(face1, edge1, vertex1, vertex2), ...]
    
    if len(L_orderedEdges) != len(R_orderedEdges):
        MC.error("[ERROR] Not topoSymmetric!")

    for i in range(len(L_orderedEdges)):
        if L_orderedEdges[i][1] == R_orderedEdges[i][1]:
            # It's a CENTRAL_EDGE
            #VTX_CENTER.append(L_orderedEdges[i][3]) # Add the second vertex of the exit
            EDGE_CENTER.append(L_orderedEdges[i][1])
            continue
        
        status = (L_orderedEdges[i][1] in EDGE_LEFT) + (R_orderedEdges[i][1] in EDGE_RIGHT)
        if status == 0:
            # Both unprocessed!

            if (L_orderedEdges[i][0], R_orderedEdges[i][0]) == ("", ""):
                # Boundary; nothing to do!
                #VTX_LEFT.append(L_orderedEdges[i][3]) # Add the second vertex of the exit
                #VTX_RIGHT.append(R_orderedEdges[i][3])
                EDGE_LEFT.append(L_orderedEdges[i][1])
                EDGE_RIGHT.append(R_orderedEdges[i][1])                
                continue

            # If we get here, everything went well and we can proceed.          
            #VTX_LEFT.append(L_orderedEdges[i][3]) # Add the second vertex of the exit
            #VTX_RIGHT.append(R_orderedEdges[i][3])
            EDGE_LEFT.append(L_orderedEdges[i][1])
            EDGE_RIGHT.append(R_orderedEdges[i][1])

            symmetricTraversal(L_orderedEdges[i][0], L_orderedEdges[i][1], L_orderedEdges[i][2], 
                               R_orderedEdges[i][0], R_orderedEdges[i][1], R_orderedEdges[i][2])


        elif status == 1:
            # One is processed, the other not! Asymmetry
            MC.error("ASYMMETRY")
        elif status == 2:
            # Already processed  
            continue


    
def topoSymmetryUI(*args):
    startEdge   = "50"
    startVertex = getVerticesFromEdge(startEdge)[0] # Random:)
    startFaces  = getFacesFromEdge(startEdge)
    
    EDGE_CENTER.append(startEdge)

    # STACK FORMAT
    # ( (Lface, Ledge, Lvtx), (Rface, Redge, Rvtx) )
    stack = list()
    stack.append( ((startFaces[0], startEdge, startVertex), (startFaces[1], startEdge, startVertex)) )



    startTime = MC.timerX() 

    while stack:
        # Pop the last pair of the stack
        # FORMAT: *ToProcess = (face, edge, vtx)
        L_toProcess, R_toProcess = stack.pop()
        #MC.select(MESH_TRANSFORM + ".f[" + L_toProcess[0] + "]", MESH_TRANSFORM + ".f[" + R_toProcess[0] + "]", add=True)
        #MC.refresh()
        
        # PROCESS the exits and POPULATE the stack
        L_orderedEdges = getOrderedEdges(L_toProcess[0], L_toProcess[1], L_toProcess[2]) # [(face1, edge1, vertex1), ...]
        R_orderedEdges = getOrderedEdges(R_toProcess[0], R_toProcess[1], R_toProcess[2])        

        if len(L_orderedEdges) != len(R_orderedEdges):
            MC.error("[ERROR] Not topoSymmetric!")

        for i in range(len(L_orderedEdges)):
            if L_orderedEdges[i][1] == R_orderedEdges[i][1]:
                # It's a CENTRAL_EDGE
                EDGE_CENTER.append(L_orderedEdges[i][1])
                continue
            
            status = (L_orderedEdges[i][1] in EDGE_LEFT) + (R_orderedEdges[i][1] in EDGE_RIGHT)
            if status == 0:
                # Both unprocessed!
                if (L_orderedEdges[i][0], R_orderedEdges[i][0]) == ("", ""):
                    # Boundary; nothing to do!
                    EDGE_LEFT.append(L_orderedEdges[i][1])
                    EDGE_RIGHT.append(R_orderedEdges[i][1])                
                    continue

                # If we get here, everything went well and we can proceed.          
                EDGE_LEFT.append(L_orderedEdges[i][1])
                EDGE_RIGHT.append(R_orderedEdges[i][1])
                
                # Populate the stack
                stack.append( ((L_orderedEdges[i][0], L_orderedEdges[i][1], L_orderedEdges[i][2]), 
                               (R_orderedEdges[i][0], R_orderedEdges[i][1], R_orderedEdges[i][2])) )

            elif status == 1:
                # One is processed, the other not! Asymmetry
                MC.error("ASYMMETRY")
            elif status == 2:
                # Already processed  
                continue


    print "[ELAPSED TIME] ", MC.timerX(startTime=startTime)

    CENTER = [MESH_TRANSFORM + ".e[" + x + "]"  for x in EDGE_LEFT]
    MC.select(CENTER, r=True) 


