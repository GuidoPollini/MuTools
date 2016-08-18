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