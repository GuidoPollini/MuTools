-------------------------------------------------------------------------------
MUTOOLS MODULES DEPENDENCY
-------------------------------------------------------------------------------

     MuUtils (ROOT)
      MuCore  <--  [ MuUtils                     ]
     MuScene  <--  [ MuUtils MuCore              ]
        MuUI  <--  [ MuUtils                     ]
MuMayaRemote  <--  [ MuUtils MuCore MuScene MuUi ]


Locally, each module must follow this import rule:
  import MuTools.MuCore  as Core
  import MuTools.MuScene as Scene
  import MuTools.MuUI    as UI
  import MuTools.MuUtils as Utils

Every script/module should have access to 'Core/Utils/Scene' namespaces!  

The following names are reference to the moduleObject (singleton) 'MuTools.MuUtils':
  MuTools.MuMayaRemote.Utils
  MuTools.MuMayaRemote.Core.Utils
  MuTools.MuMayaRemote.Scene.Utils
  MuTools.MuMayaRemote.Scene.Core.Utils
  MuTools.MuMayaRemote.UI.Utils


(NO CYCLIC REFERENCES PLEASE and keep it simple!)    
