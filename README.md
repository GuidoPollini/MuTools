#MuTools
- **MuCore**: a lightweight pointer-based wrapping of all Maya standard nodal hierarchy and commandEngine (CG9-style, not the hyper complex and heavy PyMel). The goal is to be able to write fluently and OOP rig macros;
- **MuUI**: a Qt-wrap of the shitty commandEngine UI, plus a MVC structure compatible with rig modules;
- **MuRig**: a system to recycle a rig pattern (a "macro", the "Mu" in the module name) with the least effort possible (no loss in performance, not obliged to follow a rigid pipeline, friendly).

**MuCore**

DGNode
  longName
  name
  shortName
  
DAGNode
- getParent()
- isInstanced()
  
Transform
- getChildren()
- getMesh()
- getMeshes()
- isPureTransform()
- isMeshTransform()
  
Mesh
- getSmoothMeshDict()
- setSmoothMesh()
  



Context managers:
```python
with RenderLayerActive(layerName) as layerNode:
    layerNode.name = 'fucked-up'
```    

  
