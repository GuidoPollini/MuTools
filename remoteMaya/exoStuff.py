import maya.cmds as MC

def exoExport(*args):
    nodes          = ['ch_litth:mane','ch_litth:body']
    path           = 'Y:/01_SAISON_4/07_WIP/3D/__DEBUG_PROD/ALEMBIC/cloud.abc'
    animStartTime  = MC.playbackOptions(query=True, animationStartTime=True)
    animEndTime    = MC.playbackOptions(query=True, animationEndTime=True)
    purePointCache = 1 # 1->pointCache, 0->wholeMesh
       
    nodes = ','.join(nodes) # [a, b, ...] --> a,b,...
    
    # Preset for "surface & normals" (saves the whole mesh data, i.e. vertices/edges/faces)
    exoAttrs = {'ogawa':            1,
                'objects':          nodes,
                'filename':         path,

                'in':               animStartTime,
                'out':              animEndTime,
                'step':             1,
                'substep':          1,
                  
                'purepointcache':   0, # Stores or not edge/face data
                'normals':          1,
                'uvs':              1,
                'facesets':         1, # Face objectSets
                
                'useInitShadGrp':   0, # Per-face shading

                'globalspace':      0, # Apply the transformation to the mesh
                'withouthierarchy': 0,
                'transformcache':   0, # Save only transform data
                'dynamictopology':  0, # Not for a basic mesh                                   
    }
        
    if purePointCache == 1:
        # Saves only vertex positions (no edge/face data)
        exoAttrs['purepointcache'] = 1
        exoAttrs['normals']        = 0
        exoAttrs['uvs']            = 0
        exoAttrs['facesets']       = 0
    
    exoCommand = ''
    for attr in exoAttrs:
        exoCommand += '{0}={1};'.format(attr, exoAttrs[attr])    
    
    print exoCommand

    MC.ExocortexAlembic_export(j=exoCommand)

exoExport()



import maya.cmds as MC
from pprint import pprint

# Oppure controlla i namespace e aggiungi una piccola icona per far
# vedere quando e in referenza

def getReferenceData(*args):
    referencedFiles = MC.file(query=True, reference=True)
    referenceData = {}
    
    for filePath in referencedFiles:
        namespace = MC.file(filePath, query=True, namespace=True)
        
        # Check for the 'RenderSet' (ex: ch_guido:RenderSet)
        renderSetName = namespace + ':RenderSet'
        if MC.objExists(namespace + ':RenderSet') and MC.nodeType(renderSetName) == 'objectSet':
            referenceData[namespace] = (filePath, renderSetName)
        else:    
            referenceData[namespace] = filePath

    return referenceData
    
pprint(getReferenceData())   



import maya.cmds as MC
from pprint import pprint

# Oppure controlla i namespace e aggiungi una piccola icona per far
# vedere quando e in referenza

def getReferenceData(*args):
    referencedFiles = MC.file(query=True, reference=True)
    referenceData = {}
    
    for filePath in referencedFiles:
        namespace = MC.file(filePath, query=True, namespace=True)
        
        # Check for the 'RenderSet' (ex: ch_guido:RenderSet)
        renderSetName = namespace + ':RenderSet'
        if MC.objExists(namespace + ':RenderSet') and MC.nodeType(renderSetName) == 'objectSet':
            referenceData[namespace] = (filePath, renderSetName)
        else:    
            referenceData[namespace] = (filePath, None)

    return referenceData
    
pprint(getReferenceData())        


"""
import maya.cmds     as MC
import maya.OpenMaya as OM

def getWorldChildren():
    worldChildren = []

    # Initialized to a fake "world" (not a kTransform)
    DAGIter = OM.MItDag(OM.MItDag.kBreadthFirst) 

    selList = OM.MSelectionList()
    fn = OM.MFnTransform()
        
    while True:
        DAGIter.next() # Skip the first one (a "fakeWorld")
        nodePtr = DAGIter.currentItem()
        if DAGIter.depth() == 1:
            if nodePtr.apiType() == OM.MFn.kTransform:
                fn.setObject(nodePtr)
                nodeName = fn.partialPathName()
                if MC.objExists(nodeName):
                    # To avoid "weird" transforms like "|groundPlane_transform"
                    # which exist, but invisible to MEL
                    worldChildren.append(nodeName)
        else:
            break
    return worldChildren

rootTransforms = [x for x in getWorldChildren() if '_UI' not in x and x not in ['persp', 'top', 'front', 'side']]    
for x in rootTransforms:
    print x
    
"""    


def getFolders(dirName, fullName=False):
    dirContent = os.listdir(dirName)
    prefix = dirName + '/' if fullName else ''        
    folders = [prefix + x for x in dirContent if os.path.isdir(dirName + '/' + x)]
    return folders

def getFiles(dirName, fullName=False):
    dirContent = os.listdir(dirName)
    prefix = dirName + '/' if fullName else ''        
    files = [prefix + x for x in dirContent if os.path.isfile(dirName + '/' + x)]
    return files
     