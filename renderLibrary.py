"""
==================================================================================================================================================
--------------------------------------------------------------------------------------------------------------------------------------------------
     YYYYYYY       YYYYYYY           AAA               KKKKKKKKK    KKKKKKK               AAA               RRRRRRRRRRRRRRRRR   IIIIIIIIII
     Y:::::Y       Y:::::Y          A:::A              K:::::::K    K:::::K              A:::A              R::::::::::::::::R  I::::::::I
     Y:::::Y       Y:::::Y         A:::::A             K:::::::K    K:::::K             A:::::A             R::::::RRRRRR:::::R I::::::::I
     Y::::::Y     Y::::::Y        A:::::::A            K:::::::K   K::::::K            A:::::::A            RR:::::R     R:::::RII::::::II
     YYY:::::Y   Y:::::YYY       A:::::::::A           KK::::::K  K:::::KKK           A:::::::::A             R::::R     R:::::R  I::::I  
        Y:::::Y Y:::::Y         A:::::A:::::A            K:::::K K:::::K             A:::::A:::::A            R::::R     R:::::R  I::::I  
         Y:::::Y:::::Y         A:::::A A:::::A           K::::::K:::::K             A:::::A A:::::A           R::::RRRRRR:::::R   I::::I  
          Y:::::::::Y         A:::::A   A:::::A          K:::::::::::K             A:::::A   A:::::A          R:::::::::::::RR    I::::I  
           Y:::::::Y         A:::::A     A:::::A         K:::::::::::K            A:::::A     A:::::A         R::::RRRRRR:::::R   I::::I  
            Y:::::Y         A:::::AAAAAAAAA:::::A        K::::::K:::::K          A:::::AAAAAAAAA:::::A        R::::R     R:::::R  I::::I  
            Y:::::Y        A:::::::::::::::::::::A       K:::::K K:::::K        A:::::::::::::::::::::A       R::::R     R:::::R  I::::I  
            Y:::::Y       A:::::AAAAAAAAAAAAA:::::A    KK::::::K  K:::::KKK    A:::::AAAAAAAAAAAAA:::::A      R::::R     R:::::R  I::::I  
            Y:::::Y      A:::::A             A:::::A   K:::::::K   K::::::K   A:::::A             A:::::A   RR:::::R     R:::::RII::::::II
         YYYY:::::YYYY  A:::::A               A:::::A  K:::::::K    K:::::K  A:::::A               A:::::A  R::::::R     R:::::RI::::::::I
         Y:::::::::::Y A:::::A                 A:::::A K:::::::K    K:::::K A:::::A                 A:::::A R::::::R     R:::::RI::::::::I
         YYYYYYYYYYYYYAAAAAAA                   AAAAAAAKKKKKKKKK    KKKKKKKAAAAAAA                   AAAAAAARRRRRRRR     RRRRRRRIIIIIIIIII
--------------------------------------------------------------------------------------------------------------------------------------------------
==================================================================================================================================================
"""



import maya.OpenMaya   as OM
import maya.cmds       as MC
import maya.mel        as MM
import json            as JSON
import maya.OpenMayaUI as OMUI
import PySide.QtGui    as QTGUI 
import PySide.QtCore   as QTC
import shiboken        as SHIBOKEN
import os              as OS
import inspect         as INSPECT
import re              as RE
import struct          as STRUCT
import alembic         as AL
import random          as RANDOM
import copy            as COPY
import string          as STRING
import datetime        as DT

from functools                        import partial
from pprint                           import *
from YAKARI_renderLibrary_preferences import *




"""
==================================================================================================================================================
--------------------------------------------------------------------------------------------------------------------------------------------------
  ,ad8888ba,   88               88                       88             
 d8"'    `"8b  88               88                       88             
d8'            88               88                       88               
88             88   ,adPPYba,   88,dPPYba,   ,adPPYYba,  88  ,adPPYba,  
88      88888  88  a8"     "8a  88P'    "8a  ""     `Y8  88  I8[    ""  
Y8,        88  88  8b       d8  88       d8  ,adPPPPP88  88   `"Y8ba,   
 Y8a.    .a88  88  "8a,   ,a8"  88b,   ,a8"  88,    ,88  88  aa    ]8I  
  `"Y88888P"   88   `"YbbdP"'   8Y"Ybbd8"'   `"8bbdP"Y8  88  `"YbbdP"'  
--------------------------------------------------------------------------------------------------------------------------------------------------
==================================================================================================================================================
"""


VERSION = "12july 17h00" # Nice formatting


# shitty global variable to share height between different UI
# (still bad procedural design: this info should be shared between objects... talking between them)
TREELIST_SIZE = 14 # max number of item showed in the treeLists
SCENE_ASSET_TREELIST_HEIGHT = 20 * TREELIST_SIZE 






#--------------------------------------------------------------------------------------------------------------------------------------------------
# Connection to SHOTGUN 
#--------------------------------------------------------------------------------------------------------------------------------------------------
ACTIVATE_SHOTGUN = True
SHOTGUN_HANDLE = None

if ACTIVATE_SHOTGUN:
    if SHOTGUN_PATH not in OS.sys.path:
        OS.sys.path.append(SHOTGUN_PATH)
    from shotgun_api3 import shotgun

def createGlobalShotGunHandle():
    global SHOTGUN_HANDLE 

    # Configure SSL validation
    shotgun.NO_SSL_VALIDATION = True
    
    # Initialize variables
    serverPath = "https://ellipsanime.shotgunstudio.com/"
    scriptName = "ellipse_packager"
    scriptKey  = "874c205a45e841393046a7e871cda1f24a2922cd06becc39ee3584246392bc36"
    
    # create global shotgun handle
    SHOTGUN_HANDLE = shotgun.Shotgun(serverPath, scriptName, scriptKey)

if ACTIVATE_SHOTGUN:
    createGlobalShotGunHandle()   
#--------------------------------------------------------------------------------------------------------------------------------------------------






#--------------------------------------------------------------------------------------------------------------------------------------------------
# DEBUGGING
#--------------------------------------------------------------------------------------------------------------------------------------------------
# I removed the debug checkbox; this shit activates:
# - 0000;finalFuncDebug()
# - 0000;finalPrintDebug(message, data)
FINAL_DEBUG = False

TEEPEE_DEBUG = False 
def teepeeDebugPrint(shit):
    if TEEPEE_DEBUG:
        print "[TEEPEE DEBUG]  ", shit





#==================================================================================================================================
#----------------------------------------------------------------------------------------------------------------------------------
# GLOBAL COLORS
#----------------------------------------------------------------------------------------------------------------------------------
#==================================================================================================================================

# BUTTON COLORS
#CYAN_L,  CYAN_B  = (100,220,220), (60,90,90)
#BLUE_L,  BLUE_B  = (100,220,230), (70,100,110)

CYAN_L, CYAN_B   = (40,40,40), (180,180,180)
BLUE_L,  BLUE_B  = (40,40,40), (255,173,49) 

GREEN_L, GREEN_B = (100,100,100), (60,110,60)                 

# creation of groupId colors
# COLD WARM COLD WARM...
# (PASTEL SHIT)
GROUPID_BUTTON_BASECOLOR = [[135, 239, 186],
                            [255, 169, 140],
                            [205, 174, 236],
                            [242, 160, 173],                            
                            [118, 228, 251], 
                            [255, 226, 129],                            
                            [129, 160, 245],
                            [255, 118, 111]
                            ]
# Normalize
for i in range(len(GROUPID_BUTTON_BASECOLOR)):
    GROUPID_BUTTON_BASECOLOR[i] = [value/255.0 for value in GROUPID_BUTTON_BASECOLOR[i]]

def getGroupIdColor(index):
    0000;finalFuncDebug()
    0000;finalPrintDebug(message="Color index requested: " + str(index))
    # simply wrap it!
    return GROUPID_BUTTON_BASECOLOR[index%8]
  
def getDarkGroupIdColor(index):
    darkColor = [c/5.0 + 0.05 for c in getGroupIdColor(index)]
    return darkColor   









#---------------------------------------------------------------------------------------------------------------------------------
# ASSETS GLOBAL DICTIONARY
#---------------------------------------------------------------------------------------------------------------------------------
# Format:
# ASSETS_DATA = {assetNamespace: [assetID,    RENPath,        AMBPath,        [amb1,  amb2,   ..., ambk]]}
# Ex:
# ASSETS_DATA = {"ch_yakar_1":   ["ch_yakar", "path_REN.txt", "path_AMB.txt", ["FIR", "SHIT", "FUCK", "FX", COO"]],
#                "ch_yakar":     ["ch_yakar", "path_REN.txt", None,           None],
#                "ch_yakar":     ["ch_yakar", None,           None,           None],
#                "ch_fuckMe":    [None,       None,           None,           None]}
ASSETS_DATA = {}

""" <== PURE ABOMINATION... bad design"""
# an horrid global to force the default of the groupId... Really a bad decision...
INITIALIZE_COMBINED_DATA_ON_REFRESH = True 






#---------------------------------------------------------------------------------------------------------------------------------
# Detect available namespaces for CHARACTERS, PROPS and SUBSETS
#---------------------------------------------------------------------------------------------------------------------------------
CHARACTER_TAGS = [x for x in OS.listdir(PROJECT_ROOT + "ch/") if OS.path.isdir(PROJECT_ROOT + "ch/" + x)]
PROP_TAGS      = [x for x in OS.listdir(PROJECT_ROOT + "pr/") if OS.path.isdir(PROJECT_ROOT + "pr/" + x)]    
SUBSET_TAGS    = [x for x in OS.listdir(PROJECT_ROOT + "ss/") if OS.path.isdir(PROJECT_ROOT + "ss/" + x)] 






#---------------------------------------------------------------------------------------------------------------------------------
# IMPORTING STUFF
#---------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------
# SHADERS
MATTE_NO_ALPHA_COLOR_LIGHT_PATH = SHADERS_PATH + "matteNoAlpha_COLOR_LIGHT.ma"
if not OS.path.isfile(MATTE_NO_ALPHA_COLOR_LIGHT_PATH):
    fatality("Can't import 'matteNoAlpha' shader!\n\nThe following file is missing:\n  -  " + MATTE_NO_ALPHA_COLOR_LIGHT_PATH)

RECEIVE_SHADOWS_CAST_SHDWS_PATH = SHADERS_PATH + "receiveShadows_CAST_SHDWS.ma"
if not OS.path.isfile(RECEIVE_SHADOWS_CAST_SHDWS_PATH):
    fatality("Can't import 'receiveShadows' shader!\n\nThe following file is missing:\n  -  " + RECEIVE_SHADOWS_CAST_SHDWS_PATH)

#------------------------------------------------
# LIGHTS
NORMAL_LIGHTS_PATH = LIGHTS_SET_PATH + "NORMAL_lights.ma"
if not OS.path.isfile(NORMAL_LIGHTS_PATH):
    fatality("Can't import NORMAL LIGHTS!\n\nThe following file is missing:\n  -  " + NORMAL_LIGHTS_PATH)

CAST_SHDWS_LIGHT_PATH = LIGHTS_SET_PATH + "CAST_SHDWS_ground.ma"
if not OS.path.isfile(CAST_SHDWS_LIGHT_PATH):
    fatality("Can't import SHADOW LIGHT!\n\nThe following file is missing:\n  -  " + CAST_SHDWS_LIGHT_PATH)












# REPORT structure
REPORT_TEXT      = "" 


# Only meshNodes need special care
MESH_DUMP_ATTRS  = ["primaryVisibility", 
                    "castsShadows", 
                    "receiveShadows"]

# NOT NECESSARY
DEFAULT_SETTINGS = []
                    #'defaultRenderGlobals.currentRenderer', 
                    #'defaultRenderGlobals.imageFilePrefix', 
                    #'defaultRenderGlobals.startFrame', 
                    #'defaultRenderGlobals.endFrame', 
                    #'miDefaultFramebuffer.datatype']

SHADER_TYPES     = ["lambert",
                    "blinn",
                    "phong", 
                    "surfaceShader", 
                    "layeredShader", 
                    "useBackground", 
                    "rampShader"]












"""
==================================================================================================================================================
--------------------------------------------------------------------------------------------------------------------------------------------------
88        88  88        88                        88  88           88  88                            
88        88  88        88                        ""  88           88  ""                            
88        88  88        88                            88           88                                
88        88  88        88,dPPYba,   88       88  88  88   ,adPPYb,88  88  8b,dPPYba,    ,adPPYb,d8  
88        88  88        88P'    "8a  88       88  88  88  a8"    `Y88  88  88P'   `"8a  a8"    `Y88  
88        88  88        88       d8  88       88  88  88  8b       88  88  88       88  8b       88  
Y8a.    .a8P  88        88b,   ,a8"  "8a,   ,a88  88  88  "8a,   ,d88  88  88       88  "8a,   ,d88  
 `"Y8888Y"'   88        8Y"Ybbd8"'    `"YbbdP'Y8  88  88   `"8bbdP"Y8  88  88       88   `"YbbdP"Y8  
                                                                                         aa,    ,88  
                                                                                          "Y8bbdP"   
--------------------------------------------------------------------------------------------------------------------------------------------------
==================================================================================================================================================
"""   

CURRENT_UIMODE = "PROD"

PREPROD_WINDOW_SIZE    = (360, 518)
PROD_WINDOW_SIZE       = (360, 980)
NODEDUMPER_WINDOW_SIZE = (360, 490)


def YAKARI_renderLibraryUI(*args):
    width  = PROD_WINDOW_SIZE[0]
    height = PROD_WINDOW_SIZE[1]
    if MC.window("YAKARI_renderLibraryUI_WIN", ex=1):
        MC.deleteUI("YAKARI_renderLibraryUI_WIN") 
    MC.window("YAKARI_renderLibraryUI_WIN", t="YAKARI render tools                                                 " + VERSION, tlb=1, s=0, mb=0)








    GLOBAL_FORM = MC.formLayout("GLOBAL_FORM", nd=100)

    YAKARI_LOGO = MC.symbolButton("YAKARI_LOGO", image=ICONS_PATH + "yakari_smallLogo.png")
    MC.symbolButton("PREPROD_SYMBOLBUTTON", image=ICONS_PATH + "preprodModeOff_icon.png", c=preProdModeClicked, h=20)
    MC.symbolButton("PROD_SYMBOLBUTTON", image=ICONS_PATH + "prodModeOn_icon.png", c=prodModeClicked, h=20)
    MC.symbolButton("EXTRA_SYMBOLBUTTON", image=ICONS_PATH + "extraModeOff_icon.png", c=extraModeClicked, h=20)

    QtText(handle="SEASON_TEXT_BLACK", label="season 4", color=(0, 0, 0), paddingTBLR=(0, 0, 0, 0), 
           margin=0, fontFamily="Arial", fontSize=15, fontWeight="bold", align="left")
    QtText(handle="SEASON_TEXT", label="season 4", color=(255, 173, 49), paddingTBLR=(0, 0, 0, 0), 
           margin=0, fontFamily="Arial", fontSize=14, fontWeight="bold", align="left")




    PREPROD_PLACEHOLDER = MC.columnLayout("PREPROD_PLACEHOLDER", manage=0)
    MC.setParent("..") 

    PROD_PLACEHOLDER = MC.columnLayout("PROD_PLACEHOLDER")
    MC.setParent("..")
    
    EXTRA_PLACEHOLDER = MC.columnLayout("EXTRA_PLACEHOLDER", manage=0)
    MC.setParent("..")

    


    MC.scrollField("UNIVERSAL_LOG", h=160, font="plainLabelFont", editable=False, wordWrap=True, text="Ready...\n", bgc=(.2,.2,.2))
    PROGRESS_BAR = MC.progressBar("PROGRESS_BAR", minValue=0, maxValue=100, progress=0, h=16, w=324, manage=0)

    MC.symbolButton("GRANULARITY_SYMBOLBUTTON", image=ICONS_PATH + "granularOptions_icon", w=20, h=20, 
                    command=granularOptions, ann="Shows a list of operations performed\nafter the '_REN' application")
    MC.symbolCheckBox("DETAILEDREPORT_SYMBOLCHECKBOX", image=ICONS_PATH + "detailedReport_icon", w=20, h=20, value=False, cc="FINAL__YAKARI_renderLibrary.printLog('SHOW DETAILED REPORT')", manage=0)
    MC.symbolCheckBox("HARDDEBUG_SYMBOLCHECKBOX", image=ICONS_PATH + "hardDebug_icon", w=20, h=20, value=False, cc="LOCALVERSION__YAKARI_renderLibrary.printLog('HARD DEBUG MODE')", manage=0)


    MC.formLayout(GLOBAL_FORM, edit=True, attachForm=[(YAKARI_LOGO, "top", 0),
                                                      ("SEASON_TEXT_BLACK", "top", 52), 
                                                      ("SEASON_TEXT_BLACK", "left", 13), 
                                                      ("SEASON_TEXT", "top", 51), 
                                                      ("SEASON_TEXT", "left", 12), 

                                                      ("PREPROD_SYMBOLBUTTON", "right", 0), 
                                                      ("PROD_SYMBOLBUTTON", "right", 0),
                                                      ("EXTRA_SYMBOLBUTTON", "right", 0),
                                                      ("GRANULARITY_SYMBOLBUTTON", "left", 0),
                                                      ("GRANULARITY_SYMBOLBUTTON", "bottom", 0), 
                                                      ("DETAILEDREPORT_SYMBOLCHECKBOX", "bottom", 0),
                                                      ("HARDDEBUG_SYMBOLCHECKBOX", "bottom", 0),

                                                      ("UNIVERSAL_LOG", 'left', 0), 
                                                      ("UNIVERSAL_LOG", 'right', 0),  
                                                      ("UNIVERSAL_LOG", 'bottom', 0),
                                                      (PROGRESS_BAR, 'bottom', 1) 
                                                      ], 
                                          attachNone=[(PROGRESS_BAR, 'top')],           
                                       attachControl=[(PREPROD_PLACEHOLDER, "top", 0, YAKARI_LOGO),
                                                      (PROD_PLACEHOLDER, "top", 0, YAKARI_LOGO),
                                                      (EXTRA_PLACEHOLDER, "top", 0, YAKARI_LOGO),
                                                      (PROGRESS_BAR, "left", 0, "HARDDEBUG_SYMBOLCHECKBOX"),

                                                      ("PROD_SYMBOLBUTTON", "top", 0, "PREPROD_SYMBOLBUTTON"),
                                                      ("EXTRA_SYMBOLBUTTON", "top", 0, "PROD_SYMBOLBUTTON"),
                                                      ("DETAILEDREPORT_SYMBOLCHECKBOX", "left", 0, "GRANULARITY_SYMBOLBUTTON"), 
                                                      ("HARDDEBUG_SYMBOLCHECKBOX", "left", 0, "DETAILEDREPORT_SYMBOLCHECKBOX")])

 



    #=================================================================================================================================
    #---------------------------------------------------------------------------------------------------------------------------------
    # PREPROD TAB
    #---------------------------------------------------------------------------------------------------------------------------------
    #=================================================================================================================================
    PREPROD_TAB_LAYOUT = MC.formLayout("PREPROD_LAYOUT", nd=100, p=PREPROD_PLACEHOLDER)

    #---------------------------------------------
    # SAVER
    SAVER_FRAME = MC.frameLayout(l="SAVER", bs="etchedIn", bv=True, mw=4, mh=4, bgc=(.4,.4,.4), w=width-6)

    SAVER_BUTTONS = MC.rowLayout(nc=2)
    0;  MC.columnLayout()
    0;    MC.button("saveDump_button", l="SAVE\n( pipeline )", w=80, h=46, bgc=(.35,.35,.35), c=pipelineSaveDump, enable=0)
    0;    MC.button("manualSaveDump_button", l="manual SAVE", w=80, h=26, bgc=(.35,.35,.35), c=manualSaveDump, enable=0)
    0;    MC.setParent("..")
    0;  MC.button("detectAnomalies_button", l="DETECT\nPRIMARY\nANOMALIES", w=80, h=60, bgc=(.50,.35,.35), c=detectSceneAnomalies, enable=True)
    0;  MC.setParent("..")
    
    SCENEID_LINE = MC.columnLayout() 
    0;  MC.rowLayout(nc=3) 
    0;    MC.text(l="  YAKARI scene ID ")
    0;    MC.textField("saver_sceneIDLabel_textField", tx="", w=100, bgc=(.25,.25,.25), ed=0)
    0;    MC.setParent("..")
    #0;  MC.rowLayout(nc=2)
    #0;    MC.image(image=ICONS_PATH + "warning_icon.png")
    #0;    MC.text(l="DON'T forget to save and load \n            (PREPROD)the 'lighLinker1' node dump!")
    #0;    MC.setParent("..")
    0;  MC.setParent("..") 

    MC.setParent("..")


    #----------------------------------------------
    # LOADER
    LOADER_FRAME = MC.frameLayout(l="LOADER", bs="etchedIn", bv=True, mw=4, mh=4, bgc=(.4,.4,.4), w=width-6)

    LOADER_BUTTONS = MC.rowLayout(nc=3)
    0;  MC.columnLayout()
    0;    MC.button("loadDump_button", l="LOAD\n( pipeline )", w=80, h=46, bgc=(.35,.35,.35), c=pipelineLoadDump, enable=0)
    0;    MC.button("manualLoadDump_button", l="manual LOAD", w=80, h=26, bgc=(.35,.35,.35), c=manualLoadDump, enable=0)
    0;    MC.setParent("..")
    0;  MC.button(l="apply\nYAKARI\nPRESETS", w=70, h=50, bgc=(.4,.4,.3), c=doApplyRenderDefaults, enable=True)
    0;  QtButton(handle="aufbau", label="DELETE\nLAYERS", action=doDeleteExtraLayers,  
                 lineColor=(240,100,100), background=(120,60,60), 
                 borderRadius=38, paddingTBLR=(0,0,0,0), margin=0, w=76, h=76,
                 fontFamily="Arial", fontSize=14, fontWeight="bold") 
    #0;  MC.button(l="DELETE\nLAYERS", w=70, h=50, bgc=(.4,.3,.3), c=doDeleteExtraLayers, enable=True)
    0;  MC.setParent("..")

    MC.setParent("..")


    MC.formLayout(PREPROD_TAB_LAYOUT, edit=True, 
                  attachForm=   [(SAVER_FRAME, 'left', 0),
                                 (SAVER_FRAME, 'top', 0),
                                 (SAVER_FRAME, 'right', 0)],
                  attachControl=[(LOADER_FRAME, 'top', 0, SAVER_FRAME)])





    #=================================================================================================================================
    #---------------------------------------------------------------------------------------------------------------------------------
    # PROD 
    #---------------------------------------------------------------------------------------------------------------------------------
    #=================================================================================================================================
    PROD_FORMLAYOUT = MC.formLayout(p=PROD_PLACEHOLDER)
    



    PROD_GLOBAL_AMBIENTS = QtFrameLayout(label="COLORS", borderStyle="etchedIn", backgroundColor=(.35,.35,.35), borderVisible=True, mw=4, mh=4, w=width-6)
    0;MC.rowLayout(nc=4)
    0;  QtText(label='global presets ')
    0;  MC.optionMenu("chosenGlobalPreset_optionMenu", changeCommand="pass")
    0;  MC.menuItem(label='DAY')
    0;  MC.menuItem(label='TWILIGHT')
    0;  MC.menuItem(label='DAWN')
    0;  MC.menuItem(label='NIGHT')
    0;  MC.menuItem(label='FX')
    0;  MC.menuItem(label='FIRELIGHT')
    0;  MC.menuItem(label='UNDERWATER')
    0;  MC.text(l="", w=16)
    0;  QtButton(handle="applyPresetGlobally_QTBUTTON", label="APPLY COLORS", action=applyGlobalPreset,  
                 lineColor=CYAN_L, background=CYAN_B, 
                 borderRadius=13, paddingTBLR=(0,0,0,0), margin=1, w=130, h=28,
                 fontFamily="Arial", fontSize=14, fontWeight="bold")
    0;  MC.setParent("..")
    0;MC.setParent("..")
    
    PROD_SELECTION_AMBIENTS = MC.rowLayout("selectionPresets_rowLayout", nc=4, enable=1)
    0;QtText(label="  selection Presets ")
    0;MC.optionMenu("selectionPresets_optionMenu", label="", changeCommand="pass")
    0;MC.menuItem(label='...')
    0;MC.text(l="", w=18)
    0;QtButton(handle="applyToSelection_QTBUTTON", label="APPLY COLORS (sel)", action=applyPresetToSelection,  
               lineColor=CYAN_L, background=CYAN_B, 
               borderRadius=13, paddingTBLR=(0,0,0,0), margin=1, w=150, h=28,
               fontFamily="Arial", fontSize=13, fontWeight="bold")
    0;MC.setParent("..")
    
    PROD_NAMESPACE_LINE = MC.rowLayout(nc=2, enable=1) 
    0;QtText(handle="selectionID_QTTEXT", label="  selection ID ")
    0;MC.textField("loader_namespace_textField", tx="...", w=90,  bgc=(.25,.25,.25), ed=0)
    0;MC.setParent("..")








    CUSTOM_RENDER_LAYERS = QtFrameLayout(label="CUSTOM RENDER LAYERS", borderStyle="etchedIn", backgroundColor=(.35,.35,.35), borderVisible=True, mw=4, mh=4, w=width-6, enable=1)
    0;MC.rowColumnLayout(nc=3)
    0;  QtText(handle="castShdwsGround_QTTEXT", label=" CAST_SHDWS_GROUND")
    0;  MC.text(l="", w=64)
    0;  QtButton(handle="createLayer_QTBUTTON", label="CREATE", action=createCastShadowsGroundLayer,  
                 lineColor=BLUE_L, background=BLUE_B, 
                 borderRadius=12, paddingTBLR=(0,0,0,0), margin=1, w=110, h=26,
                 fontFamily="Arial", fontSize=14, fontWeight="bold")
    0;  MC.setParent("..")





    0;MC.formLayout("CUSTOM_LAYERS_FORM", nd=100)

    0;  QtText("CUSTOM_LAYERS_LABEL", label=" CUSTOM LAYERS", fontSize=13)
    0;  MC.treeView("CUSTOM_LAYERS_TREE", numberOfButtons=0, w=360, h=120,  abr=True, sc=treeViewDoNothing, scc=treeViewDoNothing)
    0;  MC.treeView("CUSTOM_LAYERS_TREE", e=True, addItem=("None...", ""))

    0;  QtButton(handle="CREATE_CUSTOM_LAYERS_QTBUTTON", label="CREATE ALL", action=createCustomLayers,  
                 lineColor=BLUE_L, background=BLUE_B, 
                 borderRadius=12, paddingTBLR=(0,0,0,0), margin=1, w=110, h=26,
                 fontFamily="Arial", fontSize=14, fontWeight="bold")
    0;  QtButtonEnable(handle="CREATE_CUSTOM_LAYERS_QTBUTTON", enable=False)
     
    0;  MC.symbolButton("ADD_SYMBOLBUTTON"   , image=ICONS_PATH + "add_icon.png", c=createCustomLayersUI, ann=HTMLFormatter("NEW RENDER LAYER TEMPLATE", ["Create a new render layer template"]))
    0;  MC.symbolButton("DELETE_SYMBOLBUTTON", image=ICONS_PATH + "delete_icon.png", c=deleteCustomLayer, ann="Delete the selected custom layers", manage=0)
    0;  MC.symbolButton("EDIT_SYMBOLBUTTON"  , image=ICONS_PATH + "edit_icon.png", c=editCustomLayer, ann="Edit the selected custom layer", manage=0)
    0;  MC.symbolButton("DELETEALL_SYMBOLBUTTON", image=ICONS_PATH + "deleteAll_icon.png", c=deleteAllCustomLayers, ann=HTMLFormatter("DELETE ALL LAYER TEMPLATES", ["Clear the custom layer list"]), enable=0)
 
    0;  MC.button("LIST_LAYERS", l="COMBINE\nLAYER", c=listLayers_DEBUG, manage=0, bgc=(1,0,0))

    0;  MC.setParent("..")

    MC.formLayout("CUSTOM_LAYERS_FORM", edit=True, 
                  attachForm=   [("CUSTOM_LAYERS_LABEL", 'top', 0),
                                 ("ADD_SYMBOLBUTTON", 'left', 0),
                                 ("CREATE_CUSTOM_LAYERS_QTBUTTON", 'right', 0)
                                 ],

                  attachControl=[("CUSTOM_LAYERS_TREE", 'top', 0, "CUSTOM_LAYERS_LABEL"),

                                 ("ADD_SYMBOLBUTTON", 'top', 0, "CUSTOM_LAYERS_TREE"),

                                 ("EDIT_SYMBOLBUTTON", 'top', 0, "CUSTOM_LAYERS_TREE"),
                                 ("EDIT_SYMBOLBUTTON", 'left', 0, "ADD_SYMBOLBUTTON"),

                                 ("DELETE_SYMBOLBUTTON", 'top', 0, "CUSTOM_LAYERS_TREE"),
                                 ("DELETE_SYMBOLBUTTON", 'left', 0, "EDIT_SYMBOLBUTTON"),

                                 ("DELETEALL_SYMBOLBUTTON", 'top', 0, "CUSTOM_LAYERS_TREE"),
                                 ("DELETEALL_SYMBOLBUTTON", 'left', 0, "DELETE_SYMBOLBUTTON"),
                                
                                 ("CREATE_CUSTOM_LAYERS_QTBUTTON", 'top', 0, "CUSTOM_LAYERS_TREE"),
                                 ("LIST_LAYERS", 'right', 0, "CREATE_CUSTOM_LAYERS_QTBUTTON")
                                  ])



    0;MC.setParent("..")








    PROD_MANAGE_SMOOTH = MC.frameLayout(l="MANAGE RENDERING SMOOTHING", bs="etchedIn", bgc=(.35,.35,.35), bv=True, mw=4, mh=4, w=width-6, enable=1)
    0;MC.rowLayout(nc=5, enable=1)
    0;  MC.columnLayout()
    0;    QtText(handle="level_QTTEXT", label=" level")
    0;    MC.optionMenu("smoothLevel_optionMenu", label="")
    0;      MC.menuItem(label=' 0 ')
    0;      MC.menuItem(label=' 1 ')
    0;      MC.menuItem(label=' 2 ')
    0;      MC.menuItem(label=' 3 ')
    0;      MC.menuItem(label=' 4 ')
    0;    MC.optionMenu("smoothLevel_optionMenu", edit=True, value=" 2 ")
    0;    MC.setParent("..")
    0;  QtButton(handle="applySmoothGlobally_QTBUTTON", label="APPLY\n(globally)", action=applyRenderingSmoothGlobally,  
                 lineColor=CYAN_L, background=CYAN_B, 
                 borderRadius=14, paddingTBLR=(0,0,0,0), margin=2, w=85, h=44,
                 fontFamily="Arial", fontSize=12, fontWeight="bold") 
    0;  QtButton(handle="applySmoothSelection_QTBUTTON", label="APPLY\n(selection)", action=applyRenderingSmoothToSelection,  
                 lineColor=CYAN_L, background=CYAN_B, 
                 borderRadius=14, paddingTBLR=(0,0,0,0), margin=2, w=85, h=44,
                 fontFamily="Arial", fontSize=12, fontWeight="bold")      
    0;  MC.text(l="", w=5)                
    0;  QtButton(handle="saveSmoothInfo_QTBUTTON", label="SAVE\n3dsMax Data", action=save3DsMaxData,  
                 lineColor=BLUE_L, background=BLUE_B, 
                 borderRadius=20, paddingTBLR=(0,0,0,0), margin=0, w=118, h=44,
                 fontFamily="Arial", fontSize=14, fontWeight="bold", 
                 annotation="<font size=\"5\">  SAVE DATA FOR 3DSMAX  </font><font size=\"4\"><br> - list what's gonna happen...<br> - NO MYSTERIOUS BUTTONS</font>")   
    0;  MC.button("saveSmoothInfo_QTBUTTON", edit=True, enable=1)                  
    0;  MC.setParent("..")   
    0;MC.setParent("..")






    PROD_DUMP_MODE = MC.columnLayout()
    0;MC.rowLayout(nc=4)
    0;  MC.text(l="", w=2)
    0;  QtButton(handle="editAssetPartition_QTBUTTON", label="EDIT GROUPS", action=assetPartitionUI,  
                 lineColor=CYAN_L, background=CYAN_B, 
                 borderRadius=12, paddingTBLR=(0,0,0,0), margin=1, w=114, h=26,
                 fontFamily="Arial", fontSize=13, fontWeight="bold",
                 annotation=HTMLFormatter("GLOBAL \"APPLY DUMP\"", ["In the follwing order:", " - apply dump info", " - postDump", " - apply dayPreset"], 80))

    0;  MC.text(l="", w=28)
    0;  QtButton(handle="globalLoadDumps_QTBUTTON", label="GLOBAL APPLY", action=pipelineGlobalLoadDumps,  
                 lineColor=BLUE_L, background=BLUE_B, 
                 borderRadius=12, paddingTBLR=(0,0,0,0), margin=1, w=196, h=26,
                 fontFamily="Arial", fontSize=14, fontWeight="bold", 
                 annotation=HTMLFormatter("GLOBAL \"APPLY DUMP\"", ["In the follwing order:", " - apply dump info", " - postDump", " - apply dayPreset"], 80))
    0;  MC.setParent("..")
    0;MC.setParent("..")



    SHITTY_LINE = MC.columnLayout()
    0;QtText(handle="treeViewtext_QTTEXT", label="  SCENE ASSET                               known     ren amb grp", fontSize=13)
    0;MC.setParent("..")
    
    # SCENE_ASSET_TREELIST_HEIGHT is a bad way to share height: ppppplease, go for OOP/Qt, all this stuff is utterly obsolete!
    PROD_ASSETS_LIST = MC.formLayout(w=360, h=SCENE_ASSET_TREELIST_HEIGHT, enable=1)

    # Disable selection and renaming by overriding with a null function
    0;MC.treeView("TREEVIEW", parent=PROD_ASSETS_LIST, numberOfButtons=0, abr=False, sc=treeViewDoNothing, scc=treeViewDoNothing)
    MC.formLayout(PROD_ASSETS_LIST, e=True, attachForm=[("TREEVIEW",'top', 0),
                                                        ("TREEVIEW",'left', 4),
                                                        ("TREEVIEW",'bottom', 0),
                                                        ("TREEVIEW",'right', 4)])
    0;  MC.setParent("..")
 
   

    MC.setParent("..") # FORMLAYOUT


    MC.formLayout(PROD_FORMLAYOUT, edit=True, 
                  attachForm=   [(SHITTY_LINE, 'left', 0),
                                 (SHITTY_LINE, 'top', 0),
                                 (SHITTY_LINE, 'right', 0)],
                  attachControl=[(PROD_ASSETS_LIST, 'top', 0, SHITTY_LINE), 
                                 (PROD_DUMP_MODE, 'top', 0, PROD_ASSETS_LIST),
                                 (PROD_GLOBAL_AMBIENTS, 'top', 0, PROD_DUMP_MODE), 
                                 (PROD_NAMESPACE_LINE, 'top', 0, PROD_GLOBAL_AMBIENTS),
                                 (PROD_SELECTION_AMBIENTS, 'top', 0, PROD_NAMESPACE_LINE), 
                                 (CUSTOM_RENDER_LAYERS, 'top', 0, PROD_SELECTION_AMBIENTS),
                                 (PROD_MANAGE_SMOOTH, 'top', 0, CUSTOM_RENDER_LAYERS)])
    


    
    #=================================================================================================================================
    #---------------------------------------------------------------------------------------------------------------------------------
    # NODE DUMPER TAB
    #---------------------------------------------------------------------------------------------------------------------------------
    #=================================================================================================================================
    NODEDUMPER_TAB = MC.columnLayout("NODEDUMPER_LAYOUT", p=EXTRA_PLACEHOLDER)
    larghezza = width/4 - 4
    altezza   = 44
    0;MC.rowLayout(nc=4)
    0;  QtButton(handle="shit1", label="STORE\nNODES", action=storeNodes,  
                 lineColor=(220,220,100), background=(100,100,60), 
                 borderRadius=14, paddingTBLR=(0,0,0,0), margin=0, w=larghezza, h=altezza,
                 fontFamily="Arial", fontSize=14, fontWeight="bold", 
                 annotation="")
    0;  QtButton(handle="shit2", label="DETECT\nCHANGES", action=detectChanges,  
                 lineColor=(180,250,100), background=(80,130,60), 
                 borderRadius=14, paddingTBLR=(0,0,0,0), margin=0, w=larghezza, h=altezza,
                 fontFamily="Arial", fontSize=14, fontWeight="bold", 
                 annotation="")
    0;  QtButton(handle="shit3", label="SAVE\nDUMP", action=saveNodesDump,  
                 lineColor=(100,220,220), background=(60,110,100), 
                 borderRadius=14, paddingTBLR=(0,0,0,0), margin=0, w=larghezza, h=altezza,
                 fontFamily="Arial", fontSize=14, fontWeight="bold", 
                 annotation="")    
    0;  QtButton(handle="shit4", label="LOAD\nDUMP", action=doLoadNodesDump,  
                 lineColor=(100,220,220), background=(60,110,100), 
                 borderRadius=14, paddingTBLR=(0,0,0,0), margin=0, w=larghezza, h=altezza,
                 fontFamily="Arial", fontSize=14, fontWeight="bold", 
                 annotation="")    
    #0;  MC.button(l="STORE\nNODES", w=larghezza, h=altezza, c=storeNodes)
    #0;  MC.button(l="DETECT\nCHANGES", w=larghezza, h=altezza, c=detectChanges)
    #0;  MC.button(l="SAVE\nNODES DUMP", w=larghezza, h=altezza, c=saveNodesDump)
    #0;  MC.button(l="LOAD\nNODES DUMP", w=larghezza, h=altezza, c=doLoadNodesDump)    
    0;  MC.setParent("..") 
    0;MC.frameLayout(l="STORED NODES", li=0, bv=0, fn="boldLabelFont", w=width-5)
    0;  MC.scrollField("storedNodes_scrollField", editable=False, wordWrap=True, text="...", w=width, h=144)
    0;  MC.setParent("..") 
    0;MC.setParent( '..' )
    




    #---------------------------------------------------------------------------------------------------------------------------------
    # SHOW WINDOW
    #---------------------------------------------------------------------------------------------------------------------------------

    MC.showWindow("YAKARI_renderLibraryUI_WIN")
    MC.window("YAKARI_renderLibraryUI_WIN", edit=True, w=width, h=height)

   


    #=================================================================================================================================
    #---------------------------------------------------------------------------------------------------------------------------------
    # SCRIPT JOBS
    #---------------------------------------------------------------------------------------------------------------------------------
    #=================================================================================================================================
    MC.scriptJob(event=["SelectionChanged", selectionListener], parent="YAKARI_renderLibraryUI_WIN") 
    MC.scriptJob(event=["NewSceneOpened"  , sceneListener]    , parent="YAKARI_renderLibraryUI_WIN") 
    MC.scriptJob(event=["SceneOpened"     , sceneListener]    , parent="YAKARI_renderLibraryUI_WIN") 
    
    # Closes all secondary windows when mainUI is closed
    MC.scriptJob(uiDeleted=["YAKARI_renderLibraryUI_WIN", closeSecondaryWindows])

    inViewMessage(message="EVENT LISTENER\nscriptJobs activated!!!", position="midCenter", time=800, status="SUCCESS")



def treeViewDoNothing(*args):
    # To disable sele ction and renaming in asset list, override with "empty" functions
    return False

def build_ASSETS_DATA(*args):

    """ BE HYPERSTRICT HERE!!! """
    # Detect:
    # - YAKARI tag (if multiple references)
    # - the path to _REN
    # - the path to _AMB
    # - the list of AMBs available
    # SET TO NONE IF SOMETHING WENT WRONG

    global ASSETS_DATA
    ASSETS_DATA.clear() # A brand new start
    MC.namespace(set=":") # Move to root namespace ":"
    sceneNamespaces = [name for name in MC.namespaceInfo(lon=True, r=True) if name not in ["UI", "shared"]]
    for namespace in sceneNamespaces:
        # ASSETS_DATA = {assetNamespace: [assetID, RENPath, AMBPath, [amb1, amb2, ..., ambk]]}
        ASSETS_DATA[namespace] = [None, None, None, None]
        # Check if it's a valid YAKARI namespace
        tokens = namespace.split("_")
        category = tokens[0]
        if category in ["ch", "pr"]:
            # CHARACTER/PROPS (multiple references, _REN, _AMB)
            VALID_TAGS = CHARACTER_TAGS if category == "ch" else PROP_TAGS
            trueNamespace = tokens[0] + "_" + tokens[1]
            if trueNamespace in VALID_TAGS:
                ASSETS_DATA[namespace][0] = trueNamespace
                # check for _REN
                RENPath = PROJECT_ROOT + category + "/" + trueNamespace + "/tex/maya/" + trueNamespace + "_REN.txt"
                if OS.path.isfile(RENPath):
                    ASSETS_DATA[namespace][1] = RENPath
                else:     
                    # missing _REN
                    ASSETS_DATA[namespace][1] = None
                #-------------------------------------------------
                # check for _AMB
                AMBPath = PROJECT_ROOT + category + "/" + trueNamespace + "/tex/maya/" + trueNamespace + "_AMB.txt"
                if OS.path.isfile(AMBPath):
                    ASSETS_DATA[namespace][2] = AMBPath
                    # open the _AMB and list the possible ambients
                    f = None
                    ambientsPreset = None
                    try:
                        f = open(AMBPath, "r")
                        ambientsPreset = JSON.loads(f.read())
                    except Exception as e:
                        fatality("Unable to load:\n" + AMBPath + "\n\nReason:\n" + str(e))
                    finally:
                        if f != None:
                            f.close()
                    ASSETS_DATA[namespace][3] = []        
                    for preset in ambientsPreset.keys():
                        ASSETS_DATA[namespace][3].append(preset)

                else:
                    # missing _AMB
                    ASSETS_DATA[namespace][2] = None

            else:
                # UNKNOWN: ABORT
                ASSETS_DATA[namespace][0] = None

        elif category == "ss":
            # SUBSET (no multiple references, no _REN, no _AMB)
            if True: #namespace in SUBSET_TAGS:
                ASSETS_DATA[namespace][0] = namespace
            else:
                # UNKNOWN: ABORT
                ASSETS_DATA[namespace][0] = None
        else:
            # UNKNOWN
            ASSETS_DATA[namespace][0] = None       

def print_ASSETS_DATA(*args):
    print "\n\n\n------------------------------------------------------------------------------------------------"
    print "RAW ASSET_DATA"
    print "format: {assetNamespace: [assetID, RENPath, AMBPath, [amb1, amb2, ..., ambk]]}\n"
    pprint(ASSETS_DATA)
    print "------------------------------------------------------------------------------------------------"
    print "\n\n"

def refreshAssetsList(*args):
    0000;finalFuncDebug()

    # Update ASSETS_DATA
    build_ASSETS_DATA()    

    # A T R O C I O U S 
    global INITIALIZE_COMBINED_DATA_ON_REFRESH
    0000;finalPrintDebug("INITIALIZE COMBINED_DATA: ", INITIALIZE_COMBINED_DATA_ON_REFRESH)
    if INITIALIZE_COMBINED_DATA_ON_REFRESH:
        # if True, reset the "COMBINED_DATA"
        # if False, just use the existing stuff
        0000;finalPrintDebug("INITIALIZE COMBINED_DATA")
        initializeCOMBINED_DATA()
        INITIALIZE_COMBINED_DATA_ON_REFRESH = False

    numOfAssets = 0 # to write a NONE
    numOfSS     = 0 # to activate or not the creation button for SHDWQS_GROUND (which needs at least one SS)

    MC.treeView("TREEVIEW", edit=True, removeAll=True, nb=5, abr=True)

    #  order items in ASSETS_DATA:
    # - first the ordered "grouped  assets"
    # - then the ungrouped stuff
    orderedAssets = []
    for groupId in COMBINED_ASSETS:
        orderedAssets.extend(COMBINED_ASSETS[groupId])
    for asset in ASSETS_DATA:
        if not asset in orderedAssets:
            orderedAssets.append(asset)    

    0000;finalPrintDebug("ASSETS_DATA: ", ASSETS_DATA)
    0000;finalPrintDebug("ORDERED ASSETS: ", orderedAssets)
    0000;finalPrintDebug("COMBINED_ASSETS: ", COMBINED_ASSETS)

    for asset in orderedAssets:

        if "pr_" not in asset and "ch_" not in asset and "ss_" not in asset:
            # we work only with PR, CH and SS; camera, st etc are not needed here!
            continue

        MC.treeView("TREEVIEW", e=True, addItem=(asset, ""))     
        MC.treeView("TREEVIEW", e=True, fn=(asset, "fixedWidthFont"))
        # hide the fakeButtons, needed to create a space between buttons
        MC.treeView("TREEVIEW", e=True, buttonVisible=(asset, 2, False))
        
        # a priori no need for gtoup id... show it only if everything is perfect or relevant
        MC.treeView("TREEVIEW", e=True, buttonVisible=(asset, 5, False))

        if ASSETS_DATA[asset][0] != None:
            numOfAssets += 1
            # IT'S KNOWN
            MC.treeView("TREEVIEW", e=True, tc=(asset, .5,1,.5))
            MC.treeView("TREEVIEW", e=True, lbc=(asset, .165,.165,.165))
            # green light on
            MC.treeView("TREEVIEW", e=True, image=                     (asset, 1, ICONS_PATH + "greenCheck_icon.png"))  
            MC.treeView("TREEVIEW", e=True, buttonTransparencyOverride=(asset, 1, True)) 
            MC.treeView("TREEVIEW", e=True, buttonTransparencyColor=   (asset, 1, 0.165,0.165,0.165)) 
            

            # If CH/PR look for _REN and _AMB
            if asset[0:2] in ["ch", "pr"]:  
                if ASSETS_DATA[asset][1] == None:
                    # REN MISSING
                    # let's go orange
                    MC.treeView("TREEVIEW", e=True, lbc=(asset, .165,.165,.165))
                    MC.treeView("TREEVIEW", e=True, tc=(asset, 1,.5,.2))

                    MC.treeView("TREEVIEW", e=True, image=                     (asset, 3, ICONS_PATH + "redCross_icon.png"))  
                    MC.treeView("TREEVIEW", e=True, buttonTransparencyOverride=(asset, 3, True)) 
                    MC.treeView("TREEVIEW", e=True, buttonTransparencyColor=   (asset, 3, 0.165,0.165,0.165)) 
                else:      
                    MC.treeView("TREEVIEW", e=True, image=                     (asset, 3, ICONS_PATH + "greenCheck_icon.png"))  
                    MC.treeView("TREEVIEW", e=True, buttonTransparencyOverride=(asset, 3, True)) 
                    MC.treeView("TREEVIEW", e=True, buttonTransparencyColor=   (asset, 3, 0.165,0.165,0.165)) 

                if ASSETS_DATA[asset][2] == None:
                    # AMB MISSING
                    # let's go orange
                    MC.treeView("TREEVIEW", e=True, lbc=(asset, .165,.165,.165))
                    MC.treeView("TREEVIEW", e=True, tc=(asset, 1,.5,.2))    

                    MC.treeView("TREEVIEW", e=True, image=                     (asset, 4, ICONS_PATH + "redCross_icon.png"))  
                    MC.treeView("TREEVIEW", e=True, buttonTransparencyOverride=(asset, 4, True)) 
                    MC.treeView("TREEVIEW", e=True, buttonTransparencyColor=   (asset, 4, 0.165,0.165,0.165))                 
                else: 
                    MC.treeView("TREEVIEW", e=True, image=                     (asset, 4, ICONS_PATH + "greenCheck_icon.png"))  
                    MC.treeView("TREEVIEW", e=True, buttonTransparencyOverride=(asset, 4, True)) 
                    MC.treeView("TREEVIEW", e=True, buttonTransparencyColor=   (asset, 4, 0.165,0.165,0.165)) 

                if ASSETS_DATA[asset][1] != None and ASSETS_DATA[asset][2] != None:
                    # KNOWN, REN, AMB ok... show GROUP ID
                    MC.treeView("TREEVIEW", e=True, buttonVisible=(asset, 5, True))
                    MC.treeView("TREEVIEW", e=True, buttonTransparencyOverride=(asset, 5, True)) 

                    # Identify the group of the asset... another bad decision of used structure that propagates here... so soooorry!!!
                    """
                    COMBINED_ASSETS = {0: ["fava", "minchia", "sborra1"], 
                                       1: ["cazzo", "sborra", "cazzo1"], 
                                       2: ["troia", "wow", "troia1"], 
                                       7: ["minchia1", "wow1"], 
                                       11:["aaa", "bbb", "ccc", "ddd"]
                                      }
                    """
                    groupMembership = getGroupFromAsset(asset)

                    MC.treeView("TREEVIEW", e=True, bti=(asset, 5, str(groupMembership)))   
                    MC.treeView("TREEVIEW", e=True, buttonTransparencyColor=   (asset, 5, getGroupIdColor(groupMembership)[0], getGroupIdColor(groupMembership)[1], getGroupIdColor(groupMembership)[2]))

                    #MC.treeView("TREEVIEW", e=True, buttonTransparencyColor=   (asset, 5, 1, 0.5, 1))   
            else: 
                # it's a KNOWN SS, no need for other shit
                numOfSS += 1
                MC.treeView("TREEVIEW", e=True, buttonVisible=             (asset, 3, False))
                MC.treeView("TREEVIEW", e=True, buttonVisible=             (asset, 4, False))  

        else:
            numOfAssets += 1
            # UNKNOWN
            MC.treeView("TREEVIEW", e=True, tc=(asset, 1,.1,.1))
            MC.treeView("TREEVIEW", e=True, lbc=(asset, .165,.165,.165))

            # red cross for KNOWN
            MC.treeView("TREEVIEW", e=True, image=                     (asset, 1, ICONS_PATH + "redCross_icon.png"))  
            MC.treeView("TREEVIEW", e=True, buttonTransparencyOverride=(asset, 1, True)) 
            MC.treeView("TREEVIEW", e=True, buttonTransparencyColor=   (asset, 1, 0.165,0.165,0.165)) 
            # don't bother with REN and AMB
            MC.treeView("TREEVIEW", e=True, buttonVisible=             (asset, 3, False))
            MC.treeView("TREEVIEW", e=True, buttonVisible=             (asset, 4, False))            
            continue
    
    if numOfAssets == 0:
        MC.treeView("TREEVIEW", e=True, addItem=("None...", ""))     
        MC.treeView("TREEVIEW", e=True, fn=("None...", "fixedWidthFont"))
        MC.treeView("TREEVIEW", e=True, tc=("None...", .8,.8,.8))
        MC.treeView("TREEVIEW", e=True, lbc=("None...", .165,.165,.165))

        MC.treeView("TREEVIEW", e=True, buttonVisible=("None...", 1, False))
        MC.treeView("TREEVIEW", e=True, buttonVisible=("None...", 2, False))
        MC.treeView("TREEVIEW", e=True, buttonVisible=("None...", 3, False))
        MC.treeView("TREEVIEW", e=True, buttonVisible=("None...", 4, False))
        MC.treeView("TREEVIEW", e=True, buttonVisible=("None...", 5, False))
    
    MC.button("createLayer_QTBUTTON", edit=True, label="CREATE", enable=1)        
    

    # if the vertical scrollBar is active, shrink slightly the text "SCENE ASSETS..."
    if numOfAssets > TREELIST_SIZE:
        # scrollBar active: shrink it
        MC.text("treeViewtext_QTTEXT", edit=True, label="  SCENE ASSET                           known     ren amb grp")
    else:
        MC.text("treeViewtext_QTTEXT", edit=True, label="  SCENE ASSET                               known     ren amb grp")

def sceneListener(*args):
    0000;finalFuncDebug()

    # LOCK THE SCENE IF NOT A VALID SCENE NAME
    lockUnlockUI()

    # refresh always the assetsList

    # It's a new scene. Force the initializaton of the COMBINE_GROUPS
    global INITIALIZE_COMBINED_DATA_ON_REFRESH
    INITIALIZE_COMBINED_DATA_ON_REFRESH = True

    build_ASSETS_DATA()
    refreshAssetsList()
    if CURRENT_UIMODE == "PROD":
        clearLog()
        printLog("[PROD MODE]")
        printLog("Ready...")
        return

    if CURRENT_UIMODE != "PREPROD":
        return

    shortSceneName = MC.file(query=True, sn=True, shn=True)

    isTagKnown = False
    if shortSceneName != "":  
        tokens = shortSceneName.split("_")
        if len(tokens) >= 2:
            if tokens[0] == "ch":
                assetID = tokens[0] + "_" + tokens[1]
                if assetID in CHARACTER_TAGS:
                    isTagKnown = True
            elif tokens[0] == "pr":
                assetID = tokens[0] + "_" + tokens[1]
                print assetID
                if assetID in PROP_TAGS:
                    isTagKnown = True
            elif tokens[0] == "ss":
                # SUBSETS ain't supposed to have a _REN!!!
                MC.textField("saver_sceneIDLabel_textField", e=1, tx="UNDUMPABLE", bgc=(1,0,0))    
                MC.button("saveDump_button", edit=True, l="SAVE\nDUMP", bgc=(.35,.35,.35))
                printLog("The current file:\n                 '" + shortSceneName + "'\n                 is of type SUBSET. Dump is not supported!", "ERROR")
                return
        if isTagKnown:
            printLog("The current file:\n          '" + shortSceneName + "'\n          has a valid YAKARI tag.", "OK")
            MC.textField("saver_sceneIDLabel_textField", e=1, tx=assetID, bgc=(0,1,0))
            # STOP SAVING INTO THE OFFICIAL _REN
            MC.button("saveDump_button", edit=True, bgc=(.3,.5,.3), enable=True)
            MC.button("manualSaveDump_button", edit=True, bgc=(.2,.35,.2), enable=True)
            """ To manage the LOAD_PIPELINE, check if _REN already exists """
            sceneTag = MC.textField("saver_sceneIDLabel_textField", query=True, tx=True)
            category = sceneTag[0:2]
            path = PROJECT_ROOT + category + "/" + sceneTag + "/tex/maya/" + sceneTag + "_REN.txt"
            if OS.path.isfile(path):
                # OK, _REN exists
                # PREVENT AUTOLOAD
                MC.button("loadDump_button", edit=True, bgc=(.3,.5,.3), enable=True)
                MC.button("manualLoadDump_button", edit=True, bgc=(.2,.35,.2), enable=True)
                printLog("The current file:\n          '" + shortSceneName + "'\n          has a \"_REN\" in the pipeline.", "OK")

            else:
                # BAD: _REN missing, no autoLoad
                MC.button("loadDump_button", edit=True, bgc=(.35,.35,.35), enable=False)
                MC.button("manualLoadDump_button", edit=True, bgc=(.35,.50,.35), enable=1)
                printLog("The current file:\n          '" + shortSceneName + "'\n          has NO \"_REN\" in the pipeline.", "WARNING")

        else:
            MC.textField("saver_sceneIDLabel_textField", e=1, tx="UNKNOWN", bgc=(.45,.3,.3))    
            MC.button("saveDump_button", edit=True, bgc=(.35,.35,.35), enable=0)
            MC.button("loadDump_button", edit=True, bgc=(.35,.35,.35), enable=0)
            MC.button("manualSaveDump_button", edit=True, bgc=(.35,.50,.35), enable=1)
            MC.button("manualLoadDump_button", edit=True, bgc=(.35,.50,.35), enable=1)
            printLog("The current file:\n                 '" + shortSceneName + "'\n                 hasn't a valid YAKARI tag. You can still dump, \n                 but MANUALLY and OUTSIDE the pipeline.", "ERROR")

    else:
        # Empty scene
        MC.textField("saver_sceneIDLabel_textField", e=1, tx="", bgc=(.25,.25,.25))
        MC.button("saveDump_button", edit=True, bgc=(.35,.35,.35), enable=0)
        MC.button("loadDump_button", edit=True, bgc=(.35,.35,.35), enable=0)
        MC.button("manualSaveDump_button", edit=True, bgc=(.35,.35,.35), enable=0)
        MC.button("manualLoadDump_button", edit=True, bgc=(.35,.35,.35), enable=0)
        printLog("Please open a scene.", "NULL")



    # HERE active the AUTODUMP(pipeline) or a MANUALDUMP(outPipeline with file dialog)
    # MC.button("saveDump_button", l="SAVE\nDUMP\n(pipeline)", w=80, h=50, bgc=(.3,.4,.3), c=doDumpLayers, enable=True)

def selectionListener(*args):
    # ONLY FOR PROD MODE
    if CURRENT_UIMODE != "PROD":
        return

    # Activate the selection presets and selection apply only if it's a known tag
    sel = MC.ls(sl=True)
    text = "..."
    color = (.25,.25,.25)

    # make the SELECTION PRESETS and SELECTION APPLY unavailable
    MC.rowLayout("selectionPresets_rowLayout", edit=True, enable=0)
    menuItemsList = MC.optionMenu("selectionPresets_optionMenu", query=True, itemListLong=True)
    MC.deleteUI(menuItemsList, menuItem=True)
    MC.menuItem(label='  ...  ', parent="selectionPresets_optionMenu")

    if len(sel) == 1:
        assetName = getNamespace(sel[0])
        tokens = assetName.split("_")
        text = "   ...   "   
        color = (.25,.25,.25)
        if len(tokens) in [2,3]:
            tag = tokens[0] + "_" + tokens[1]
            if tag in CHARACTER_TAGS or tag in PROP_TAGS:
                # VALID
                text = tag   
                color = (.3,.6,.3)
                MC.rowLayout("selectionPresets_rowLayout", edit=True, enable=1)
                menuItemsList = MC.optionMenu("selectionPresets_optionMenu", query=True, itemListLong=True)
                MC.deleteUI(menuItemsList, menuItem=True)
                if ASSETS_DATA[assetName][3] != None  and len(ASSETS_DATA[assetName][3]) > 0: 
                    for preset in ASSETS_DATA[assetName][3]:
                        MC.menuItem(label=preset, parent="selectionPresets_optionMenu")
                else:
                    MC.menuItem(label=' NO _AMB ', parent="selectionPresets_optionMenu")
                    MC.rowLayout("selectionPresets_rowLayout", edit=True, enable=0)



    MC.textField("loader_namespace_textField", e=1, tx=text, bgc=color)
    
def preProdModeClicked(*args):
    global CURRENT_UIMODE
    if CURRENT_UIMODE != "PREPROD":
        MC.symbolButton("PREPROD_SYMBOLBUTTON", edit=True, image=ICONS_PATH + "preprodModeOn_icon.png")
        MC.symbolButton("PROD_SYMBOLBUTTON", edit=True, image=ICONS_PATH + "prodModeOff_icon.png")
        MC.symbolButton("EXTRA_SYMBOLBUTTON", edit=True, image=ICONS_PATH + "extraModeOff_icon.png")
        CURRENT_UIMODE = "PREPROD"
        
        MC.columnLayout("PREPROD_PLACEHOLDER", edit=True, manage=1)
        MC.columnLayout("PROD_PLACEHOLDER", edit=True, manage=0)
        MC.columnLayout("EXTRA_PLACEHOLDER", edit=True, manage=0)

        MC.window("YAKARI_renderLibraryUI_WIN", edit=True, w=PREPROD_WINDOW_SIZE[0], h=PREPROD_WINDOW_SIZE[1])

        sceneListener()
        
        clearLog()
        printLog("[PREPROD MODE]")
        printLog("Ready...")
        
def prodModeClicked(*args):
    global CURRENT_UIMODE
    if CURRENT_UIMODE != "PROD":
        MC.symbolButton("PREPROD_SYMBOLBUTTON", edit=True, image=ICONS_PATH + "preprodModeOff_icon.png")
        MC.symbolButton("PROD_SYMBOLBUTTON", edit=True, image=ICONS_PATH + "prodModeOn_icon.png")
        MC.symbolButton("EXTRA_SYMBOLBUTTON", edit=True, image=ICONS_PATH + "extraModeOff_icon.png")
        CURRENT_UIMODE = "PROD"

        MC.columnLayout("PREPROD_PLACEHOLDER", edit=True, manage=0)
        MC.columnLayout("PROD_PLACEHOLDER", edit=True, manage=1)
        MC.columnLayout("EXTRA_PLACEHOLDER", edit=True, manage=0)

        MC.window("YAKARI_renderLibraryUI_WIN", edit=True, w=PROD_WINDOW_SIZE[0], h=PROD_WINDOW_SIZE[1])
        refreshAssetsList()

        clearLog()
        printLog("[PROD MODE]")
        printLog("Ready...")
        
def extraModeClicked(*args):
    global CURRENT_UIMODE
    if CURRENT_UIMODE != "EXTRA":
        MC.symbolButton("PREPROD_SYMBOLBUTTON", edit=True, image=ICONS_PATH + "preprodModeOff_icon.png")
        MC.symbolButton("PROD_SYMBOLBUTTON", edit=True, image=ICONS_PATH + "prodModeOff_icon.png")
        MC.symbolButton("EXTRA_SYMBOLBUTTON", edit=True, image=ICONS_PATH + "extraModeOn_icon.png")
        CURRENT_UIMODE = "EXTRA"

        MC.columnLayout("PREPROD_PLACEHOLDER", edit=True, manage=0)
        MC.columnLayout("PROD_PLACEHOLDER", edit=True, manage=0)
        MC.columnLayout("EXTRA_PLACEHOLDER", edit=True, manage=1)

        MC.window("YAKARI_renderLibraryUI_WIN", edit=True, w=NODEDUMPER_WINDOW_SIZE[0], h=NODEDUMPER_WINDOW_SIZE[1])

        clearLog()
        printLog("[EXTRA MODE]")
        printLog("Ready...")

def listLayers_DEBUG(*args):
    pass

def HTMLFormatter(title="", rowList=[], width=100):
    code = "<p width: 200px;>"
    code += "<font size=\"5\"><b>" + title + "</b></font><font size=\".5\"><br>" + "-"*width + "</font>"
    code += "<font size=\"5\">"
    for row in rowList:
        code = code + "<br>" + row
    code += "</font></p>"    
    return code














"""
==================================================================================================================================================
--------------------------------------------------------------------------------------------------------------------------------------------------
88                                                            88888888ba,                                                                          
88                                                            88      `"8b                                                                         
88                                                            88        `8b                                                                        
88           ,adPPYYba,  8b       d8   ,adPPYba,  8b,dPPYba,  88         88  88       88  88,dPYba,,adPYba,   8b,dPPYba,    ,adPPYba,  8b,dPPYba,  
88           ""     `Y8  `8b     d8'  a8P_____88  88P'   "Y8  88         88  88       88  88P'   "88"    "8a  88P'    "8a  a8P_____88  88P'   "Y8  
88           ,adPPPPP88   `8b   d8'   8PP"""""""  88          88         8P  88       88  88      88      88  88       d8  8PP"""""""  88          
88           88,    ,88    `8b,d8'    "8b,   ,aa  88          88      .a8P   "8a,   ,a88  88      88      88  88b,   ,a8"  "8b,   ,aa  88          
88888888888  `"8bbdP"Y8      Y88'      `"Ybbd8"'  88          88888888Y"'     `"YbbdP'Y8  88      88      88  88`YbbdP"'    `"Ybbd8"'  88          
                             d8'                                                                              88                                   
                            d8'                                                                               88
                                          

     ,adPPYba,   ,adPPYba,   8b,dPPYba,   ,adPPYba,                                                                                                
    a8"     ""  a8"     "8a  88P'   "Y8  a8P_____88                                                                                                
    8b          8b       d8  88          8PP"""""""                                                                                                
    "8a,   ,aa  "8a,   ,a8"  88          "8b,   ,aa                                                                                                
     `"Ybbd8"'   `"YbbdP"'   88           `"Ybbd8"'    
--------------------------------------------------------------------------------------------------------------------------------------------------
==================================================================================================================================================
"""
def getShader(node):
    # "getShader()" will ALWAYS be called AFTER a "detectSceneAnomalies()"; hence no extra check is needed!!!
    if MC.nodeType(node) == "mesh":
        # node was a mesh
        mesh = node
    elif MC.nodeType(node) == "transform" and MC.listRelatives(node, children=True, type="mesh") != None:
        # node was a transform with a mesh
        mesh = MC.listRelatives(node, children=True, type="mesh")[0]   
    else:
        # it's pointless to ask for a shader here; ABORT
        fatality("Proc getShader() works only for transform and [mesh]!\nThe node " + node + " is not a meshNode!", [node])
    shader = None
    shadingEngine = MC.listConnections(mesh, type="shadingEngine", source=False, destination=True)[0]
    shader = MC.listConnections(shadingEngine + ".surfaceShader", source=True, destination=False)[0]
    if MC.nodeType(shader) in SHADER_TYPES:
        return shader
    else:
        # not a default shader: ABORT
        mesh = getShortDAGPath(mesh)
        fatality("The shader:\n  -  " + shader + "\napplied to mesh:\n  -  " + mesh + "\nis of type " + MC.nodeType(shader) + ", NOT standard for YAKARI.", [shader, mesh, shadingEngine])        
        
def isADumpableTransform(node):
    """ DEBUG """
    0000; funcDebug()
    0000; printDebug("node: " + node)
    0000; printDebug("type: " + MC.nodeType(node))


    nodeType = MC.nodeType(node)
    shapes = MC.listRelatives(node, children=True, shapes=True, noIntermediate=True)
    if nodeType == "transform":
        if shapes != None:
            # accept only transforms
            for shape in shapes:
                # accept only locatorTransforms ans meshTransforms
                if MC.nodeType(shape) not in ["mesh", "locator"]:
                    return False
            # if you are here, it's a mesh/locator transform
            return True        
        else:
            # a shapeless transform, good
            return True
    else:
        # only TRANSFORMS
        return False       

def isADumpableAttribute(attr):
    # YAKARI has not transform overrides
    undumpableAttributes = ["translate", "rotate", "scale", "shear",
                            "translateX", "translateY", "translateZ", 
                            "rotateX", "rotateY", "rotateZ",
                            "scaleX", "scaleY", "scaleZ",
                            "visibility"]
    if attr not in undumpableAttributes:
        return True
    else:
        return False

def getLayerAdjustments(inLayer):
    """ DEBUG """
    0000; funcDebug()
    0000; printDebug("layer: " + inLayer)


    appendReport("Dumping layer '" + inLayer +"'", upperBar=True, newLines=1)

    #-----------------------------------------------------------------------------------------------------------------------------------    
    # Layer membership (accept only TRANSFORMS)
    #----------------------------------------------------------------------------------------------------------------------------------- 
    appendReport("Membership (only mesh/locator transforms accepted):")
    nodesDict = {}    
    layerNodes = MC.editRenderLayerMembers(inLayer, query=True, fullNames=True)
    0000; printDebug("member nodes: ", layerNodes)
    
    # NO EMPTY LAYER ALLOWED
    if layerNodes == None:
        fatality("The following render layer is empty:\n - " + inLayer)

    for layerNode in layerNodes:
        if isADumpableTransform(layerNode):
            nodesDict[layerNode] = {}
            nodesDict[layerNode]["LAYERMEMBERSHIP"] = True  
            appendReport("[OK] " + getShortDAGPath(layerNode))

        else:    
            layerNode = getShortDAGPath(layerNode)
            appendReport("[REJECTED] " + layerNode) 

    # ACTIVE THE PROGRESS LINE:
    #progressBarInitialize(numberOfTasks= len(getActiveIDs(inLayer + ".adjustments")) + len(getActiveIDs(inLayer + ".outAdjustments")))

    #-----------------------------------------------------------------------------------------------------------------------------------    
    # Manage renderLayer's "outAdjustments" (i.e. CONNECTION OVERRIDES: in this case, SHADING ENGINE OVERRIDES)
    #----------------------------------------------------------------------------------------------------------------------------------- 
    appendReport("\nConnection overrides:")
    activeIndices = getActiveIDs(inLayer + ".outAdjustments") # Returns [] if no shadingEngine override present
    for index in activeIndices:
        mesh = getNodeFromPlug(inLayer + ".outAdjustments[" + str(index) + "].outPlug")
        if mesh != None:
            transform = getParent(mesh)
            if not transform in layerNodes:
                # WEIRD: the mesh is not visible but it has a connection override... SKIP IT
                mesh = getShortDAGPath(mesh)
                transform = getShortDAGPath(transform)
                appendReport("[SKIPPED] The pair ('" + mesh + "', '" + transform + "') doesn't belong to this layer,\n          but yet has a CONNECTION OVERRIDE (probably an orphan shaderOverride)")
                continue
            shadingEngines = MC.listConnections(inLayer + ".outAdjustments[" + str(index) + "].outValue")
            if shadingEngines != None:
                shaders = MC.listConnections(shadingEngines[0] + ".surfaceShader", source=True, destination=False)
                if shaders != None:
                    if MC.nodeType(shaders[0]) in SHADER_TYPES:
                        nodesDict[transform]["OVERRIDESHADER"] = shaders[0]
                        appendReport("[OK] shaderOverride '"+ mesh + "' = '" + shaders[0] + "'")
                    else:
                        # an shaderOverride not standard for YAKARI
                        mesh = getShortDAGPath(mesh)
                        fatality("The overriding shader:\n  -  " + shaders[0] + "\napplied to mesh:\n  -  " + mesh + "\nin layer:\n  -  " + inLayer + "\nis of type " + MC.nodeType(shaders[0]) + ", NOT standard for YAKARI.", [shaders[0], mesh, shadingEngines[0]])        
                else: 
                    # empty shadingEngine
                    mesh = getShortDAGPath(mesh)
                    fatality("The overriding shadingEngine:\n  -  " + shadingEngines[0] + "\napplied to mesh:\n  -  " + mesh + "\nin layer:\n  -  " + inLayer + "\nis empty!", [shadingEngines[0], mesh])
            else:
                # weird connectionOverride
                mesh = getShortDAGPath(mesh)
                fatality("Layer:\n  -  " + inLayer + "\nhas an unknown override connection for mesh:\n  -  " + mesh, [mesh])
        progressBarIncrement()        
    if len(activeIndices) == 0:
        appendReport("None")

    #-----------------------------------------------------------------------------------------------------------------------------------    
    # Manage renderLayer's "adjustments" (i.e. ATTRIBUTE OVERRIDES: no new connections)
    #-----------------------------------------------------------------------------------------------------------------------------------    
    appendReport("\nAttribute overrides:")
    activeIndices = getActiveIDs(inLayer + ".adjustments") # Returns [] if no attributeOverride present
    for index in activeIndices:
        potentialConnection = getNodeFromPlug(inLayer + ".adjustments[" + str(index) + "].plug")
        if potentialConnection != None:
            # DETECT ANIMCURVES ORPHANS
            # (a VALUE without a PLUG)
            node = getDAGPath(getNodeFromPlug(inLayer + ".adjustments[" + str(index) + "].plug"))
            attribute = getAttrFromPlug(inLayer + ".adjustments[" + str(index) + "].plug")
            if isADumpableAttribute(attribute):
                if not node in nodesDict:
                    # it's an override belonging to an outsider node (not a transform in the current layer)
                    nodesDict[node] = {}
                nodesDict[node][attribute] = MC.getAttr(inLayer + ".adjustments[" + str(index) + "].value")
                appendReport("[OK] attribute '" + getShortDAGPath(node) + "." + attribute + "' overrided")
            else: 
                appendReport("[REJECTED] attribute '" + getShortDAGPath(node) + "." + attribute + "'")  

        progressBarIncrement()        
    if len(activeIndices) == 0:
        appendReport("None")            

    # COMPLETED    
    appendReport("\n\n")
    return nodesDict

def collectLayersSetup(*args):
    clearReport()
    appendReport("START DUMPING", bars=True, barSymbol="=", newLines=0)

    # Before dumping, check the integrity of the scene (meshes and shaders)
    detectSceneAnomalies()
    appendReport("[OK] No primary mesh/shading anomalies found!")
    appendReport("\n\n")
    
    settings    = {}
    layersSetup = {}

    #---------------------------------------------------
    # GLOBALS
    #---------------------------------------------------
    appendReport("Dumping defaultSettings", upperBar=True, newLines=1)
    for defaultSetting in DEFAULT_SETTINGS:
        settings[defaultSetting] = MC.getAttr(defaultSetting)    
        appendReport("[OK] attribute '" + defaultSetting + "' dumped")
    appendReport("\n\n")

    #---------------------------------------------------
    # DEFAULT RENDER LAYER
    #---------------------------------------------------
    appendReport("Dumping 'defaultRenderLayer'", upperBar=True, newLines=1)
    layersSetup["defaultRenderLayer"] = {} 
    MC.editRenderLayerGlobals(currentRenderLayer="defaultRenderLayer") # now every mesh receive the original unoverridden shaders
    defaultLayerNodes = MC.editRenderLayerMembers("defaultRenderLayer", query=True, fullNames=True)
    if defaultLayerNodes == None:
        # Empty shene: ABORT
        return
    # Identify only visible meshes (so, no intermediates, if any)
    """ BE WARNED, if the camera is in the scene; it's fake nurbs (a shaderless mesh) will be detected as anomlaky or dumped (it's name is "XXXShape")"""
    defaultLayerMeshes = [node for node in defaultLayerNodes if (MC.nodeType(node) == "mesh" and MC.ls(node, visible=True) and "XXXShape" not in node)]


    # INITIALIZE PROGRESS BAR
    # make a global list of what we have to do
    thingsToDo = len(defaultLayerMeshes)

    validLayers = []
    sceneLayers = MC.ls(type="renderLayer") 
    for layer in sceneLayers:
        if layer != "defaultRenderLayer" and getNamespace(layer) == "" and not MC.referenceQuery(layer, isNodeReferenced=True):
            if not "renderLayerManager" in MC.listConnections(layer, type="renderLayerManager", destination=False):
                appendReport("[WARNING] Layer " + layer + " is connected to a secondary LayerManager; it will be skipped!")
                continue
            validLayers.append(layer)
            thingsToDo = thingsToDo + len(getActiveIDs(layer + ".adjustments")) + len(getActiveIDs(layer + ".outAdjustments"))
        
    progressBarInitialize(numberOfTasks=thingsToDo)

    
    for mesh in defaultLayerMeshes:
        # please dump ONLY (mesh)transform names... so that later we don't need to manage weird mesh names!!! 
        layersSetup["defaultRenderLayer"][getParent(mesh)] = {"BASESHADER": getShader(mesh)}
        appendReport("Accepted meshTransform: " + getShortDAGPath(getParent(mesh)))
        appendReport("[OK] Dumped shader '" + getShader(mesh) + "' ")
        for attr in MESH_DUMP_ATTRS:
            layersSetup["defaultRenderLayer"][getParent(mesh)][attr] = MC.getAttr(mesh + "." + attr)
            appendReport("[OK] Dumped attribute: '" + getShortDAGPath(mesh) + "." + attr +"' dumped")
        appendReport("")
        progressBarIncrement()    
    appendReport("\n")

    #---------------------------------------------------
    # All the other layers
    #---------------------------------------------------
    
    for layer in validLayers:
        layersSetup[layer] = getLayerAdjustments(layer)

    #---------------------------------------------------
    # Assemble and return the final dictionary
    #---------------------------------------------------
    sceneSetup = {"settings": settings, 
                  "layers":   layersSetup}
    progressBarHide()              
    return sceneSetup

def detectSceneAnomalies(*args):
    clearFatality()

    #--------------------------------------------------------
    # Work in DAGPath (scenes have A LOT of ambiguities)
    #--------------------------------------------------------

    # DIRECT ABORT if any anomaly is found!
    activeMeshes = MC.ls(type="mesh", noIntermediate=True, visible=True, long=True)
    for mesh in activeMeshes:
        """ 
        Here I pay the price to having been "cool". The shape of the HD camera is a mesh (not a nurbs) 
        (and it's name is a plain fucking "XXXShape")      
        """
        if "XXXShape" in mesh:
            # it's the fake nurbs; skip it
            continue

        # Detect INSTANCES + MULTIPLESHAPES
        parents = MC.listRelatives(mesh, allParents=True, fullPath=True)
        if len(parents) != 1:
            mesh = getShortDAGPath(mesh)
            culprits = [mesh] + parents
            fatality("The mesh:\n  -  " + mesh + "\nis instanced!", culprits)        
        parent = parents[0]       
        shapes = MC.listRelatives(parent, shapes=True, fullPath=True, noIntermediate=True)

        if len(shapes) != 1:
            parent = getShortDAGPath(parent)
            fatality("The transform:\n  -  " + parent + "\nhas multiple shapes attached!", [parent])                
        
        # Detect shading anomalies
        shadingEngines = MC.listConnections(mesh, type='shadingEngine', source=False, destination=True)
        if shadingEngines != None:
            if len(shadingEngines) > 1:
                # Component shader detected: ABORT
                mesh = getShortDAGPath(mesh)
                fatality("The mesh:\n  -  " + mesh + "\nhas probably \"per-component\" shadingEngines!", [mesh])        
            else:
                # Has the shadingEngine a shader connected?
                if MC.listConnections(shadingEngines[0] + ".surfaceShader", source=True, destination=False) == None:
                    mesh = getShortDAGPath(mesh)
                    fatality("The shadingEngine:\n  -  " + shadingEngines[0] + "\nconnected to the mesh:\n  -  " + mesh + "\nis empty!", [mesh, shadingEngines[0]])        
        else: 
            # ShadingEngineless mesh: ABORT
            mesh = getShortDAGPath(mesh)
            fatality("The mesh:\n  -  " + mesh + "\nhas no shadingEngine!", [mesh])
    # If we get here, we have single meshes and each one has EXACTLY ONE shadingEngine (with a shader) directly 
    # connected (the overrides are linked to the renderLayers) and no weird "component shading" shit!!!  
    printLog("")
    printLog("No primary mesh/shading anomalies detected.", "OK")
    inViewMessage(message="No primary MESH/SHADING anomaly found!", position="botLeft", time=1500, status="SUCCESS")       

def deleteExtraLayers():
    printLog("\nDELETING EXTRA RENDER LAYERS")
    deletableLayers = []
    sceneLayers = MC.ls(type="renderLayer") 

    referencedLayers = []

    for layer in sceneLayers:
        # Don't touch  anomalous layers
        if MC.referenceQuery(layer, isNodeReferenced=True) and "defaultRenderLayer" not in layer:
            # Avoid the "defaultRenderLayer"
            referencedLayers.append(layer)

        if layer != "defaultRenderLayer" and not MC.referenceQuery(layer, isNodeReferenced=True):
        #if layer != "defaultRenderLayer" and getNamespace(layer) == "" and not MC.referenceQuery(layer, isNodeReferenced=True):

            if not "renderLayerManager" in MC.listConnections(layer, type="renderLayerManager", destination=False):
                printLog("Layer '" + layer + "' is connected to a secondary LayerManager.\nIt won't be erased!", "WARNING")
                continue
            deletableLayers.append(layer)
    
    try:        
        MC.editRenderLayerGlobals(currentRenderLayer="defaultRenderLayer")   
    except RuntimeError as error:
        fatality("The 'DefaultRenderLayer' is CORRUPTED:\n" + str(error))

    # Now, just delete the layer nodes; the shadingEngines are respected and everything is just fine 
    progressBarInitialize(len(deletableLayers))
    for layer in deletableLayers:
        MM.eval("renderLayerEditorDeleteLayer RenderLayerTab " + layer + ";")
        printLog("Extra layer '" + layer + "' deleted!", "SUCCESS")
        progressBarIncrement()
    progressBarHide()    
    
    if len(deletableLayers) == 0:
        printLog("No deletable extra rendering layer found.", "NULL")
    else: 
        inViewMessage(message="Extra RENDER LAYERS deleted!", position="topLeft", time=2000, status="SUCCESS")  

    # CLEAN THE DEFAULT RENDER LAYER BY "DELETING IT"
    # If you don't, parasitic connections will stay there and IT'S GONNA BE A HUGE MESS
    MM.eval("renderLayerEditorDeleteLayer RenderLayerTab defaultRenderLayer;")
    
    if len(referencedLayers) > 0:
        badAssets = set()
        for layer in referencedLayers:
            if ":" in layer:
                badAssets.add(layer.split(":")[0])
        badAssets = list(badAssets)
        if len(badAssets):
            message = "The following <assets> have referenced <render layers>:\n" 
            for badAsset in badAssets:
                message += "  -  " + badAsset + "\n"
            message += "\nPlease check the corresponding <referenced files>!"
        else:
            message = "The scene has some unknown referenced <render layers>.\nCan't proceed, sorry!"    
        
        fatality(message=message, title="REFERENCED LAYERS ERROR")


def doDeleteExtraLayers(*args):
    # bof
    deleteExtraLayers()

def doApplyRenderDefaults(*args):
    """
    --> FUNDAMENTAL LESSON:
        Don't EVER try to delete/rearrange maya nodes without passing by MEL scripts!!!
        Every action done via the interface is NOT a simple connection/node deletion...
        If you erase these nodes, the MENTAL RAY interface is TOTALLY FUCKED!!!
    This for examples, destroys irreversibly mentalRay's interface:

    # Delete MentalRay nodes
    for node in ["miDefaultOptions", 
                 "mentalrayItemsList", 
                 "mentalrayGlobals", 
                 "miDefaultFramebuffer"]:
        if MC.objExists(node):
            MC.delete(node)
    """
    
    printLog("\nAPPLYING MENTAL RAY PRESETS")

    # make sure MENTAL RAY is here:
    if not MC.pluginInfo("Mayatomr", query=True, registered=True):
        fatality("Can't find needed plugin 'Mayatomr'!")
    if not MC.pluginInfo("Mayatomr", query=True, loaded=True):
        MC.loadPlugin("Mayatomr", quiet=True)
    # Check if that shitty "rayTracingCtrl" exists. If it doen't, do this...
    MC.setAttr("defaultRenderGlobals.currentRenderer", "mentalRay", type="string")
    MM.eval("miCreateDefaultNodes;")

    #------------------------------------------------------------
    # Manually force the creation of the infamous "quality tab"
    #------------------------------------------------------------
    MM.eval("unifiedRenderGlobalsWindow")
    MM.eval('toggleWindowVisibility unifiedRenderGlobalsWindow')
    MM.eval('tabLayout -e -selectTab "mentalRayQualityTab" unifiedRenderGlobalsWindow|rgMainForm|tabForm|mentalRayTabLayout;')
    MM.eval('fillSelectedTabForCurrentRenderer')
    #MM.eval("rendererChanged;")
    #MC.setAttr("miDefaultOptions.stringOptions[29].value", False) # this happens when you select "legacySamplingMode" and "customSampling"
    #MC.setAttr("miDefaultOptions.stringOptions[32].value", 100)
    MC.setAttr("miDefaultOptions.miRenderUsing", 2)
    MM.eval('miSetRenderUsingValue') 

    # Load YAKARI's renderingNodes dump and apply it
    # ACTIVATE DEFAULT RENDER LAYER; otherwise it will override the attrs
    MC.editRenderLayerGlobals(currentRenderLayer="defaultRenderLayer") 
    
    loadNodesDump([MENTALRAY_NODESDUMP_PATH + "YAKARI_preset.txt"])
    
    # Applying the YAKARIdefault puts resolution ratio to ZERO!!!
    MC.setAttr("defaultResolution.height", 1080)
    MC.setAttr("defaultResolution.width", 1920)
    MC.setAttr("defaultResolution.pixelAspect", 1)
    MC.setAttr("defaultResolution.deviceAspectRatio", 1.778)  

    # SET FILMTER TO "MITCHELL"
    MC.setAttr("miDefaultOptions.filter", 3)
    
    printLog("'YAKARI rendering settings' applied!", "SUCCESS")
    inViewMessage(message="YAKARI RENDER SETTINGS applied!", position="topLeft", time=2000, status="SUCCESS")

def pipelineSaveDump(*args):
    # PIPELINE PATH for CH and PR
    sceneTag = MC.textField("saver_sceneIDLabel_textField", query=True, tx=True)
    category = sceneTag[0:2]
    path = PROJECT_ROOT + category + "/" + sceneTag + "/tex/maya/" + sceneTag + "_REN.txt"
    saveDump(path)
    
def manualSaveDump(*args):
    # MANUAL PATH
    paths = MC.fileDialog2(fileFilter="*.txt", fileMode=0, dialogStyle=1, caption="Save the rendering info into a '_REN.txt' file:")
    if paths == None or len(paths) == 0:
        printLog("ABORTED", "NULL")
        return False
    else:
        saveDump(paths[0])  

def saveDump(path):
    # pipeline/manual saves converge HERE
    if path == None:
        return False
    layersSetup = collectLayersSetup()
    try:
        dump = JSON.dumps(layersSetup, indent=2)
        f = open(path, "w")
        f.write(dump)
    except Exception as e:
        fatality ("Saving renderLayers dump to file:\'" + path + "\'\nFAILED!\n" + str(e))
    finally:
        if f != None:
            f.close()
    printLog("RenderLayers dumped to file:\n                    '" + path + "'", "SUCCESS")
    showReport("DUMP SUCCEEDED", "SUCCESS")
    inViewMessage(message="RENDERING DATA dumped to:\n" + path, position="topLeft", time=3500, status="SUCCESS")
    
    # Refresh the scene info, now that the dump exists
    sceneListener()
    # DEBUG dump
    # print JSON.dumps(layersSetup, indent=2)

def pipelineLoadDump(*args):
    #------------------------------
    # clean the scene and initialize the report
    deleteExtraLayers()
    doApplyRenderDefaults()
    clearReport()
    appendReport("APPLYING DUMP", bars=True, barSymbol="=", newLines=0)
    
    # PIPELINE PATH for CH and PR
    sceneTag = MC.textField("saver_sceneIDLabel_textField", query=True, tx=True)
    category = sceneTag[0:2]
    path = PROJECT_ROOT + category + "/" + sceneTag + "/tex/maya/" + sceneTag + "_REN.txt"
    loadDumpPreProd(path)

    showReport("DUMP SUCCEEDED", "SUCCESS")
    printLog("RenderLayersDump applied!", "SUCCESS")

def manualLoadDump(*args):
    #------------------------------
    # clean the scene and initialize the report   
    deleteExtraLayers()
    doApplyRenderDefaults()
    clearReport()
    appendReport("APPLYING DUMP", bars=True, barSymbol="=", newLines=0)
    
    # MANUAL PATH
    paths = MC.fileDialog2(fileFilter="*.txt", fileMode=1, dialogStyle=1, caption="Load the rendering info from a '_REN.txt' file:")
    if paths == None or len(paths) == 0:
        printLog("ABORTED", "NULL")
        return False
    else:
        loadDumpPreProd(paths[0])
    
    showReport("DUMP SUCCEEDED", "SUCCESS")
    printLog("RenderLayersDump applied!", "SUCCESS")

""" ########################### """
""" LOAD DUMP (PREPROD VERSION) """
""" ########################### """
def loadDumpPreProd(path, namespaceContainer=""):
    """ DEBUG """
    0000; funcDebug()
    0000; printDebug("path: " + path)
    0000; printDebug("namespace: " + namespaceContainer)

    #-----------------------------------------------------------------------------------
    # Load the '_REN.txt'
    f = None
    renderLayersDump = None
    try:
        f = open(path, "r")
        renderLayersDump = JSON.loads(f.read())
        printLog("RenderLayersDump loaded for '" + namespaceContainer +"'", "SUCCESS")
    except Exception as e:
        fatality ("Loading renderLayersDump for '" + namespaceContainer + "' FAILED!\n" + str(e))
    finally:
        if f != None:
            f.close()

    #-----------------------------------------------------------------------------------
    # "defaulRenderLayer"
    appendReport("APPLYING THE 'defaultRenderLayer' DUMP",  bars=True, barSymbol="-", newLines=0)

    MC.setAttr("defaultRenderLayer.renderable", False) 
    MC.editRenderLayerGlobals(currentRenderLayer="defaultRenderLayer")
    defaultRenderLayerData = renderLayersDump["layers"]["defaultRenderLayer"]
    renderLayersDump["layers"].pop("defaultRenderLayer") # Remove from list

    # "defaultRenderLayer" has only (mesh)-transforms!!!
    for meshTransformTag in defaultRenderLayerData.keys():
        # FATALITY if it can't found unambiguously the corresponding node in scene
        sceneMeshTransform = smartObjExists(meshTransformTag, type="DAG", namespaceContainer=namespaceContainer)
        if sceneMeshTransform == None:
            fatality("Can't resolve the dumpTag:\n\n - " + meshTransformTag + "\n\n(missing node, hierarchy problems or duplicates)")        
        0000; printDebug("\n----------------------------------------------------------------\nTAG ASSOCIATION:")
        0000; printDebug(meshTransformTag + "      ==>      " + sceneMeshTransform + "\n")

        appendReport("APPLYING DUMP INFO '" + meshTransformTag + "' TO SCENE OBJECT '" + sceneMeshTransform + "'")
        #appendReport("Working on '" + sceneMeshTransform + "'")
        mesh = MC.listRelatives(sceneMeshTransform, shapes=True, noIntermediate=True, path=True)[0] # AVOID INTERMEDIATES + return A VALID NAME ()DAG PATH REQUIRED)
        meshData = defaultRenderLayerData[meshTransformTag]
        
        #---------------------------------------------------------------------------------
        # Assign base shader
        shaderTag = meshData.pop("BASESHADER")

        # There can be ONLY a "lambert1" (even namespaced) in the scene
        # Thus, the tag "XXXX:lambert1" must be associated to "lambert1", disregarding the namespace confinement rule
        if shaderTag[shaderTag.rfind(":")+1:] == "lambert1":
            sceneShader = "lambert1"
        else:    
            sceneShader = smartObjExists(shaderTag, type="DG", namespaceContainer=namespaceContainer)
        
        if sceneShader != None:
            shadingEngines = MC.listConnections(sceneShader + ".outColor", destination=True, source=False, type="shadingEngine")
            if shadingEngines != None:
                if len(shadingEngines) == 1:
                    0000; printDebug("Applying shader " + sceneShader + "(" + shadingEngines[0]+ ") to mesh " + mesh)
                    MC.sets(mesh, edit=True, forceElement=shadingEngines[0])
                    appendReport("[OK] Base shader applied '" + sceneShader + "'")
                else: 
                    if sceneShader == "lambert1":
                        # The "lambert1" is an ecception: it's connected to the particle shadingEngine too
                        MC.sets(mesh, edit=True, forceElement="initialShadingGroup")
                        appendReport("[OK] 'lambert1' applied")
                    else:
                        fatality("The shader:\n" + sceneShader + "\nhas more than one shadingEngine: CAN'T CHOOSE!", culprits=[sceneShader])
            else: 
                fatality("The shader:\n" + sceneShader + "\nhas NO shadingEngine", culprits=[sceneShader])
        else:
            fatality("Can't find shader <b>" + shaderTag + "</b> for mesh <b>" + sceneMeshTransform + "</b> <br>iIt was dumped, but missing here!", culprits=[sceneMeshTransform], title="\"_REN\" ERROR")

        #---------------------------------------------------------------------------------
        # Attributes
        for attr in meshData:
            attrFullname = mesh+ "." + attr
            if MC.attributeQuery(attr, node=mesh, exists=True) and MC.getAttr(attrFullname, settable=True):
                setAttr(attrFullname, meshData[attr])
                appendReport("[OK] Base attribute applied '" + getShortDAGPath(mesh) + "." + attr + "'")
            else:
                fatality("The dumped attribute:\n" + attrFullName + "\ndoesn't exist or it's already connected in mesh:\n" + mesh, culprits=[mesh], title="\"_REN ERROR\"")
        
        appendReport("")    

    
    #-----------------------------------------------------------------------------------
    # RenderLayers creation and overriding attributes
    extraLayersDump = renderLayersDump["layers"] 
    
    """ Generate a proper progressBar """
    numberOfTasks = 0
    for layer in extraLayersDump:
        numberOfTasks += len(extraLayersDump[layer])
    progressBarInitialize(numberOfTasks)

    for extraLayer in extraLayersDump.keys():
        
        # The extraLayers must have the correct namespace
        sceneExtraLayer = namespaceContainer + (":" if namespaceContainer != "" else "") + extraLayer
        
        extraLayerInfo = extraLayersDump[extraLayer]
        appendReport("CREATING EXTRA LAYER '" + sceneExtraLayer + "'", bars=True, barSymbol="-", newLines=0)
        
        # Create the new layer and make it active
        ''' THE NEW LAYER MUST HAVE THE PROPER NAMESPACE '''
        newLayer = MC.createRenderLayer(name=sceneExtraLayer, makeCurrent=True, empty=True)
        for nodeTag in extraLayerInfo:
            # "smartObjExists" can detect if the override has to be done on a rendering node and act consequently
            sceneNode = smartObjExists(nodeTag, type="GENERIC", namespaceContainer=namespaceContainer)
            if sceneNode != None:
                appendReport("APPLYING DUMP INFO '" + nodeTag + "' TO SCENE NODE '" + sceneNode + "'")
                nodeInfo = extraLayerInfo[nodeTag]
                #-----------------------------------------------------------
                # membership
                if "LAYERMEMBERSHIP" in nodeInfo.keys():
                    """
                    Only a transform can have this flag; put it in the layer... BUT:  
                    To avoid parasitic membership of lights and cameras, apply ONLY membership of MESH TRANSFORMS
                    """
                    meshChildren = MC.listRelatives(sceneNode, children=True, type="mesh")
                    if meshChildren != None:
                        # it's a transform with a valid mesh... membership possible 
                        MC.editRenderLayerMembers(newLayer, sceneNode, noRecurse=True)
                        appendReport("[OK] Layer membership")
                    nodeInfo.pop("LAYERMEMBERSHIP")
                #-----------------------------------------------------------
                # shader    
                if "OVERRIDESHADER" in nodeInfo.keys():
                    shaderTag =  nodeInfo["OVERRIDESHADER"]
                    sceneShader = smartObjExists(shaderTag, type="DG", namespaceContainer=namespaceContainer)
                    if sceneShader != None:
                        shadingEngines = MC.listConnections(sceneShader + ".outColor", destination=True, source=False, type="shadingEngine")
                        if shadingEngines != None and len(shadingEngines) == 1:
                            mesh = MC.listRelatives(sceneNode, shapes=True, noIntermediate=True, path=True)[0] # Again, we have ambiguity on names
                            MC.sets(mesh, edit=True, forceElement=shadingEngines[0])
                            appendReport("[OK] Shader override '" + sceneShader + "'")
                        else:
                            fatality("Bad/missing shading engine for shader:\n" + sceneShader, culprits=[mesh, sceneShader])
                    else:
                        print newLayer
                        print nodeTag
                        print sceneNode
                        fatality("MISSING SHADER\n\nThe shader:\n  -  " + shaderTag + 
                                 "\nwas dumped as override of mesh:\n  -  " + nodeTag + 
                                 "\nfor renderLayer: \n  -  " + extraLayer + 
                                 "\nbut MISSING here!", culprits=[sceneNode], title="[LOAD DUMP ERROR]") 
                    nodeInfo.pop("OVERRIDESHADER")
                #-----------------------------------------------------------
                # attribute overrides
                for attr in nodeInfo.keys():
                    attrFullname = sceneNode + "." + attr
                    MC.editRenderLayerAdjustment(attrFullname) #now what follow will be an override on the active render layer 
                    setAttr(attrFullname, nodeInfo[attr]) 
                    appendReport("[OK] Attribute override '" + getShortDAGPath(sceneNode) + "." + attr + "'")
            else:
                fatality("The following dump tag can't be resolved:\n" + nodeTag)

            appendReport("")
            progressBarIncrement()

        # End of construction for this layer
        appendReport("\n\n")
    
    # End of layer construction   
    appendReport("")  
    progressBarHide()

def pipelineGlobalLoadDumps(*args):
    """ DEBUG """
    0000; funcDebug()

    printLog("\n-------------------------------------------------------")    
    printLog("APPLYING DUMPS GLOBALLY + PROCESSING")
    printLog("-------------------------------------------------------")    

    # always deactivate the viewport 2.0 (but save user's preferences)
    deactivateViewport20()
    
    # Detect if there's something to do
    thingsToDo = 0
    for assetNamespace in ASSETS_DATA:
        if ASSETS_DATA[assetNamespace][0] == None:
            # UNKNOWN; ignore
            continue
        if "ch_" not in assetNamespace and "pr_" not in assetNamespace:
            # it's not pr or ch; no dump
            continue   
        else: 
            thingsToDo += 1     
    if thingsToDo == 0:
        printLog("No asset detected!", "NULL")
        return
    

    #------------------------------
    # clean the scene    
    deleteExtraLayers()
    doApplyRenderDefaults()
    clearReport()
    appendReport("APPLYING DUMPS GLOBALLY", bars=True, barSymbol="/", newLines=0)

    refreshAssetsList() # it calls "build_ASSETS_DATA()" too

    printLog("\nAPPLYING DUMPS TO SCENE ASSETS")

    for assetNamespace in ASSETS_DATA:

        if ASSETS_DATA[assetNamespace][0] == None: 
            # UNKNOWN: ignore
            continue
        
        if "ch_" not in assetNamespace and "pr_" not in assetNamespace:
            # you need to cycle only PR and CH!!
            continue    
        

        """ TEEPEE FIX """
        if "pr_tdo02" in assetNamespace:
            # "pr_tdo02" is in reality an SS: skip it
            teepeeDebugPrint("_REN skipped for pr_tdo02 (it's an SS)")
            continue  
        """ TEEPEE FIX END """    


        if ASSETS_DATA[assetNamespace][1] == None:
            # without _REN: skip but create a list of warnings
            printLog("The asset '" + assetNamespace + "' has no '_REN'; it'll be skipped!", "WARNING")
            continue
        
        0000; printDebug("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        0000; printDebug("WORKING ON ASSET: " + assetNamespace)
        0000; printDebug("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

        # ASSETS_DATA = {assetNamespace: [assetID, RENPath, AMBPath, [amb1, amb2, ..., ambk]]}
        appendReport("WORKING ON ASSET '" + assetNamespace + "' (YAKARI ID: " + ASSETS_DATA[assetNamespace][0] + ")", bars=True, barSymbol="=", newLines=0)
        loadDump(ASSETS_DATA[assetNamespace][1], namespaceContainer=assetNamespace)
        0000; printDebug("\n\n\n")

    # move to defaultRenderLayer
    MC.editRenderLayerGlobals(currentRenderLayer="defaultRenderLayer")
    showReport("DUMPS GLOBALLY APPLIED", "SUCCESS")
    printLog("Dumps globally applied!", "SUCCESS")




    #---------------------------------------------------------------------------------
    # POST PROCESSING
    #---------------------------------------------------------------------------------
    printLog("\n-------------------------------")    
    printLog("POST DUMP PROCESSING")
    printLog("-------------------------------")    

    if POSTAPPLYDUMP_MANAGENORMALLIGHTS_FLAG:
        postApplyDump_manageNormalLights()

    if POSTAPPLYDUMP_MANAGECOLOR_LIGHTLAYERS_FLAG:
        postApplyDump_manageCOLOR_LIGHTLayers()
    
    if POSTAPPLYDUMP_MANAGESHADOWLIGHTS_FLAG:
        postApplyDump_manageShadowLights()

    if POSTAPPLYDUMP_CORRECTALEMBICLIGHTLINKERBUG_FLAG:
        postApplyDump_correctAlembicLightLinkerBug()

    if POSTAPPLYDUMP_CORRECTALEMBICVISIBILITYBUG_FLAG:
        postApplyDump_correctAlembicVisibilityBug()

    if POSTAPPLYDUMP_RENDERINGMISCELLANEA_FLAG:
        postApplyDump_renderingMiscellanea()

    combineAssetLayer_writeCallback()
    """
    if POSTAPPLYDUMP_WRITEGROUPSHOTGUN_FLAG:
        postApplyDump_writeGroupsShotgun()
    """
    
    if POSTAPPLYDUMP_MAKESSVISIBLE_FLAG:
        postApplyDump_makeSSVisible()



    #------------------------------------------------------
    # AUTO "DAY AMBIENT" APPLY
    #------------------------------------------------------
    MC.optionMenu("chosenGlobalPreset_optionMenu", edit=True, value="DAY")
    MC.refresh()
    applyGlobalPreset()

    # ORDER RENDER LAYERS
    orderRenderLayers()
    

    """"""
    # Apply a renderSmooth (with the chosen level) and save for 3DSMAX
    applyRenderingSmoothGlobally()
    save3DsMaxData()
    """"""
    
    # Restore the viewport rendering preference
    restoreViewports()

    inViewMessage(message="SUCCESS", position="topLeft", time=2000, status="SUCCESS")






# The horrid global dictionary used to save viewport info
VIEWPORTS_INFO = {} 

def deactivateViewport20(*args):
    global VIEWPORTS_INFO
    VIEWPORTS_INFO.clear()
    # A "viewport" is a panel of type "modelPanel"
    modelPanels = [panel for panel in MC.getPanel(all=True) if MC.getPanel(typeOf=panel) == "modelPanel"]
    for panel in modelPanels:
        # Save user viewport rendering preferences
        VIEWPORTS_INFO[panel] = MC.modelEditor(panel, query=True, rendererName=True)
        MC.modelEditor(panel, edit=True, rendererName="base_OpenGL_Renderer")
        
def restoreViewports(*args):
    for panel in VIEWPORTS_INFO:
        # restore user viewport rendering preferences
        MC.modelEditor(panel, edit=True, rendererName=VIEWPORTS_INFO[panel])

def orderRenderLayers(*args):
    # Easier than it could seem!
    # Only the "display layers" have a sorting option
    # Here, we get from renderLayerManager the layer list (with proper names) and reorder everything via the ".displayOrder" attribute of each layer
    renderLayers = MC.listConnections("renderLayerManager.renderLayerId")
    numberOfLayers = len(renderLayers)

    renderLayers.remove("defaultRenderLayer")
    sortedRenderLayers = sorted(renderLayers)
    
    for index, layer in enumerate(sortedRenderLayers):
        MC.setAttr(layer + ".displayOrder", numberOfLayers - index - 1)



#------------------------------------------------------------------------------------------------------
# POST "APPLY DUMP" OPERATIONS WINDOW
#------------------------------------------------------------------------------------------------------
POSTAPPLYDUMP_MANAGENORMALLIGHTS_FLAG           = True
POSTAPPLYDUMP_MANAGECOLOR_LIGHTLAYERS_FLAG      = True
POSTAPPLYDUMP_MANAGESHADOWLIGHTS_FLAG           = True
POSTAPPLYDUMP_CORRECTALEMBICLIGHTLINKERBUG_FLAG = True
POSTAPPLYDUMP_CORRECTALEMBICVISIBILITYBUG_FLAG  = True
POSTAPPLYDUMP_RENDERINGMISCELLANEA_FLAG         = True
POSTAPPLYDUMP_WRITEGROUPSHOTGUN_FLAG            = True
POSTAPPLYDUMP_MAKESSVISIBLE_FLAG                = True

def granularOptions(*args):
    if MC.window("granularOptions_WIN", ex=1):
        MC.deleteUI("granularOptions_WIN")
    MC.window("granularOptions_WIN", t="GRANULARITY OPTIONS", tlb=1, s=0, mb=0, tb=1)

    # DEACTIVE MAIN WINDOW
    MC.formLayout("GLOBAL_FORM", edit=True, enable=0)
    mainUIGroupButtonsEnable(False)

    GRANULARITY_FORMLAYOUT = MC.formLayout(nd=100)

    0;TEXT_COLUMNLAYOUT = MC.columnLayout(bgc=(.3,.4,.4))
    0;  QtText(label="GRANULARITY OPTIONS", color=(220,240,240),paddingTBLR=(4, 0, 4, 0), margin=0, fontFamily="Arial", fontSize=18, fontWeight="Bold")
    0;  QtText(label="<p align=\"left\">Operations performed after the <b><font color=\"#FFFFFF\">_REN.txt</font></b> is applied.<br>It's only for debugging, you shouldn't modify these!!!</p>", 
               paddingTBLR=(0, 0, 4, 0), color=(160,220,220), fontFamily="Arial", fontSize=14, fontWeight="normal")
    0;  MC.setParent("..")


    0;CLOSE_SYMBOLBUTTON = MC.symbolButton(image=ICONS_PATH + "closeWindow_icon.png", command=closeGranularOptionsUI)

    0;OPERATIONS_ROWCOLUMNLAYOUT = MC.rowColumnLayout(nc=2, cw=[(1,520), (2,20)], co=(1, "left", 10), cal=(1,"right"))
    pointer = OMUI.MQtUtil.findLayout(OPERATIONS_ROWCOLUMNLAYOUT)      
    widget  = SHIBOKEN.wrapInstance(long(pointer), QTGUI.QWidget)
    widget.setStyleSheet("""font-size: 12px;""")

    0;  MC.text(l="")
    0;  MC.text(l="")
    0;  MC.checkBox("postApplyDump_manageNormalLights_checkBox", 
                    label="Import 'normalLights' and share them between all NORMAL layers", 
                    value=POSTAPPLYDUMP_MANAGENORMALLIGHTS_FLAG, 
                    cc=postApplyDump_manageNormalLights_callback)
    0;  MC.symbolButton(image=ICONS_PATH + "execute_icon.png", c=postApplyDump_manageNormalLights, h=20)

    0;  MC.checkBox("postApplyDump_manageCOLOR_LIGHTLayers_checkBox",
                    label="Manage COLOR_LIGHT layers", 
                    value=POSTAPPLYDUMP_MANAGECOLOR_LIGHTLAYERS_FLAG, 
                    cc=postApplyDump_manageCOLOR_LIGHTLayers_callback)
    0;  MC.symbolButton(image=ICONS_PATH + "execute_icon.png", c=postApplyDump_manageCOLOR_LIGHTLayers, h=20)    
    
    0;  MC.checkBox("postApplyDump_manageShadowLights_checkBox",
                    label="If present (usually only in humans), put shadowLights in SHADOWS", 
                    value=POSTAPPLYDUMP_MANAGESHADOWLIGHTS_FLAG, 
                    cc=postApplyDump_manageShadowLights_callback)
    0;  MC.symbolButton(image=ICONS_PATH + "execute_icon.png", c=postApplyDump_manageShadowLights, h=20)
    
    0;  MC.checkBox("postApplyDump_correctAlembicLightLinkerBug_checkBox",
                    label="Correct EXOCORTEX lightLinking bug (WARNING: shape namespaces are still broken!)", 
                    value=POSTAPPLYDUMP_CORRECTALEMBICLIGHTLINKERBUG_FLAG, 
                    cc=postApplyDump_correctAlembicLightLinkerBug_callback)
    0;  MC.symbolButton(image=ICONS_PATH + "execute_icon.png", c=postApplyDump_correctAlembicLightLinkerBug, h=20)    
    
    0;  MC.checkBox("postApplyDump_correctAlembicVisibilityBug_checkBox", 
                    label="Break connections and make visible all the shdw/shdws", 
                    value=POSTAPPLYDUMP_CORRECTALEMBICVISIBILITYBUG_FLAG,
                    cc=postApplyDump_correctAlembicVisibilityBug_callback)
    0;  MC.symbolButton(image=ICONS_PATH + "execute_icon.png", c=postApplyDump_correctAlembicVisibilityBug, h=20)    

    0;  MC.checkBox("postApplyDump_renderingMiscellanea_checkBox", 
                    label="Prefix, renderableCamera, frameRange, deconnectImagePlane, imageSize,\nIf PROJ remove all cameras, reimport the alembic and check if V-stretched", 
                    value=POSTAPPLYDUMP_RENDERINGMISCELLANEA_FLAG,
                    cc=postApplyDump_renderingMiscellanea_callback)
    0;  MC.symbolButton(image=ICONS_PATH + "execute_icon.png", c=postApplyDump_renderingMiscellanea, h=20)      

    0;  MC.checkBox("postApplyDump_writeGroupsShotgun_checkBox", 
                    label="Write in Shotgun's database the assets' grouping", 
                    value=POSTAPPLYDUMP_WRITEGROUPSHOTGUN_FLAG,
                    cc=postApplyDump_writeGroupsShotgun_callback)
    0;  MC.symbolButton(image=ICONS_PATH + "execute_icon.png", c=postApplyDump_writeGroupsShotgun, h=20)      

    0;  MC.checkBox("postApplyDump_makeSSVisible_checkBox", 
                    label="Make all the SS visible", 
                    value=POSTAPPLYDUMP_MAKESSVISIBLE_FLAG,
                    cc=postApplyDump_makeSSVisible_callback)
    0;  MC.symbolButton(image=ICONS_PATH + "execute_icon.png", c=postApplyDump_makeSSVisible, h=20)      

    
    0;  MC.text(l="")
    0;  MC.text(l="")

    # DEBUGGING EXTRA
    0;  MC.rowLayout(nc=3)
    0;  QtButton(handle="printAssetData", label="prettyPrint\nASSETS_DATA", action=print_ASSETS_DATA,  
                 lineColor=CYAN_L, background=CYAN_B, 
                 borderRadius=18, paddingTBLR=(0,0,0,0), margin=0, w=140, h=40,
                 fontFamily="Arial", fontSize=14, fontWeight="bold") 
    0;  MC.text(l="  ")
    0;  QtButton(handle="bof", label="UNLOCK UI\n(PERMANENTLY)", action=unlockUIPermanently,  
                 lineColor=CYAN_L, background=CYAN_B, 
                 borderRadius=18, paddingTBLR=(0,0,0,0), margin=0, w=140, h=40,
                 fontFamily="Arial", fontSize=14, fontWeight="bold") 
    0;  MC.setParent("..")

    0;MC.setParent("..")
    0;MC.setParent("..")

    0;EXCEPTIONS_COLUMNLAYOUT = MC.columnLayout(bgc=(.4,.3,.3))
    0;  QtText(label="SMOOTHING EXCEPTIONS", color=(240,220,220),paddingTBLR=(4, 0, 4, 0), margin=0, fontFamily="Arial", fontSize=18, fontWeight="Bold")
    0;  QtText(label="The \"APPLY\" and \"SAVE3DSMAXDATA\" commands will force the following exceptions:", 
               paddingTBLR=(0, 0, 4, 0), color=(220,160,160), fontFamily="Arial", fontSize=14, fontWeight="normal")
    0;  MC.setParent("..")

    0;EXCEPTIONITEMS_ROWLAYOUT = MC.rowColumnLayout(nc=2, cw=[(1, 20), (2, 520)], co=(1, "left", 0), cal=[(1,"left"), (2, "left")])
    pointer = OMUI.MQtUtil.findLayout(EXCEPTIONITEMS_ROWLAYOUT)      
    widget  = SHIBOKEN.wrapInstance(long(pointer), QTGUI.QWidget)
    widget.setStyleSheet("""font-size: 13px;""") 
    #0;  MC.text(l="", h=12)   
    0;  MC.text(l="   - ")
    0;  MC.text(l="<b>pr_fiy01</b>: <b>body</b> and <b>back</b> always 0-smoothed")
    0;  MC.text(l="   - ")
    0;  MC.text(l="<b>pr_sto01</b>:  everything always 1-smoothed")
    0;  MC.setParent("..")


    MC.formLayout(GRANULARITY_FORMLAYOUT, edit=True, 
                  attachForm=   [(TEXT_COLUMNLAYOUT, 'left', 0),
                                 (TEXT_COLUMNLAYOUT, 'top', 0),
                                 (TEXT_COLUMNLAYOUT, 'right', 0), 
                                 (OPERATIONS_ROWCOLUMNLAYOUT, 'left', 0),
                                 (OPERATIONS_ROWCOLUMNLAYOUT, 'right', 0),
                                 (CLOSE_SYMBOLBUTTON, 'top', 0),
                                 (CLOSE_SYMBOLBUTTON, 'right', 0), 
                                 (EXCEPTIONS_COLUMNLAYOUT, 'right', 0),
                                 (EXCEPTIONS_COLUMNLAYOUT, 'left', 0)],
                  attachControl=[(OPERATIONS_ROWCOLUMNLAYOUT, 'top', 0, TEXT_COLUMNLAYOUT), 
                                 (EXCEPTIONS_COLUMNLAYOUT, 'top', 20, OPERATIONS_ROWCOLUMNLAYOUT), 
                                 (EXCEPTIONITEMS_ROWLAYOUT, 'top', 0, EXCEPTIONS_COLUMNLAYOUT)])
    
    MC.showWindow("granularOptions_WIN")
    MC.window("granularOptions_WIN", edit=True, w=560, h=410)
    
    # sctipJob to reactivate the main UI when this window is closed
    MC.scriptJob (uiDeleted=["granularOptions_WIN", enableMainUI])

def closeGranularOptionsUI(*args):
    if MC.window("granularOptions_WIN", ex=1):
        MC.deleteUI("granularOptions_WIN")

    # REACTIVATE MAIN WINDOW
    MC.formLayout("GLOBAL_FORM", edit=True, enable=1)   


# THIS IS A CODING ABOMINATION... At the present time I'm not able to do it differently... 
def postApplyDump_manageNormalLights_callback(*args):
    global POSTAPPLYDUMP_MANAGENORMALLIGHTS_FLAG
    POSTAPPLYDUMP_MANAGENORMALLIGHTS_FLAG = MC.checkBox("postApplyDump_manageNormalLights_checkBox", query=True, value=True)

def postApplyDump_manageCOLOR_LIGHTLayers_callback(*args):
    global POSTAPPLYDUMP_MANAGECOLOR_LIGHTLAYERS_FLAG
    POSTAPPLYDUMP_MANAGECOLOR_LIGHTLAYERS_FLAG = MC.checkBox("postApplyDump_manageCOLOR_LIGHTLayers_checkBox", query=True, value=True)

def postApplyDump_manageShadowLights_callback(*args):
    global POSTAPPLYDUMP_MANAGESHADOWLIGHTS_FLAG
    POSTAPPLYDUMP_MANAGESHADOWLIGHTS_FLAG = MC.checkBox("postApplyDump_manageShadowLights_checkBox", query=True, value=True)

def postApplyDump_correctAlembicLightLinkerBug_callback(*args):
    global POSTAPPLYDUMP_CORRECTALEMBICLIGHTLINKERBUG_FLAG
    POSTAPPLYDUMP_CORRECTALEMBICLIGHTLINKERBUG_FLAG = MC.checkBox("postApplyDump_correctAlembicLightLinkerBug_checkBox", query=True, value=True)

def postApplyDump_correctAlembicVisibilityBug_callback(*args):
    global POSTAPPLYDUMP_CORRECTALEMBICVISIBILITYBUG_FLAG
    POSTAPPLYDUMP_CORRECTALEMBICVISIBILITYBUG_FLAG = MC.checkBox("postApplyDump_correctAlembicVisibilityBug_checkBox", query=True, value=True)

def postApplyDump_renderingMiscellanea_callback(*args):
    global POSTAPPLYDUMP_RENDERINGMISCELLANEA_FLAG
    POSTAPPLYDUMP_RENDERINGMISCELLANEA_FLAG = MC.checkBox("postApplyDump_renderingMiscellanea_checkBox", query=True, value=True)

def postApplyDump_writeGroupsShotgun_callback(*args):
    global POSTAPPLYDUMP_WRITEGROUPSHOTGUN_FLAG
    POSTAPPLYDUMP_WRITEGROUPSHOTGUN_FLAG = MC.checkBox("postApplyDump_writeGroupsShotgun_checkBox", query=True, value=True)

def postApplyDump_makeSSVisible_callback(*args):
    global POSTAPPLYDUMP_MAKESSVISIBLE_FLAG
    POSTAPPLYDUMP_MAKESSVISIBLE_FLAG = MC.checkBox("postApplyDump_makeSSVisible_checkBox", query=True, value=True)



#######################################################################################################

def updateDAGPath(DAGPath, newNamespace=""):
    # Input:   |namespace:label_1|namespace:label_2... |namespace:label_n
    # where "namespace" can be a nested namespace and each "label_i" has no ":"s    
    tempDAGPath = ""
    tokens = DAGPath.lstrip("|").split("|") # Remove the startTrailing "|"
    for token in tokens:
        i = token.rfind(":")
        if i != -1:
            # rebuild properly the dagpath:
            token = token[i+1:]
        tempDAGPath += "|" + newNamespace + (":" if newNamespace != "" else "") + token
    return tempDAGPath

def decomposeDAGPath(DAGPath, newNameSpace=""):
    # Return a list with the correct tokens, namespaced: INVERSED 
    # i.e. [0]=label  [1]=first parent   [2]=second parent...
    cleanDAGPath = updateDAGPath(DAGPath, newNameSpace)     
    DAGTokens = cleanDAGPath.lstrip("|").split("|")
    return DAGTokens[::-1] #[start:stop:step], to reverse the list

def smartObjExists(dumpName, type="DAG", namespaceContainer=""):
    """ DEBUG """
    0000; funcDebug()
    0000; printDebug("LOOKING FOR: " + dumpName + " (" + type + ")")
    0000; printDebug("namespace: " + namespaceContainer)

    # namespaceContainer=""        --> "preProd" mode
    # namespaceContainer="ch_shit" -->    "prod" mode

    """ RENDERING NODE EXCEPTIONS """
    # If the TAG is global, apply it to the existing global nodes
    ANOMALIES = ["miDefaultFramebuffer", 
                 "mentalrayGlobals",
                 "miDefaultOptions",
                 "defaultRenderGlobals", 
                 "defaultResolution",
                 "defaultRenderQuality"] 
    for anomaly in ANOMALIES:
        if anomaly in dumpName:
            # It was an override on a global rendering node; select the global one
            return dumpName
    

    #if namespaceContainer == "":
    if True: 
        #---------------------------------------------------------
        # PREPROD mode
        MC.namespace(set=':') # Go GLOBAL
        if type == "DAG":
            #----------
            # DAG node:            
            
            # [0]=label   [1]=firstParent   [2]=secondParent...
            decomposedDumpName = decomposeDAGPath(dumpName, newNameSpace=namespaceContainer)
            0000; printDebug("decomposedDumpName: ", decomposedDumpName)

            """
            MAYA DEFORMER SHAPES RENAMING PROBLEM....
            The dumped node was:      XXXXXShapeXXXX
            The receiver node can be:
                                      NAMESPACE:XXXXXShapeXXXXX
                                      XXXXXShapeDeformedXXXXX 
            """            
            
            firstTagsToTry = [decomposedDumpName[0]] # Usually there's no problem at all   
            if "Shape" in decomposedDumpName[0]:
                # ALEMBIC WILL USUALLY PRODUCE A NEW NAME: XXXXXXShapeDeformed... no namespace
                alternativeTag = updateDAGPath(decomposedDumpName[0], "") + "Deformed" # Remove namespace and add "Deformed"
                firstTagsToTry = [decomposedDumpName[0], alternativeTag]   
                0000; printDebug("Shape detected; firstTagsToTry: ", firstTagsToTry)

            # If working on a mesh node, we try the two possibilities
            for firstTagToTry in firstTagsToTry:
                0000; printDebug("Trying firstTag: " + firstTagToTry)
                decomposedDumpName[0] = firstTagToTry 
                partialSearchTag =""
                for i, dumpTag in enumerate(decomposedDumpName):
                    # progressive search pattern:
                    # "TAG|TAG|TAG" <--
                    partialSearchTag = dumpTag + ("|" + partialSearchTag if partialSearchTag != "" else "")
                    candidates = MC.ls(partialSearchTag, recursive=True)
                    if len(candidates) == 1:
                        0000; printDebug("MATCH FOUND: " + candidates[0])
                        return candidates[0]
            
            # if we got here, the node wasn't found or there was an ambiguity
            0000; printDebug("UNRESOLVED NODE!")
            return None    

        elif type == "DG":
            #-----------------------------------------
            # DG node (not DAG)
            # SHADERS, AUXILIARIS, MENTALRAYS, SHIT...
            cleanDumpName = dumpName[dumpName.rfind(".")+1:]
            # if in prodMode, look for a VERY SPECIFIC DG node
            namespacedCleanDumpName = (namespaceContainer + ":" if namespaceContainer != "" else "") + cleanDumpName
            candidates = MC.ls(namespacedCleanDumpName, recursive=True)
            if len(candidates) == 1:
                0000; printDebug("MATCH FOUND: " + candidates[0])
                return candidates[0]
            else:
                # NOT FOUND
                0000; printDebug("UNRESOLVED NODE!")
                return None

        elif type == "GENERIC":
            #----------------------------------------------------
            # hack to call "smartObjExists" for all type of nodes
            # (SAFE RECURSION)
            DAGCandidate = smartObjExists(dumpName, type="DAG", namespaceContainer=namespaceContainer)
            if DAGCandidate != None:
                # there's a DAG?
                return DAGCandidate
            else:
                # probably a DG?
                DGCandidate = smartObjExists(dumpName, type="DG", namespaceContainer=namespaceContainer)
                if DGCandidate != None:
                    return DGCandidate 
                else:
                    # if we get here, nothing was found!!!
                    return None       
     
        else:
            fatality("Ok, andiamo a mangiare una pizza che e meglio!!!")

    else:
        #---------------------------------------------------------
        # PROD mode
        pass

def setAttr(attr, value):
    """
    TRAP the MC. here with TYR\EXCEPT
    """
    if isinstance(value, basestring): 
        MC.setAttr(attr, value, type="string")
    elif value != None:
        MC.setAttr(attr, value)

def getAssetGroupIdString(assetName):
    # recover the groupId string of an asset ("00", "01", "02", ...)
    assetGroupId = None
    for groupId in COMBINED_ASSETS:
        if assetName in COMBINED_ASSETS[groupId]:
            assetGroupId = groupId
            break
    if assetGroupId == None:
        fatality("GROUP ID error")
     
    rawAssetGroupIdString = str(assetGroupId)
    assetGroupIdString = str(rawAssetGroupIdString) if len(str(rawAssetGroupIdString)) > 1 else "0" + str(rawAssetGroupIdString)
    return assetGroupIdString    

def loadDump(path, namespaceContainer=""):
    """ DEBUG """
    0000; funcDebug()
    0000; printDebug("path: " + path)
    0000; printDebug("namespace: " + namespaceContainer)

    #-----------------------------------------------------------------------------------
    # Load the '_REN.txt'
    f = None
    renderLayersDump = None
    try:
        f = open(path, "r")
        renderLayersDump = JSON.loads(f.read())
        printLog("RenderLayersDump loaded for '" + namespaceContainer +"'", "SUCCESS")
    except Exception as e:
        fatality ("Loading renderLayersDump for '" + namespaceContainer + "' FAILED!\n" + str(e))
    finally:
        if f != None:
            f.close()

    #-----------------------------------------------------------------------------------
    # "defaulRenderLayer"
    appendReport("APPLYING THE 'defaultRenderLayer' DUMP",  bars=True, barSymbol="-", newLines=0)

    MC.setAttr("defaultRenderLayer.renderable", False) 
    MC.editRenderLayerGlobals(currentRenderLayer="defaultRenderLayer")
    defaultRenderLayerData = renderLayersDump["layers"]["defaultRenderLayer"]
    renderLayersDump["layers"].pop("defaultRenderLayer") # Remove from list

    # "defaultRenderLayer" has only (mesh)-transforms!!!
    for meshTransformTag in defaultRenderLayerData.keys():
        # FATALITY if it can't found unambiguously the corresponding node in scene
        sceneMeshTransform = smartObjExists(meshTransformTag, type="DAG", namespaceContainer=namespaceContainer)
        if sceneMeshTransform == None:
            fatality("Can't resolve the dumpTag:\n\n - " + meshTransformTag + "\n\n(missing node, hierarchy problems or duplicates)")        
        0000; printDebug("\n----------------------------------------------------------------\nTAG ASSOCIATION:")
        0000; printDebug(meshTransformTag + "      ==>      " + sceneMeshTransform + "\n")

        appendReport("APPLYING DUMP INFO '" + meshTransformTag + "' TO SCENE OBJECT '" + sceneMeshTransform + "'")
        #appendReport("Working on '" + sceneMeshTransform + "'")
        mesh = MC.listRelatives(sceneMeshTransform, shapes=True, noIntermediate=True, path=True)[0] # AVOID INTERMEDIATES + return A VALID NAME ()DAG PATH REQUIRED)
        meshData = defaultRenderLayerData[meshTransformTag]
        
        #---------------------------------------------------------------------------------
        # Assign base shader
        shaderTag = meshData.pop("BASESHADER")

        # There can be ONLY a "lambert1" (even namespaced) in the scene
        # Thus, the tag "XXXX:lambert1" must be associated to "lambert1", disregarding the namespace confinement rule
        if shaderTag[shaderTag.rfind(":")+1:] == "lambert1":
            sceneShader = "lambert1"
        else:    
            sceneShader = smartObjExists(shaderTag, type="DG", namespaceContainer=namespaceContainer)
        
        if sceneShader != None:
            shadingEngines = MC.listConnections(sceneShader + ".outColor", destination=True, source=False, type="shadingEngine")
            if shadingEngines != None:
                if len(shadingEngines) == 1:
                    0000; printDebug("Applying shader " + sceneShader + "(" + shadingEngines[0]+ ") to mesh " + mesh)
                    MC.sets(mesh, edit=True, forceElement=shadingEngines[0])
                    appendReport("[OK] Base shader applied '" + sceneShader + "'")
                else: 
                    if sceneShader == "lambert1":
                        # The "lambert1" is an ecception: it's connected to the particle shadingEngine too
                        MC.sets(mesh, edit=True, forceElement="initialShadingGroup")
                        appendReport("[OK] 'lambert1' applied")
                    else:
                        fatality("The shader:\n" + sceneShader + "\nhas more than one shadingEngine: CAN'T CHOOSE!", culprits=[sceneShader])
            else: 
                fatality("The shader:\n" + sceneShader + "\nhas NO shadingEngine", culprits=[sceneShader])
        else:
            fatality("Can't find shader <b>" + shaderTag + "</b> for mesh <b>" + sceneMeshTransform + "</b> <br>iIt was dumped, but missing here!", culprits=[sceneMeshTransform], title="\"_REN\" ERROR")

        #---------------------------------------------------------------------------------
        # Attributes
        for attr in meshData:
            attrFullname = mesh+ "." + attr
            if MC.attributeQuery(attr, node=mesh, exists=True) and MC.getAttr(attrFullname, settable=True):
                setAttr(attrFullname, meshData[attr])
                appendReport("[OK] Base attribute applied '" + getShortDAGPath(mesh) + "." + attr + "'")
            else:
                fatality("The dumped attribute:\n" + attrFullName + "\ndoesn't exist or it's already connected in mesh:\n" + mesh, culprits=[mesh], title="\"_REN ERROR\"")
        
        appendReport("")    

    
    #-----------------------------------------------------------------------------------
    # RenderLayers creation and overriding attributes
    extraLayersDump = renderLayersDump["layers"] 
    
    """ Generate a proper progressBar """
    numberOfTasks = 0
    for layer in extraLayersDump:
        numberOfTasks += len(extraLayersDump[layer])
    progressBarInitialize(numberOfTasks)

    for extraLayer in extraLayersDump.keys():
        
        # The extraLayers must have the correct namespace
        sceneExtraLayer = namespaceContainer + (":" if namespaceContainer != "" else "") + extraLayer
        
        extraLayerInfo = extraLayersDump[extraLayer]
        appendReport("CREATING EXTRA LAYER '" + sceneExtraLayer + "'", bars=True, barSymbol="-", newLines=0)
        


        """
        ==================================================================
        LAYER CREATION/ACTIVATION (or combine)
        ==================================================================
        """
        # get asset's groupId
        assetGroupIdString = getAssetGroupIdString(namespaceContainer)
 
        """
        print "-----------------------------"
        print "ASSET: ", namespaceContainer 
        print "GROUPID: ", assetGroupIdString
        print "LAYER: ", extraLayer
        print "-----------------------------"
        """

        if "COLOR_LIGHT" in extraLayer:
            # COLOR LIGHT LAYER: never merge, create a new layer, respect the proper namespace
            newLayer = MC.createRenderLayer(name=sceneExtraLayer, makeCurrent=True, empty=True)
        else:
            # it's a MERGED LAYER, named:
            # _03_LAYERNAME        
                
            mergedNewLayerName = "_" + assetGroupIdString + "_" + extraLayer
            if not MC.objExists(mergedNewLayerName):
                # it doesn't exist: create the merged layer
                newLayer = MC.createRenderLayer(name=mergedNewLayerName, makeCurrent=True, empty=True)
            else:
                # already created; just set it as active
                MC.editRenderLayerGlobals(currentRenderLayer=mergedNewLayerName)
                newLayer = mergedNewLayerName    




        for nodeTag in extraLayerInfo:

            """ TEEPEE FIX """
            if "pr_tdo01" in namespaceContainer and "subset_tipi" in nodeTag:
                # the infamous SS component; skip it
                teepeeDebugPrint("LAYER " + extraLayer + ", skipped: " + nodeTag + "(" + namespaceContainer + ")")
                continue
            """ TEEPEE FIX END """   

            # "smartObjExists" can detect if the override has to be done on a rendering node and act consequently
            sceneNode = smartObjExists(nodeTag, type="GENERIC", namespaceContainer=namespaceContainer)
            if sceneNode != None:
                appendReport("APPLYING DUMP INFO '" + nodeTag + "' TO SCENE NODE '" + sceneNode + "'")
                nodeInfo = extraLayerInfo[nodeTag]
                #-----------------------------------------------------------
                # membership
                if "LAYERMEMBERSHIP" in nodeInfo.keys():
                    """
                    Only a transform can have this flag; put it in the layer... BUT:  
                    To avoid parasitic membership of lights and cameras, apply ONLY membership of MESH TRANSFORMS
                    """
                    meshChildren = MC.listRelatives(sceneNode, children=True, type="mesh")
                    if meshChildren != None:
                        # it's a transform with a valid mesh... membership possible 
                        MC.editRenderLayerMembers(newLayer, sceneNode, noRecurse=True)
                        appendReport("[OK] Layer membership")
                    nodeInfo.pop("LAYERMEMBERSHIP")
                #-----------------------------------------------------------
                # shader    
                if "OVERRIDESHADER" in nodeInfo.keys():
                    shaderTag =  nodeInfo["OVERRIDESHADER"]
                    sceneShader = smartObjExists(shaderTag, type="DG", namespaceContainer=namespaceContainer)
                    if sceneShader != None:
                        shadingEngines = MC.listConnections(sceneShader + ".outColor", destination=True, source=False, type="shadingEngine")
                        if shadingEngines != None and len(shadingEngines) == 1:
                            mesh = MC.listRelatives(sceneNode, shapes=True, noIntermediate=True, path=True)[0] # Again, we have ambiguity on names
                            MC.sets(mesh, edit=True, forceElement=shadingEngines[0])
                            appendReport("[OK] Shader override '" + sceneShader + "'")
                        else:
                            fatality("Bad/missing shading engine for shader:\n" + sceneShader, culprits=[mesh, sceneShader])
                    else:
                        print newLayer
                        print nodeTag
                        print sceneNode
                        fatality("MISSING SHADER\n\nThe shader:\n  -  " + shaderTag + 
                                 "\nwas dumped as override of mesh:\n  -  " + nodeTag + 
                                 "\nfor renderLayer: \n  -  " + extraLayer + 
                                 "\nbut MISSING here!", culprits=[sceneNode], title="[LOAD DUMP ERROR]") 
                    nodeInfo.pop("OVERRIDESHADER")
                #-----------------------------------------------------------
                # attribute overrides
                for attr in nodeInfo.keys():
                    attrFullname = sceneNode + "." + attr
                    MC.editRenderLayerAdjustment(attrFullname) #now what follow will be an override on the active render layer 
                    setAttr(attrFullname, nodeInfo[attr]) 
                    appendReport("[OK] Attribute override '" + getShortDAGPath(sceneNode) + "." + attr + "'")
            else:
                fatality("The following dump tag can't be resolved:\n" + nodeTag)

            appendReport("")
            progressBarIncrement()

        # End of construction for this layer
        appendReport("\n\n")
    
    # End of layer construction   
    appendReport("")  
    progressBarHide()

def applyPresetToSelection(assetNamespace="", chosenPreset=""):
    """ DEBUG """
    0000; funcDebug()

    # Move to defaultRenderLayer
    MC.editRenderLayerGlobals(currentRenderLayer="defaultRenderLayer")
    MC.refresh()

    if assetNamespace == "": 
        # Called from UI
        selection = MC.ls(sl=True)[0]
        assetNamespace = getNamespace(selection)
        printLog("\nAPPLYING LOCALLY AMBIENT PRESET")
           
    # If you can call this function, the button is active and something namespaced is selected


    # ASSETS_DATA = {assetNamespace: [assetID, RENPath, AMBPath, [amb1, amb2, ..., ambk]]}
    AMBPath = ASSETS_DATA[assetNamespace][2]
    f = None
    ambientsPreset = None
    try:
        f = open(AMBPath, "r")
        ambientsPreset = JSON.loads(f.read())
    except Exception as e:
        fatality("Unable to load:\n" + AMBPath + "\n\nReason:\n" + str(e))
    finally:
        if f != None:
            f.close()

    # global or specifi preset apply?
    if chosenPreset == "":
        # applying global pseset
        chosenPreset = MC.optionMenu("selectionPresets_optionMenu", query=True, value=True)
    
    0000; printDebug("namespace: " + assetNamespace)
    0000; printDebug("_AMB file: " + AMBPath)
    0000; printDebug("preset:    " + chosenPreset)
    0000; printDebug("presetted attributes: ")
    
    if chosenPreset not in ambientsPreset:
        # the asset has not the required ambient; the caller will detect a false
        return False 

    for attribute in ambientsPreset[chosenPreset]:
        namespacedAttribute = assetNamespace + ":" + attribute
        node = namespacedAttribute[:namespacedAttribute.find(".")]
        0000; printDebug(" - " + namespacedAttribute)
        value = ambientsPreset[chosenPreset][attribute]
        value[:] = [x/255.0 for x in value] # They were scaled...
        if MC.objExists(node): 
            try:
                MC.setAttr(namespacedAttribute, value[0], value[1], value[2])
            except:
                fatality("Can't apply the preset; the following attribute is locked/missing:\n - " + namespacedAttribute)    
        else:
            fatality("Can't apply the preset <b>" + chosenPreset + "</b> to the asset <b>" + assetNamespace + \
                     "</b>!<br>The node <b>" + node[node.find(":")+1:] + "</b> was dumped in the '_AMB', but missing here!", title="AMBIENT ERROR")

    # if we arrive here, it succeeded
    printLog("Preset '" + chosenPreset + "' applied to asset '" + assetNamespace + "'", "SUCCESS")

    return True        
 
def applyGlobalPreset(*args):
    presetsTable = {"DAY":        "DAY",
                    "TWILIGHT":   "TWI", 
                    "DAWN":       "DAW",
                    "NIGHT":      "NIG",
                    "FX":         "FX",
                    "FIRELIGHT":  "FIR",
                    "UNDERWATER": "UWT"}

    # Move to defaultRenderLayer
    MC.editRenderLayerGlobals(currentRenderLayer="defaultRenderLayer")
    MC.refresh()

    chosenGlobalPreset = presetsTable[MC.optionMenu("chosenGlobalPreset_optionMenu", query=True, value=True)]
    assetsWithoutPreset =[]
    
    operationsDone = 0

    printLog("\nAPPLYING GLOBALLY AMBIENT PRESET")
    # ASSETS_DATA = {assetNamespace: [assetID, RENPath, AMBPath, [amb1, amb2, ..., ambk]]}
    progressBarInitialize(numberOfTasks=len(ASSETS_DATA))
    for assetNamespace in ASSETS_DATA:
        if ASSETS_DATA[assetNamespace][0] == None or ("ch_" not in assetNamespace and "pr_" not in assetNamespace):
            # UNKNOWN or not CH/PR: skip
            continue

        if ASSETS_DATA[assetNamespace][2] == None:
            printLog("The asset '" + assetNamespace + "' has not a '_AMB'!", "WARNING")
            assetsWithoutPreset.append(assetNamespace + " [missing _AMB]")
            continue

        0000; printDebug("\n---------------------------------------------------\nAPPLYING PRESET '" + chosenGlobalPreset + "' TO ASSET '" + assetNamespace + "'")

        result = applyPresetToSelection(assetNamespace=assetNamespace, chosenPreset=chosenGlobalPreset)
        operationsDone += 1

        if result == False:
            # this asset has not the required ambient preset
            printLog("The asset '" + assetNamespace + "' has not a '" + chosenGlobalPreset + "' preset!", "WARNING")
            assetsWithoutPreset.append(assetNamespace)
        
        progressBarIncrement()
        MC.refresh()
        #appendReport("WORKING ON ASSET '" + assetNamespace + "' (YAKARI ID: " + ASSETS_DATA[assetNamespace][0] + ")", bars=True, barSymbol="=", newLines=0)
    progressBarHide()

    if len(assetsWithoutPreset) > 0:
        # List the asset without ambient
        missingAmbientWarning(assetsWithoutPreset)
    
    if operationsDone == 0:
        printLog("No valid mesh detected!", "NULL")






#-------------------------------------------------------------------
# "POST APPLY DUMP" procedures    
def postApplyDump_manageNormalLights(*args):
    printLog("\nMANAGING NORMAL LIGHTS")
    MC.editRenderLayerGlobals(currentRenderLayer="defaultRenderLayer")
    # Import the .ma file "NORMAL_LIGHTS_PATH"
    if MC.objExists("NORMAL_lights"):
        MC.delete("NORMAL_lights")

    try:
        MC.file(NORMAL_LIGHTS_PATH, i=True, type="mayaAscii", ignoreVersion=True, mergeNamespacesOnClash=False)
    except:
        fatality("Can't import normal lights!!!")
    
    printLog("Normal lights imported!", "SUCCESS")
    
    # NEW VERSION "GROUPED"
    #
    # Manage each group as it were a single asset; note that if an asset has not a NORMAL layer, even if it's 
    # grouped, it won't be here...
    # 
    # The dictionary COMBINED_ASSETS holds the asset grouping
    
    # ACCEPT 
    for groupId in COMBINED_ASSETS:
        groupIdString = str(groupId) if len(str(groupId)) > 1 else "0" + str(groupId)
        tag = "_" + groupIdString + "_NORMAL" # e.g. "_03_NORMAL"

        sceneLayers = MC.ls(type="renderLayer") 
        for layer in sceneLayers:
            # Accepted name: _03_NORMAL*
            if tag in layer:
                try:
                    MC.editRenderLayerMembers(layer, "NORMAL_lights", noRecurse=True)
                except:
                    fatality("Can't assign normalLights to the combined layer:\n  -  " + layer)
                printLog("Shared normalLights with '" + layer + "'", "OK")        
    
    """
    for groupId in COMBINED_ASSETS:
        groupIdString = str(groupId) if len(str(groupId)) > 1 else "0" + str(groupId)
        groupedNormalLayer = "_" + groupIdString + "_NORMAL" # e.g. "_03_NORMAL"
        if MC.objExists(groupedNormalLayer):
            try:
                MC.editRenderLayerMembers(groupedNormalLayer, "NORMAL_lights", noRecurse=True)
            except:
                fatality("Can't assign normalLights to the combined layer:\n  -  " + groupedNormalLayer)
            printLog("Shared normalLights with '" + groupedNormalLayer + "'", "OK")        
    sceneLayers = MC.ls(type="renderLayer") 
    """

    """
    # OLD VERSION
    #
    #
    for assetNamespace in ASSETS_DATA:
        if ASSETS_DATA[assetNamespace][0] == None:
            # UNKNOWN: skip
            continue
        if MC.objExists(assetNamespace + ":NORMAL"):
            # NORMAL layer can be absent; just continue
            try:
                MC.editRenderLayerMembers(assetNamespace + ":NORMAL", "NORMAL_lights", noRecurse=True)
            except:
                fatality("Can't assign normalLights to layer:\n  -  " + assetNamespace + ":NORMAL")
            printLog("Shared normalLights with '" + assetNamespace + ":NORMAL'", "OK")
    """

def postApplyDump_manageCOLOR_LIGHTLayers(*args):
    """
    NEW VERSION
     - For each asset, add ONLY meshes of other assets of the same group!
     - Keep the same namespace
     - If it's an "atomic" asset, nothing will be done
    """

    # Remove shader, then import it again
    if MC.objExists("matteNoAlpha_COLOR_LIGHT"):
        MC.delete("matteNoAlpha_COLOR_LIGHT")
    if MC.objExists("matteNoAlpha_COLOR_LIGHT_SG"):
        MC.delete("matteNoAlpha_COLOR_LIGHT_SG")
    
    try:
        MC.file(MATTE_NO_ALPHA_COLOR_LIGHT_PATH, i=True, type="mayaAscii", ignoreVersion=True, mergeNamespacesOnClash=False)
    except:
        fatality("Can't import 'matteNoAlpha' shader!!!")
    
    printLog("\nMANAGING 'COLOR_LIGHT' LAYERS")
    printLog("'matteNoAlpha' shader imported!", "SUCCESS")

    # YAKARI assets
    validAssets = [asset for asset in ASSETS_DATA if ASSETS_DATA[asset][0] != None]

    """ TEEPEES FIX """
    charPropAssets = {asset for asset in validAssets if asset.startswith(("ch", "pr")) and "pr_tdo02" not in asset} # "pr_tdo02" is a full-fledged SS (with bad TAG)
    subsetAssets   = {asset for asset in validAssets if asset.startswith("ss") or "pr_tdo02" in asset}              # "pr_tdo02" is a full-fledged SS (with bad TAG)
    """ TEEPEES FIX END """
    
    # Old version (no teepees!)
    # charPropAssets = {asset for asset in validAssets if asset.startswith(("ch", "pr"))}
    # subsetAssets   = {asset for asset in validAssets if asset.startswith("ss")}
    
 
    
    # mesh tags to be ignored
    excludedMeshes = ["shdw_", 
                      "shdws_", 
                      "col_", 
                      "C_"]

    progressBarInitialize(numberOfTasks=len(charPropAssets))

    for asset in charPropAssets:
        printDebug("\nWORKING ON " + asset)

        # Activate on mode "override" the proper renderLayer if possible
        colorLightLayer = asset + ":COLOR_LIGHT"
        if not MC.objExists(colorLightLayer):
            fatality("The following asset has no COLOR_LIGHT layer:\n  -  " + asset)
        MC.editRenderLayerGlobals(currentRenderLayer=colorLightLayer, useCurrent=True, enableAutoAdjustments=True)

        # For every other asset OF THE SAME GROUP, list the valid meshes and put them in the correct layer with shader override    
        # (don't forget to cycle over the SSs... but only for "MATTE_")



        """ TEEPEE FIX """
        if "pr_tdo01" in asset:
            # but for the hybrid teepee, it has to...
            extraAssetsToIterate = (charPropAssets | subsetAssets)
            teepeeDebugPrint("Working on " + asset) 
        else:                
            # Usually, an asset will not interact with itself
            extraAssetsToIterate = (charPropAssets | subsetAssets) - {asset}     
        """ TEEPEE FIX END """



        for extraCharPropSSAsset in extraAssetsToIterate:
            printDebug("  FROM " + extraCharPropSSAsset)
            
            # Mask only on assets of the same group (NOTE THAT SS AND THE HYBRID "pr_tdo01" ARE EXCEPTION: they don't have a group)
            if extraCharPropSSAsset not in subsetAssets and "pr_tdo01" not in extraCharPropSSAsset and "pr_tdo02" not in extraCharPropSSAsset:
                # it's not an SS neither "pr_tdo01" or "pr_tdo02"... so work on it only if it belongs to the group
                if getGroupFromAsset(extraCharPropSSAsset) != getGroupFromAsset(asset):
                    # Different groups: skip!
                    continue

            # Get all the mesh belonging to an asset
            meshTransforms = [transform for transform in MC.ls(extraCharPropSSAsset + ":*", type="transform")]  
            """ you can't work directly on namespaces and meshes!!!
                ALEMBIC destroys mesh namespaces... """    
            # Detect the meshTransforms
            for meshTransform in meshTransforms:
                meshes = MC.listRelatives(meshTransform, shapes=True, noIntermediate=True, fullPath=True) or []
                if len(meshes) > 0 and MC.nodeType(meshes[0]) == "mesh":
                    mesh = meshes[0]
                    isValid = True
                    for tag in excludedMeshes:
                        if tag in getParent(mesh):
                            isValid = False
                            break
                    if isValid:
                        printDebug(mesh)

                        # membership and override shader

                        if "ss_" in extraCharPropSSAsset and "MATTE_" not in meshTransform:
                            # for SS, only the mesh "MATTE_" has to be managed
                            continue
                        
                        """ TEEPEE FIX """
                        # If we get here, "pr_tdo01" had not the group check...
                        # Reenable it for all its meshes except "subset_tipi"
                        if "pr_tdo01" in extraCharPropSSAsset: 
                            if getGroupFromAsset(extraCharPropSSAsset) != getGroupFromAsset(asset):
                                # Different group
                                if "subset_tipi" in meshTransform:
                                    # Different groups but it's its SS component... valid 
                                    teepeeDebugPrint("Asset: " + asset + ", extra: " + extraCharPropSSAsset + "... mesh: " + meshTransform) 
                                    teepeeDebugPrint("it's a SS part, but different grouping: MASK IT!\n")
                                    pass
                                else:
                                    # Different groups and standard PR mesh; skip it
                                    teepeeDebugPrint("Asset: " + asset + ", extra: " + extraCharPropSSAsset + "... mesh: " + meshTransform) 
                                    teepeeDebugPrint("it's a PR part, but different grouping: SKIPPED!\n")
                                    continue    

                        if asset == extraCharPropSSAsset and "subset_tipi" not in meshTransform:
                            # Asset merging with himself!
                            # Obly exception: pr_tdo01... and only "subset_tipi" has to be moved
                            teepeeDebugPrint("Asset: " + asset + ", extra: " + extraCharPropSSAsset + "... mesh: " + meshTransform) 
                            teepeeDebugPrint("Only 'subsetTipi' needs some work: SKIPPED!\n")
                            continue

                        """ APPARENTLY, everything is fine for 'pr_tdo02', grouping has been disabled and all its meshes are SS """
                        """ TEEPEE FIX END """

                        MC.editRenderLayerMembers(colorLightLayer, getParent(mesh), noRecurse=True)
                        MC.sets(mesh, edit=True, forceElement="matteNoAlpha_COLOR_LIGHT_SG") # We are on the proper layer, so this is an override

        progressBarIncrement() 
        printLog("RenderLayer 'COLOR_LIGHT' built for asset '" + asset + "'", "SUCCESS")

    progressBarHide()

    MC.editRenderLayerGlobals(currentRenderLayer="defaultRenderLayer")

def __OLDVERSION_postApplyDump_manageCOLOR_LIGHTLayers(*args):
    # Remove shader, then import it again
    if MC.objExists("matteNoAlpha_COLOR_LIGHT"):
        MC.delete("matteNoAlpha_COLOR_LIGHT")
    if MC.objExists("matteNoAlpha_COLOR_LIGHT_SG"):
        MC.delete("matteNoAlpha_COLOR_LIGHT_SG")
    
    try:
        MC.file(MATTE_NO_ALPHA_COLOR_LIGHT_PATH, i=True, type="mayaAscii", ignoreVersion=True, mergeNamespacesOnClash=False)
    except:
        fatality("Can't import 'matteNoAlpha' shader!!!")
    
    printLog("\nMANAGING 'COLOR_LIGHT' LAYERS")
    printLog("'matteNoAlpha' shader imported!", "SUCCESS")

    # YAKARI assets
    validAssets = [asset for asset in ASSETS_DATA if ASSETS_DATA[asset][0] != None]
    charPropAssets = {asset for asset in validAssets if asset[:2] in ["ch", "pr"]}
    subsetAssets   = {asset for asset in validAssets if asset[:2] == "ss"}
    
    # mesh tags to be ignored
    excludedMeshes = ["shdw_", 
                      "shdws_", 
                      "col_", 
                      "C_"]

    progressBarInitialize(numberOfTasks=len(charPropAssets))

    for asset in charPropAssets:
        printDebug("\nWORKING ON " + asset)

        # Activate on mode "override" the proper renderLayer if possible
        colorLightLayer =asset + ":COLOR_LIGHT"
        if not MC.objExists(colorLightLayer):
            fatality("The following asset has no COLOR_LIGHT layer:\n  -  " + asset)
        MC.editRenderLayerGlobals(currentRenderLayer=colorLightLayer, useCurrent=True, enableAutoAdjustments=True)

        # For every other asset, list the valid meshes and put them in the correct layer with shader override    

        # (don't forget to cycle over the SSs... but only for "MATTE_")
        for extraCharPropSSAsset in (charPropAssets | subsetAssets) - {asset}:
            printDebug("  FROM " + extraCharPropSSAsset)

            # Get all the mesh belonging to an asset
            meshTransforms = [transform for transform in MC.ls(extraCharPropSSAsset + ":*", type="transform")]  
            """ you can't work directly on namespaces and meshes!!!
                ALEMBIC destroys mesh namespaces... """    
            # detect the meshTransforms
            for meshTransform in meshTransforms:
                meshes = MC.listRelatives(meshTransform, shapes=True, noIntermediate=True, fullPath=True) or []
                if len(meshes) > 0 and MC.nodeType(meshes[0]) == "mesh":
                    mesh = meshes[0]
                    isValid = True
                    for tag in excludedMeshes:
                        if tag in getParent(mesh):
                            isValid = False
                            break
                    if isValid:
                        printDebug(mesh)

                        # membership and override shader

                        if "ss_" in extraCharPropSSAsset and "MATTE_" not in meshTransform:
                            # for SS, only the mesh "MATTE_" has to be managed
                            continue

                        MC.editRenderLayerMembers(colorLightLayer, getParent(mesh), noRecurse=True)
                        MC.sets(mesh, edit=True, forceElement="matteNoAlpha_COLOR_LIGHT_SG") # We are on the proper layer, so this is an override

        progressBarIncrement() 
        printLog("RenderLayer 'COLOR_LIGHT' built for asset '" + asset + "'", "SUCCESS")

    progressBarHide()

    MC.editRenderLayerGlobals(currentRenderLayer="defaultRenderLayer")

def postApplyDump_manageShadowLights(*args):
    # For each asset, move the SHADOWS_lights (if any) to the corresponding "GROUPED" SHADOWS layer
    
    #======================================================================================
    # NEW VERSION "GROUPED"
    #======================================================================================
    printLog("\nMANAGING SHADOW LIGHTS")
    for assetNamespace in ASSETS_DATA:
        if ASSETS_DATA[assetNamespace][0] == None:
            # UNKNOWN: skip
            continue

        # Look for a lightTransform with the tag "*SHADOW*"
        """ 
        Starting "RELATIVE LOOKUP MODE" 
        WARNING: when activated you're stuck in a "namespaceless" world, renderLayers included
                 if the script fails, the relative mode will be still active and it's potentially fatal!
                 TRAP ALWAYS this part with a TRY EXCEPT FINALLY
        """
        try:
            MC.namespace(setNamespace=assetNamespace)
            MC.namespace(relativeNames=True) # <== now, the namespace is IMPLICIT!
            printDebug("\nWORKING ON " + assetNamespace)
            for item in MC.ls("*SHADOWS*", type="transform", long=True):
                shapes = MC.listRelatives(item, shapes=True)
                if shapes != None and len(shapes) == 1 and "Light" in MC.nodeType(shapes[0]): # again, LAZY PYTHON
                    # Found a lightTransform
                    printDebug(item)
                    printDebug(shapes[0])
                    # recover the groupId
                    groupId = getAssetGroupIdString(assetNamespace)
                    groupIdString = str(groupId) if len(str(groupId)) > 1 else "0" + str(groupId)

                    try:
                        # UGLY AS SHIT...
                        # go back in "absolute lookup" mode
                        MC.namespace(setNamespace=":") # back to absolute lookup
                        MC.namespace(relativeNames=False)

                        # realive lookup gives this shit "|:__CHARS__|rig_group|SHADOWS_lights|head_locator|SHADOWS_lights_head"
                        # remove the ":" and add the namespace (relative lookup wasn't a ggod idea... youre stuck in a namespace:)
                        item = "|" + item[2:]
                        item = updateDAGPath(item, newNamespace=assetNamespace)
                        item = item[item.find(":"):]

                        # relative lookUp is tricky... apparently, it modifies the strings 
                        # (defining this name in relativeMode gives an automatic namespace)
                        shadowLayer = "_" + groupIdString + "_SHADOWS"

                        """
                        print "----------------------"
                        print "LAYER ", shadowLayer
                        print "ITEM ", item
                        print "----------------------"
                        """
                        MC.editRenderLayerMembers(shadowLayer, item, noRecurse=True)
                        
                        # reactivate "relative lookup" mode
                        MC.namespace(setNamespace=assetNamespace)
                        MC.namespace(relativeNames=True)

                    except Exception as error:
                        fatality("Can't assign shadowLight:\n  -  " + item + "\nto layer:\n  -  " + shadowLayer + ":SHADOWS\nError: " + str(error))
                   
        except Exception as error:
            print str(error)
        finally:
            MC.namespace(setNamespace=":") # back to absolute lookup
            MC.namespace(relativeNames=False) 

        printLog("Moved 'shadowLights' for asset '" + assetNamespace + "'", "SUCCESS") 
        """ 
        Ending "RELATIVE LOOKUP MODE"
        """

    """
    #====================================================================================
    # OLD VERSION
    #====================================================================================    
    printLog("\nMANAGING SHADOW LIGHTS")
    for assetNamespace in ASSETS_DATA:
        if ASSETS_DATA[assetNamespace][0] == None:
            # UNKNOWN: skip
            continue

        if MC.objExists(assetNamespace + ":SHADOWS"):
            # Layer exists; now look for a lightTransform with the tag "*SHADOW*"
            try:
                MC.namespace(setNamespace=assetNamespace)
                MC.namespace(relativeNames=True) # <== now, the namespace is IMPLICIT!
                printDebug("\nWORKING ON " + assetNamespace)
                for item in MC.ls("*SHADOWS*", type="transform", long=True):
                    shapes = MC.listRelatives(item, shapes=True)
                    if shapes != None and len(shapes) == 1 and "Light" in MC.nodeType(shapes[0]): # again, LAZY PYTHON
                        # Found a lightTransform
                        printDebug(item)
                        printDebug(shapes[0])
                        try:
                            MC.editRenderLayerMembers("SHADOWS", item, noRecurse=True)
                        except Exception as error:
                            fatality("Can't assign shadowLight:\n  -  " + item + "\nto layer:\n  -  " + assetNamespace + ":SHADOWS\nError: " + str(error))
                       
            except Exception as error:
                print str(error)
            finally:
                MC.namespace(setNamespace=":") # back to absolute lookup
                MC.namespace(relativeNames=False) 

            printLog("Moved 'shadowLights' for asset '" + assetNamespace + "'", "SUCCESS") 
    """   

def postApplyDump_correctAlembicLightLinkerBug(*args):
    """ DEBUG """
    0000;funcDebug()
    
    printLog("\nCORRECTING EXOCORTEX LIGHTLINKING BUGS")
    lightLinkerNode = "lightLinker1"
    compounds = [(".link",         "light",              "object"), 
                 (".ignore",       "lightIgnored",       "objectIgnored"), 
                 (".shadowLink",   "shadowLight",        "shadowObject"), 
                 (".shadowIgnore", "shadowLightIgnored", "shadowObjectIgnored")]
 
    solved = 0

    for pair in compounds:
        # get the list of valid indices of the compound (I guess not sparse...)
        validIndices = MC.getAttr(lightLinkerNode + pair[0], multiIndices=True) # if empty returns None, not []
        if validIndices != None: 
            for index in validIndices:
                0000;printDebug("")
                0000;printDebug("PLUG " + pair[0] + ": working on index " + str(index))

                lightAttribute = lightLinkerNode + pair[0] + "[" + str(index) + "]." + pair[1]
                objectAttribute = lightLinkerNode + pair[0] + "[" + str(index) + "]." + pair[2]
                objectPlugs = MC.listConnections(objectAttribute, source=True, d=False, shapes=True, type="mesh")
                lightPlugs  = MC.listConnections(lightAttribute, source=True, d=False, shapes=True)
                if objectPlugs != None: # if empty returns None, not []
                    object = objectPlugs[0]
                    lightShape = lightPlugs[0]
                    0000;printDebug("intermediate mesh = " + object)  
                    0000;printDebug("light to relink   = " + lightShape)

                    if MC.getAttr(object + ".intermediateObject") == 1:
                        # the lightLinker1 is connected to the intermediary shape, not the main mesh  
                        # The intermediate mesh is in reality a DAG; hence it must have a parent, 
                        # corresponding to the validMesh; the intermediate flag hides the mesh in the outliner
                        parent = MC.listRelatives(object, parent=True, fullPath=True) 
                        validMesh = MC.listRelatives(parent, shapes=True, noIntermediate=True, fullPath=True)[0]
                        
                        # DO IT WITH THE COMMAND ENGINE
                        # unlink the intermediate shape
                        MC.disconnectAttr(lightShape + ".message", lightAttribute)
                        MC.disconnectAttr(object + ".message", objectAttribute) 
                        # relink the proper mesh
                        0000;printDebug("true mesh         = " + validMesh)

                        solved = solved + 1
                        MC.lightlink(object=validMesh, light=lightShape) 
    printDebug("SOLVED" + str(solved))
    if solved == 0:
        printLog("Nothing to do!", "NULL")
    else:
        printLog(str(solved) + " Exocortex bugs corrected!", "OK")   

def postApplyDump_correctAlembicVisibilityBug(*args):
    # Some objects are hidden in the rei; alembic will make a connection; break it and make visible
    printLog("\nCORRECTING EXOCORTEX VISIBILITY BUG")

    solved = 0

    transformCandidates = set(MC.ls("*shdws*", type="transform", recursive=True)) | set(MC.ls("*shdw*", type="transform", recursive=True))
    for transform in transformCandidates:
        sourcePlugs = MC.listConnections(transform + ".visibility",source=True) or []
        if len(sourcePlugs) > 0:
            if MC.nodeType(sourcePlugs[0]) == "ExocortexAlembicXform":
                MC.disconnectAttr(sourcePlugs[0] + ".outVisibility", transform + ".visibility")
                MC.setAttr(transform + ".visibility", 1)
                printLog("Mesh '" + transform + "' is now visible!", "SUCCESS")
                solved += 1

    if solved == 0:
        printLog("Nothing to do!", "NULL")            

def postApplyDump_renderingMiscellanea(*args):
    """ 
    OPEN MANUALLY THE RENDER SETTINGS WINDOWS 
    (some MEL commands are loaded ONLY when the interface is shown at least once... argh) 
    """
    MM.eval("unifiedRenderGlobalsWindow")
    MM.eval('toggleWindowVisibility unifiedRenderGlobalsWindow')    


    printLog ("\nMISCELLANEA")
    #---------------------------------------------------------
    # FILE NAME PREFIX and RENDERABLE CAMERA
    #---------------------------------------------------------

    # don't be so punitive: if the name is not right, just do what you can!!!
    isValidSceneName = False
    sceneName = MC.file(q=True, sceneName=True, shortName=True)

    episode, shot = getProperEpisodeShotName()
    if episode is not None and shot is not None:
        isValidSceneName = True
    







    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # CAMERA PROJ: erase all cameras, reimport the proper alembic
    """
    print "================" 
    print "CAMERA PROJ HACK"
    print "================"
    """
    if isValidSceneName:
        cameraType = getShotCameraType_shotGun(episode, "sh" + shot) # naming convention ("YKR405", "sh012") 
        print "[SHOT TYPE] ", cameraType
        if cameraType == "PROJ": #"""<== JUST TO TEST, switch to PROJ"""
            # case PROJ: 
            # - delete all cameras and "__CAMERA__" hierarchy;
            # - alembicImport the proper file
            # - check the proper naming and namespace 
            
            cams = [node for node in MC.ls(type="camera") if node not in ["frontShape", "perspShape", "sideShape", "topShape"]]
            if len(cams) > 0:
                try:
                    MC.delete(cams)    
                except:
                    # Probably referenced, just skip it
                    pass

            cameraHolder = MC.ls("*__CAMERA__*") or []
            if len(cameraHolder) > 0:
                try:
                    MC.delete(cameraHolder)
                except:
                    # referenced???
                    pass
            
            printLog("All camera deleted!", "SUCCESS")

            #------------------------------------------------------------------------------
            # Import a new PROJ
            #------------------------------------------------------------------------------
            cacheFolder = "Y:/01_SAISON_4/09_EPISODES/04_Fabrication_3D/" + episode + "/sh" + shot + "/ani/maya/publish/"
            try: 
                candidates = [x for x in OS.listdir(cacheFolder) if "caches" in x]
            except:
                fatality("\nCan't find the folder :\n" + cacheFolder + "\nCan't proceed, sorry!", title="CAMERA CACHE ERROR")       

            mostRecent = None
            lowestNumericTag = -1
            for item in candidates:
                tokens = item.split("_")
                # detect the folder with name "caches_###" and get the "bigger"
                # (check if it's a number or not)
                try:
                    numericTag = int(tokens[1])
                    if len(tokens) == 2 and numericTag > lowestNumericTag:
                        mostRecent = item
                        lowestNumericTag = numericTag
                except:
                    # not relevant
                    pass    

            if mostRecent == None:
                fatality("\nCan't find a proper cache folder!\n(it should be named 'caches_###', with the biggest ###)\n\nCan't proceed, sorry!", title="CAMERA CACHE ERROR")       
            alembicPath = cacheFolder + mostRecent
            print "[CACHE FOLDER] " + alembicPath
            
            cameraAlembicCandidates = [x for x in OS.listdir(alembicPath) if ".abc" in x and "PROJ" in x] or []
            if len(cameraAlembicCandidates) == 1:
                cameraAlembicPath = alembicPath + "/" + cameraAlembicCandidates[0]
                print "[CAMERA CACHE] " + cameraAlembicPath
            else: 
                fatality("\nCan't load a proper .abc for the camera PROJ (inexistant or ambiguous) in the folder:\n" + alembicPath + "\n\nCan't proceed, sorry!", title="CAMERA CACHE ERROR")       

            # Now import the camera alembic
            exoCommand = "fileName=%s;"\
                         "normals=0;"\
                         "uvs=0;"\
                         "facesets=0;"\
                         "attachToExisting=0"% cameraAlembicPath
            try:
                MC.ExocortexAlembic_import(j=exoCommand)
            except Exception as exc:
                fatality("Can't open the alembic file:\n" + cameraAlembicPath)

            printLog("Camera PROJ alembic imported!", "SUCCESS")
                
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""







    #tokens = sceneName.split("_")
    #if len(tokens) >= 2 and "YKR" in tokens[0]:
    #   isValidSceneName = True

    
    # BAD: parasite the getCameraFromShotgun, to utilise it later
    cameraShapeHandle = None

    if isValidSceneName:
        # fileNamePrefix
        path = "Y:/01_SAISON_4/09_EPISODES/04_Fabrication_3D/" + episode + "/sh" + shot + "/rnd/<RenderLayer>/<RenderLayer>"
        MC.setAttr("defaultRenderGlobals.imageFilePrefix", path, type="string")
        printLog("Rendering imageFilePrefix set to:\n           " + cutInHalfString(path)[0] + "\n           " + cutInHalfString(path)[1], "OK")
        
        # renderableCamera
        renderableCameraTag = getShotCameraType_shotGun(episode, "sh" + shot) # naming convention ("YKR405", "sh012") 
        cameraShapes = MC.ls(type="camera")
        for cameraShape in cameraShapes:
            if renderableCameraTag in cameraShape:
                # the camera has the right tag: make it the only renderable!!!
                MC.setAttr(cameraShape + ".renderable", True)
                wrappedCamera = DGNode(cameraShape)
                printLog("Renderable camera set to '" + wrappedCamera.getParent(DAGPath=False) + "'", "OK")
                cameraShapeHandle = cameraShape
            else: 
                MC.setAttr(cameraShape + ".renderable", False)

        # Notify the UI that something has changed
        # (apparently, "updateMayaSoftwareCameraControl" is loaded only when the corresponding interface is active
        #  exactly once it failed... if you call this, at this point everything should be fine)
        MM.eval("updateMayaSoftwareCameraControl;")

    #---------------------------------------------------------
    # FRAMERANGE
    #---------------------------------------------------------
    minFrame = MC.playbackOptions(query=True, animationStartTime=True)
    maxFrame = MC.playbackOptions(query=True, animationEndTime=True)
    MC.setAttr("defaultRenderGlobals.startFrame", minFrame)
    MC.setAttr("defaultRenderGlobals.endFrame",   maxFrame)
    printLog("Rendering frameRange set to [" + str(int(minFrame)) + ", " + str(int(maxFrame)) + "]", "OK")
    
    # Notify the UI that something has changed
    # (this can fail if the frame/animation ext is single frame. The following command doesn't exist)
    #  but usually, it has been already set...)
    MM.eval("updateMayaSoftwareTargetFilePreview;")


    #---------------------------------------------------------
    # DECONNECT IMAGEPLANE
    #---------------------------------------------------------
    imagePlanes = MC.ls(type="imagePlane")
    solved = 0
    for imagePlane in imagePlanes:
        outputPlugs= MC.listConnections(imagePlane + ".message", s=False, d=True, plugs=True, shapes=True) or []
        for outputPlug in outputPlugs:
            if MC.nodeType(outputPlug) == "camera":
                MC.disconnectAttr(imagePlane + ".message", outputPlug)
                wrappedCamera = DGNode(outputPlug[:outputPlug.rfind(".")])
                solved += 1
                printLog("Disconnected imagePlane from camera\n           " +  wrappedCamera.getParent(DAGPath=False), "OK")
    if solved == 0:
        printLog("No imagePlane to disconnect!", "NULL")    
    
    #---------------------------------------------------------
    # IMAGE SIZE
    #---------------------------------------------------------  
    # Official PNG binary structure (@ means byte) (http://www.w3.org/TR/PNG/#5PNG-file-signature)
    #
    #    signature     IHDR (image header)                other chunks...
    #    @@@@@@@@      @@@@ @@@@ @@@@ @@@@ @ @ @ @ @      @@@@@...
    #                   len code    w    h ....
    #
    # So, the first 8 + 4 + 4 = 16 bytes are useless for us.
    
    if isValidSceneName: 
        if renderableCameraTag == "PROJ":
            # PROJ mode: set the camera opening to the size and ration of the BG
            # build the PNGs path
            PNGsPath = r"Y:\01_SAISON_4\09_EPISODES\03_Fabrication_2D" + "\\" + episode + "\\" + episode + "_" + shot
            print "TEST", PNGsPath
            if OS.path.exists(PNGsPath):
                # look for exactly one PNG matching "*_BG.png" (if not present, abort)
                BGPlates = [x for x in OS.listdir(PNGsPath) if x.find("BG.png") != -1]
                if len(BGPlates) == 0:
                   fatality("Can't find a PNG '*_BG.png' in the folder '" + PNGsPath + "' (inexistant). Render size undefined!")
                
                possibleBGs = [x for x in BGPlates if "01_BG" in x]
                if len(possibleBGs) > 0:
                    chosenBGPlate = possibleBGs[0]
                else:
                    chosenBGPlate = BGPlates[0]    

                BGPlatePath = PNGsPath + "\\" + chosenBGPlate
                try:
                    PNGHandle = open(BGPlatePath, "rb")  # Open .png in binary format
                    irrelevantBytes = PNGHandle.read(16)  # Read the first useless 16 bytes
                    IHDRBytes = PNGHandle.read(8)  # IHDR bytes
                except Exception as e:
                    fatality(str(e))    
                finally:
                    PNGHandle.close()     

                # The method struct.unpack(format, byteSequence) takes lowLevel data (bytes) and
                # rebuild highLevel data (numbers, strings) by following the chosen format; 
                # here it recovers two unsigned ints (the "!2I" format) from 4+4 bytes
                (width, height) = STRUCT.unpack("!2I", IHDRBytes)

                MC.setAttr("defaultResolution.width", width)
                MC.setAttr("defaultResolution.height", height)
                ratio = width/float(height)
                MC.setAttr("defaultResolution.deviceAspectRatio", ratio)
                
                # if vertically stretched, fitResulotionGate = Vertical
                if ratio < 1:
                    MC.setAttr(cameraShapeHandle + ".filmFit", 2)
                    printLog("Vertically stretched aperture: set ResGate to 'vertical' (PROJ camera mode)", "OK")


                MC.setAttr("defaultResolution.pixelAspect", 1)
                printLog("Rendering [width, height, ratio] set to [" + str(int(width)) + ", " + str(int(height)) + ", " + str(ratio) + "] (PROJ camera mode)", "OK")
                
                # Notify the UI that something has changed
                MM.eval("mayaSoftwareDeviceAspectRatioChanged;")
                MM.eval("updateMayaSoftwareResolution;")

            else:
                fatality("Can't find the folder '" + PNGsPath + "' containing the PNGs!")        

        elif renderableCameraTag == "HD":  
            # HD mode: set camera opening to fullHD
            MC.setAttr("defaultResolution.width", 1920)
            MC.setAttr("defaultResolution.height", 1080)
            ratio = 1920.0/1080.0
            MC.setAttr("defaultResolution.deviceAspectRatio", ratio)
            MC.setAttr("defaultResolution.pixelAspect", 1)
            printLog("Rendering camera set to [HD1080] (HD camera mode)", "OK")

            # Notify the UI that something has changed
            MM.eval("mayaSoftwareDeviceAspectRatioChanged;")
            MM.eval("updateMayaSoftwareResolution;")
      
def postApplyDump_writeGroupsShotgun(*args):
    # Write the COMBINE_ASSETS data on shotGun
    combineAssetLayer_writeCallback()

def postApplyDump_makeSSVisible(*args):
    # Make all SS meshes visible (disconnect if necessary)
    # ASSETS_DATA has the list of namespaces (each namespace beginning with "ss_" is automatically valid)
    SSAssets = [asset for asset in ASSETS_DATA if asset.startswith("ss_")]
    for asset in SSAssets:
        try:
            DAGsToCheck = [node for node in MC.ls(asset + "*:*", long=True) if MC.nodeType(node) in ["transform", "mesh"]]
            for dag in DAGsToCheck:
                # First, disconnect if necessary:
                inputPlugs = MC.listConnections(dag + ".visibility", plugs=True) or []
                for inputPlug in inputPlugs:
                    MC.disconnectAttr(inputPlug, dag + ".visibility")
                # Then, unlock and set to 1
                MC.setAttr(dag + ".visibility", lock=False)
                MC.setAttr(dag + ".visibility", 1)
                printLog("The SS \"" + dag + "\" is now visible!", "SUCCESS")
        except Exception as exc:
            printLog("Can't make the SS\"" + dag + "\" visible!\n" + str(exc))        













"""
==================================================================================================================================================
--------------------------------------------------------------------------------------------------------------------------------------------------
     _______. __    __    ______   .___________.  _______  __    __  .__   __. 
    /       ||  |  |  |  /  __  \  |           | /  _____||  |  |  | |  \ |  | 
   |   (----`|  |__|  | |  |  |  | `---|  |----`|  |  __  |  |  |  | |   \|  | 
    \   \    |   __   | |  |  |  |     |  |     |  | |_ | |  |  |  | |  . `  | 
.----)   |   |  |  |  | |  `--'  |     |  |     |  |__| | |  `--'  | |  |\   | 
|_______/    |__|  |__|  \______/      |__|      \______|  \______/  |__| \__| 
--------------------------------------------------------------------------------------------------------------------------------------------------
==================================================================================================================================================
"""
# naming convention ("YKR405", "sh012") 
# the handle to shotGun is the global SHOTGUN_HANDLE
PROJECT_ID = 66  # YAKARI ID





# "2 TAGS" version         
def getProperEpisodeShotName(*args): 
    """
    Returns: 
      YKR408_012_shit   --> ("YKR408", "012")
      YKR405_099_B_fuck --> ("YKR405", "099_B")
      YKR405_056B_die   --> ("YKR405", "056B")   
      (None, None) if the whole name is invalid!!!    
       
    Note:
      The splitting "YKR405_099C" --> ("YKR405", "099C") works fine!
      Just modify the code to manage the split "YKR499_999_C" --> ("YKR499", "999_C")
    """
      
    sceneName = MC.file(q=True, sceneName=True, shortName=True)
    
    # Remove the trailing ".ma" or ".mb"
    cleanSceneName = sceneName.split(".")[0] 
    tokens = cleanSceneName.split("_")
    
    episode, shot = None, None
    
    if len(tokens) >= 2 and tokens[0].startswith("YKR"):
        
        # Case "###@":
        if RE.match(r"^[0-9]{3}[A-Z]{1}$", tokens[1]):
            # - start from the left "^"
            # - match exactly 3 numbers "[0-9]{3}"
            # - look for an uppercase letter "[A-Z]{1}"
            # - don't go any further "$"
            episode = tokens[0]
            shot    = tokens[1]
            
        # Case "###":    
        elif RE.match(r"^[0-9]{3}$", tokens[1]):
            episode = tokens[0]
            shot    = tokens[1]
            # Check if the 3rd token (if any) is a single "@" (otherwise, ignore the extra tags):
            if len(tokens) >= 3:
                if RE.match(r"^[A-Z]{1}$", tokens[2]):
                    shot = shot + "_" + tokens[2]
    
    # When we get here, the triple has the proper values
    # (not explicit at all, but easy to maintain and shorter)     
    return (episode, shot)

def getShotCameraType_readCallback(*args):
    (episode, shotShortName) = getProperEpisodeShotName()
    print getShotCameraType_shotGun(episode, shotShortName)

def combineAssetLayer_writeCallback(*args):
    (episode, shotShortName) = getProperEpisodeShotName()
    shotShortName = "sh" + shotShortName

    #try:
    combineAssetLayer_shotGunWrite(episode, shotShortName, COMBINED_ASSETS)
    #except Exception as exc:
    #    fatality(message="Can't write the 'combinedAssets' data!\n" + str(exc), title="SHOTGUN_WRITE ERROR")        
    printLog("'combinedAssets' data written on ShotGun's database!","SUCCESS")

def combineAssetLayer_readCallback(*args):
    episode, shotShortName = getProperEpisodeShotName()
    shotShortName = "sh" + shotShortName

    combinedAssets = combineAssetLayer_shotGunRead(episode, shotShortName)      
    pprint(combinedAssets)

def getShotCameraType_shotGun(episode, shotShortName):
    # NOTE: shotShortName must be of the form "sh012"... not "012"

    episodeDict = SHOTGUN_HANDLE.find_one("CustomEntity01", [["project", "is", {"type": "Project", "id": PROJECT_ID}], ["code", "is", episode]], [])
    filters = [["project", "is", {"type": "Project", "id": PROJECT_ID}],
               ["sg_episode", "is", episodeDict],
               ["sg_shortname", "is", shotShortName]]
    cameraType = SHOTGUN_HANDLE.find_one("Shot", filters, ["sg_cam_type"])["sg_cam_type"]
    return cameraType 

def combineAssetLayer_shotGunWrite(episode, shotShortName, combinedAssets):
    # NOTE: shotShortName must be of the form "sh012"... not "012"

    episodeDict = SHOTGUN_HANDLE.find_one("CustomEntity01", [["project", "is", {"type": "Project", "id": PROJECT_ID}], ["code", "is", episode]], [])
    filters = [["project", "is", {"type": "Project", "id": PROJECT_ID}],
               ["sg_episode", "is", episodeDict],
               ["sg_shortname", "is", shotShortName]]

    # convert the dictionary in an one with "00", "01", "02", ... as keys
    elegantCombinedAssets = {}
    for key in combinedAssets:
        stringKey = ("0" + str(key)) if len(str(key)) == 1 else str(key)
        elegantCombinedAssets[stringKey] = combinedAssets[key]

    elegantCombinedAssetsString = JSON.dumps(elegantCombinedAssets, indent=2)
    data = {"sg_combine_asset_layer": elegantCombinedAssetsString} # "sg_combine_asset_layer" is the name of the new shotGun field
    
    # Before writing, check if it exists in shotGun
    handle = SHOTGUN_HANDLE.find_one("Shot", filters)
    if handle is not None and "id" in handle:
        SHOTGUN_HANDLE.update("Shot", handle["id"], data)
    else:
        # Should I be punitive?
        message = "Can't write the \"layer groups\" data in ShotGun!\nProbably still not \"published\"..."
        fatality(message, title="SHOTGUN WRITE ERROR")
        #printLog(message, "ERROR")
        #MC.warning(message)
    #SHOTGUN_HANDLE.update("Shot", SHOTGUN_HANDLE.find_one("Shot", filters)["id"], data)

def combineAssetLayer_shotGunRead(episode, shotShortName):
    # NOTE: shotShortName must be of the form "sh012"... not "012"

    episodeDict = SHOTGUN_HANDLE.find_one("CustomEntity01", [["project", "is", {"type": "Project", "id": PROJECT_ID}], ["code", "is", episode]], [])
    filters = [["project", "is", {"type": "Project", "id": PROJECT_ID}],
               ["sg_episode", "is", episodeDict],
               ["sg_shortname", "is", shotShortName]]
    # This one could be "None"
    combinedAssetsString = SHOTGUN_HANDLE.find_one("Shot", filters, ["sg_combine_asset_layer"])["sg_combine_asset_layer"]
    try:
        combinedAssets = JSON.loads(combinedAssetsString) 
    except Exception as exc:
        fatality(message="Can't read the 'combinedAssets' data!\n" + str(exc), title="SHOTGUN READ ERROR")       
    return combinedAssets














#======================================================================================================
#------------------------------------------------------------------------------------------------------
# "COMBINE GROUPS" EDITOR
#------------------------------------------------------------------------------------------------------
#======================================================================================================

"""
COMBINED_ASSETS = {0: ["fava", "minchia", "sborra1"], 
                   1: ["cazzo", "sborra", "cazzo1"], 
                   2: ["troia", "wow", "troia1"], 
                   7: ["minchia1", "wow1"], 
                   11:["aaa", "bbb", "ccc", "ddd"]
                  }

#AVAILABLE_GROUPS = sorted([0, 1, 2, 7, 8, 9, 10, 11])
"""


# It's a PARTITION of assets
COMBINED_ASSETS  = {}
AVAILABLE_GROUPS = []

# A local copy of data to prevent automatic update when working in the UI
COMBINED_ASSETS_LOCAL  = {}
AVAILABLE_GROUPS_LOCAL = []

def getGroupFromAsset(asset):
    group = None
    for groupKey in COMBINED_ASSETS:
        if asset in COMBINED_ASSETS[groupKey]:
            group = groupKey
            break
    if group is None:
        fatality("Sorry, can't find the group of asset '" + asset + "'!\nCan't proceed, sorry!")
    else:
        return group            

def initializeCOMBINED_DATA(*args):
    # ASSETS_DATA = {"ch_yakar_1":   ["ch_yakar", "path_REN.txt", "path_AMB.txt", ["FIR", "SHIT", "FUCK", "FX", COO"]],
    global COMBINED_ASSETS
    global AVAILABLE_GROUPS
    
    # Exceptional case: no ASSETS_DATA (e.g. new scene)
    if len(ASSETS_DATA) == 0:
        COMBINED_ASSETS = {}
        AVAILABLE_GROUPS = []
        return

    # erase all and remember: "Everything begins as son of a ZERO" 
    COMBINED_ASSETS.clear()
    COMBINED_ASSETS[0] = []
    AVAILABLE_GROUPS[:] = [0]

    # start from scratch
    """ This is a fine example of BADprocedural design... accessing data via ASSETS_DATA[fuck][0] is HORRID
        And adding a new field is a nightmare (you need to refactor everything)!
        ...
        Imagine having something like this:
        ASSETS_DATA["dioMerda"].tag
        ASSETS_DATA["dioMerda"].availableAmbients

        IT'S TIME TO MOVE TOWARDS "OOP" or "STRUCT" (when you need to...)
        NOTE:
         - sometimes you don't need the whole "polymorphism, inheritance" shit... just ENCAPSULATION
    """

    for asset in ASSETS_DATA:
        if ASSETS_DATA[asset][0] != None and "ss_" not in ASSETS_DATA[asset][0]:
            COMBINED_ASSETS[0].append(asset)

    copyGlobalToLocalCombinedData()    
 
def copyGlobalToLocalCombinedData(*args):
    # create a local deepCopy to work nonDestructively with the UI
    global COMBINED_ASSETS_LOCAL
    global AVAILABLE_GROUPS_LOCAL     
    COMBINED_ASSETS_LOCAL  = COPY.deepcopy(COMBINED_ASSETS) 
    AVAILABLE_GROUPS_LOCAL = COPY.deepcopy(AVAILABLE_GROUPS)

def copyLocalToGlobalCombinedData(*args):
    # copy local data to global when "apply"
    global COMBINED_ASSETS
    global AVAILABLE_GROUPS     
    COMBINED_ASSETS = COPY.deepcopy(COMBINED_ASSETS_LOCAL) 
    AVAILABLE_GROUPS = COPY.deepcopy(AVAILABLE_GROUPS_LOCAL)

"""
def synchroAvailableGroupWithPartition(*args):
    # AVAILABLE_GROUPS should always include COMBINED_ASSETS.keys()
    # (not really necessary, I think)
    global AVAILABLE_GROUPS
    for group in COMBINED_ASSETS:
        if group not in AVAILABLE_GROUPS:
            AVAILABLE_GROUPS.append(group)
    AVAILABLE_GROUPS = sorted(AVAILABLE_GROUPS)        
"""

def mainUIGroupButtonsEnable(enable):
    if enable:
        # just refresh the UI
        refreshAssetsList()        
    else:    
        # work directly on the treeview, agnostically
        treeViewItems = MC.treeView("TREEVIEW", q=True, children="")
        for item in treeViewItems:
            # imagine having a method:
            # treeViewObject.colorButton(5, color)... 
            MC.treeView("TREEVIEW", e=True, buttonTransparencyColor=(item, 5, .3, .3, .3))

def assetPartitionUI(*args):
    # Create a local copy of combineData
    copyGlobalToLocalCombinedData()
    
    # grey-out the fucking buttons in the main UI
    mainUIGroupButtonsEnable(False)

    (width, height) = (260, 414)
    if MC.window("manageCombineGroups_WIN", ex=1):
        MC.deleteUI("manageCombineGroups_WIN") 
    MC.window("manageCombineGroups_WIN", t="ASSETS PARTITION MANAGER", tlb=1, s=1, mb=0)
    MC.columnLayout()
    
    #synchroAvailableGroupWithPartition()

 
    MC.text(label="Available Groups... Left click on group to delete it")
    
    MC.rowLayout("fuckYou", nc=2)
    0;MC.symbolButton("addButton", image=ICONS_PATH + "add_icon.png", c=addGroup, ann=HTMLFormatter("ADD GROUP", ["Add a new group"]))
    0;MC.scrollLayout("AVAILABLE_GROUPS_ROWLAYOUT_HOLDER", w=220, h=38)
    0;  MC.rowLayout("AVAILABLE_GROUPS_ROWLAYOUT", nc=len(AVAILABLE_GROUPS_LOCAL))
    0;    MC.setParent("..")
    0;  MC.setParent("..")
    0;MC.setParent("..")
    
    MC.text("\nselect assets, the click on GROUP ICON to assign")
    
    MC.columnLayout(w=width)
    0;QtText(handle="coloredAssets_QTTEXT", label=" SCENE ASSET                                   grp", fontSize=13)
    #MC.frameLayout("coloredAssets_frameLayout", l="   SCENE ASSET                         GRP", bs="etchedIn", bgc=(.3,.3,.3), bv=True, mw=4, mh=4, w=width)
    0;MC.treeView("coloredAssetsTreeView", numberOfButtons=1, abr=True, arp=False, adr=False, h=SCENE_ASSET_TREELIST_HEIGHT, w=width)
    0;MC.setParent("..")     

    """
    MC.rowLayout(nc=3)
    0;MC.button(label="print", c=printDict)
    0;MC.button(label="SHOTGUN write", c=combineAssetLayer_writeCallback)
    0;MC.button(label="SHOTGUN read", c=combineAssetLayer_readCallback, bgc=(0, 1, .5))
    MC.setParent("..")
    """

    MC.rowLayout(nc=6)
    MC.text(l="", w=2)
    QtButton(handle="resetPartitionButton", label="RESET", action=resetAssetPartition,  
             lineColor=CYAN_L, 
             background=CYAN_B, 
             borderRadius=12, paddingTBLR=(0,0,0,0), margin=0, w=66, h=24,
             fontFamily="Arial", fontSize=14, fontWeight="bold", 
             annotation="")  
    MC.text(l="", w=2)
    QtButton(handle="optimizeButton", label="OPTIMIZE", action=optimizeTreeList,  
             lineColor=CYAN_L, 
             background=CYAN_B, 
             borderRadius=12, paddingTBLR=(0,0,0,0), margin=0, w=82, h=24,
             fontFamily="Arial", fontSize=14, fontWeight="bold", 
             annotation="")  
    MC.text(l="", w=14)
    QtButton(handle="closeButton", label="APPLY", action=applyAssetPartition,  
             lineColor=BLUE_L, 
             background=BLUE_B, 
             borderRadius=14, paddingTBLR=(0,0,0,0), margin=0, w=80, h=30,
             fontFamily="Arial", fontSize=18, fontWeight="bold", 
             annotation="")  
    MC.setParent("..")

    MC.showWindow("manageCombineGroups_WIN")
    MC.window("manageCombineGroups_WIN", edit=True, w=width+5, h=height)

    # Disable mainUI and activate scriptJob to reenable once closed
    MC.formLayout("GLOBAL_FORM", edit=True, enable=0)
    MC.scriptJob (uiDeleted=["manageCombineGroups_WIN", enableMainUI])

    # don't do this in the middle of aUI creation
    """ IT'S TIME TO MOVE TO QT... this shit is OBSOLETE!!!!!!!!!!!!!! """
    refreshAssetsPartitionInterface()

def applyAssetPartition(*args):
    optimizeTreeList()

    # copy the UI temporary data on the official one
    copyLocalToGlobalCombinedData()
    
    MC.deleteUI("manageCombineGroups_WIN")
    refreshAssetsList()

def resetAssetPartition(*args):
    global COMBINED_ASSETS_LOCAL
    global AVAILABLE_GROUPS_LOCAL
    
    # erase all and remember: "Everything begins as son of a ZERO" 
    COMBINED_ASSETS_LOCAL.clear()
    COMBINED_ASSETS_LOCAL[0] = []
    AVAILABLE_GROUPS_LOCAL[:] = [0]

    for asset in ASSETS_DATA:
        if ASSETS_DATA[asset][0] != None and "ss_" not in ASSETS_DATA[asset][0]:
            COMBINED_ASSETS_LOCAL[0].append(asset)

    refreshAssetsPartitionInterface()

def refreshAssetsPartitionInterface(*args):
    MC.treeView("coloredAssetsTreeView", e=True, removeAll=True)     

    numberOfItems = 0
    for group in sorted(COMBINED_ASSETS_LOCAL.keys()):
        for asset in COMBINED_ASSETS_LOCAL[group]:
            MC.treeView("coloredAssetsTreeView", e=True, addItem=(asset, ""))     
            MC.treeView("coloredAssetsTreeView", e=True, fn=(asset, "fixedWidthFont")) 
            MC.treeView("coloredAssetsTreeView", e=True, lbc=(asset, getDarkGroupIdColor(group)[0], getDarkGroupIdColor(group)[1], getDarkGroupIdColor(group)[2]))
            MC.treeView("coloredAssetsTreeView", e=True, tc=(asset,  getGroupIdColor(group)[0], getGroupIdColor(group)[1], getGroupIdColor(group)[2]))              
            MC.treeView("coloredAssetsTreeView", e=True, buttonTransparencyOverride=(asset, 1, True)) 
            MC.treeView("coloredAssetsTreeView", e=True, buttonTransparencyColor=(asset, 1, getGroupIdColor(group)[0], getGroupIdColor(group)[1], getGroupIdColor(group)[2]))
            MC.treeView("coloredAssetsTreeView", e=True, bti=(asset, 1, str(group)))
            numberOfItems += 1
    
    # Resize scrollLayout if necessary
    if len(AVAILABLE_GROUPS_LOCAL) > 8:
        MC.scrollLayout("AVAILABLE_GROUPS_ROWLAYOUT_HOLDER", edit=True, w=220, h=58)
    else: 
        MC.scrollLayout("AVAILABLE_GROUPS_ROWLAYOUT_HOLDER", edit=True, w=220, h=38)


    # Destroy the old Group list and rebuild
    MC.deleteUI("AVAILABLE_GROUPS_ROWLAYOUT")
    MC.rowLayout("AVAILABLE_GROUPS_ROWLAYOUT", p="AVAILABLE_GROUPS_ROWLAYOUT_HOLDER", nc=len(AVAILABLE_GROUPS_LOCAL))
    
    for group in AVAILABLE_GROUPS_LOCAL:
        if group == 0:
            ww = 28
            hh = 28
            br = 14
        else:
            ww = 24
            hh = 24
            br = 12 
        QtButton(handle="groupButton" + str(group), label=str(group), action=voidFunction,  
                 lineColor=(getGroupIdColor(group)[0]*255, getGroupIdColor(group)[1]*255, getGroupIdColor(group)[2]*255), 
                 background=(getDarkGroupIdColor(group)[0]*255, getDarkGroupIdColor(group)[1]*255, getDarkGroupIdColor(group)[2]*255), 
                 borderRadius=br, paddingTBLR=(0,0,0,0), margin=0, w=ww, h=hh,
                 fontFamily="Arial", fontSize=14, fontWeight="bold", 
                 annotation="")             

        # THE FOLLOWING WOULD FAIL MISERABLY... but functools.partial works magnificently:)
        # MC.button("groupButton" + str(group), edit=True, c=__name__ + ".groupButtonPressed(" + str(group) + ")", w=ww, h=hh)        
        MC.button("groupButton" + str(group), edit=True, c=partial(groupButtonPressed, index=group), w=ww, h=hh)

    0;  MC.setParent("..")
    
    # Scroll to the furthest right (when maya is idle!!!)
    #-----------------------------------------------------------------------------------------------------
    # (but when doing APPLY, the idle will come after window death... bad design, but just try/except it)
    # try:
    #     __name__.MC.scrollLayout("AVAILABLE_GROUPS_ROWLAYOUT_HOLDER", edit=True, scrollPage="right")
    # except:    
    #     pass
    MC.evalDeferred("try:\n    " + str(__name__) + ".MC.scrollLayout(\"AVAILABLE_GROUPS_ROWLAYOUT_HOLDER\", edit=True, scrollPage=\"right\")\nexcept:\n    pass")

    # When the vertical scrollBar is active, just shrink the header a bit
    if numberOfItems > TREELIST_SIZE:
        # scrollBar active: shrink it
        MC.text("coloredAssets_QTTEXT", edit=True, label=" SCENE ASSET                               grp")
    else:
        MC.text("coloredAssets_QTTEXT", edit=True, label=" SCENE ASSET                                   grp")



def voidFunction(*args):
    # you need to study better Qt... invalid "function" pass 
    pass

def printDict(*args):
    # stampamelo bene
    pprint(COMBINED_ASSETS_LOCAL)
    
def groupButtonPressed(shit=None, index=0):
    global COMBINED_ASSETS_LOCAL
    
    # don't modify a dictionary inside a self-loop... you're gonna miss something (go for a DEEPCOPY)
    newCombinedAssets = COPY.deepcopy(COMBINED_ASSETS_LOCAL) # dictionary deep copy
    
    selectedAssets = MC.treeView("coloredAssetsTreeView", query=True, si=True) or []

    for group in COMBINED_ASSETS_LOCAL:
        for asset in COMBINED_ASSETS_LOCAL[group]:
            if asset in selectedAssets and index != group:
                # move something only if you need to
                newCombinedAssets[group].remove(asset)
                if not index in newCombinedAssets.keys():
                    # if a foreign index, create 
                    newCombinedAssets[index] = []
                newCombinedAssets[index].append(asset)
    COMBINED_ASSETS_LOCAL = COPY.deepcopy(newCombinedAssets)
    refreshAssetsPartitionInterface()
    
def addGroup(*args):
    global AVAILABLE_GROUPS_LOCAL
    groupToAdd = max(AVAILABLE_GROUPS_LOCAL) + 1
    AVAILABLE_GROUPS_LOCAL.append(groupToAdd)
    refreshAssetsPartitionInterface()

def optimizeTreeList(*args):
    global COMBINED_ASSETS_LOCAL
    global AVAILABLE_GROUPS_LOCAL
    
    optimizedCombinedAssets = {}
    usedGroups = sorted([group for group in COMBINED_ASSETS_LOCAL if len(COMBINED_ASSETS_LOCAL[group]) > 0])
    for index in range(len(usedGroups)):
        optimizedCombinedAssets[index] = COPY.deepcopy(COMBINED_ASSETS_LOCAL[usedGroups[index]])

    COMBINED_ASSETS_LOCAL = COPY.deepcopy(optimizedCombinedAssets)
    AVAILABLE_GROUPS_LOCAL = sorted(COMBINED_ASSETS_LOCAL.keys())    
    refreshAssetsPartitionInterface()    




























#------------------------------------------------------------------------------------------------------
# CUSTOM LAYERS interface and callbacks
#------------------------------------------------------------------------------------------------------

# IT'S FUCKING RIDICULOUS! the shitty treeView doesn't allow me to get the status of the buttons... so I must go "global"

#CUSTOM_LAYERS = {"layerName" : ("type", addNewLight, {"obj1": [CAST, RECEIVE], ..., "objk": [CAST, RECEIVE]}), ....
CUSTOM_LAYERS = {}
#CUSTOM_LAYER_TREEVIEW[asset] = [0, 0] ...[CAST, RECEIVE]
ACTUAL_CUSTOM_LAYER_TREEVIEW = {}
ISVALIDNAME = False

def createCustomLayersUI(*args):
    if len(ASSETS_DATA) == 0:
        printLog(" No asset detected!", "NULL")
        return

    global ACTUAL_CUSTOM_LAYER_TREEVIEW
    
    # disable main UI
    MC.formLayout("GLOBAL_FORM", edit=True, enable=0)
    mainUIGroupButtonsEnable(False)


    ACTUAL_CUSTOM_LAYER_TREEVIEW = dict() # erase old stuff

    # create the UI for creating customizing render layers
    (width, height) = (300, 446)
    if MC.window("addCustomLayers_WIN", ex=1):
        MC.deleteUI("addCustomLayers_WIN") 
    MC.window("addCustomLayers_WIN", t="NEW CUSTOM LAYER", tlb=1, s=0, mb=0)
    MC.frameLayout("customLayers_frameLayout", l="ADD CUSTOM RENDER LAYER", bs="etchedIn", bgc=(.3,.3,.3), bv=True, mw=4, mh=4)

    0;  MC.rowLayout(nc=4, enable=1)
    0;    MC.text(l=" Type ")
    0;    MC.optionMenu("customLayerType_optionMenu", l="", changeCommand="pass")
    0;    MC.menuItem(l="CAST_SHDWS")
    0;    MC.menuItem(l="REFLECTION", enable=0)
    0;    MC.text(l="Suffix")
    0;    MC.textField("customLayerSuffix_textField", editable=True, tx="custom", enterCommand=customLayerSuffixChanged, aie=True, w=120)
    0;    MC.setParent("..")
    0;  MC.rowLayout(nc=2)
    0;    MC.text(l=" Layer name ")
    0;    MC.textField("customLayerName_textField", editable=False, tx="CAST_SHDWS_custom", w=180, bgc=(.23, .23, .23))
    0;    MC.setParent("..")
    0;  MC.text("customLayerTextLine", l="SCENE ASSET                                    CAST     RECEIVE")

    # This time, works on all assets known by YAKARI, "ch", "pr" and "ss"
    workableAssets = [asset for asset in ASSETS_DATA if ASSETS_DATA[asset][0] != None]
    
    0;  MC.treeView("customLayerTreeView", numberOfButtons=4, abr=True, sc=treeViewDoNothing, scc=treeViewDoNothing, h=SCENE_ASSET_TREELIST_HEIGHT)

    for asset in workableAssets:
        # create the dictionary item
        ACTUAL_CUSTOM_LAYER_TREEVIEW[asset] = [0, 0] # (unchecked, unchecked)

        MC.treeView("customLayerTreeView", e=True, addItem=(asset, ""))     
        MC.treeView("customLayerTreeView", e=True, fn=(asset, "fixedWidthFont"))
        MC.treeView("customLayerTreeView", e=True, lbc=(asset, .165,.165,.165))
        MC.treeView("customLayerTreeView", e=True, tc=(asset, .9,.9,.9))
        
        MC.treeView("customLayerTreeView", e=True, image=(asset, 1, ""))   
        MC.treeView("customLayerTreeView", e=True, buttonStyle=(asset, 1, "2StateButton"))  
        MC.treeView("customLayerTreeView", e=True, buttonState=(asset, 1, "buttonDown"))  
        MC.treeView("customLayerTreeView", e=True, pc=(1, customLayerTreeViewCastButtonPressed))
        MC.treeView("customLayerTreeView", e=True, buttonTransparencyOverride=(asset, 1, True)) 
        MC.treeView("customLayerTreeView", e=True, buttonTransparencyColor=(asset, 1, 0.1,0.1,0.1))

        MC.treeView("customLayerTreeView", e=True, image=(asset, 3, "")) 
        MC.treeView("customLayerTreeView", e=True, buttonStyle=(asset, 3, "2StateButton"))  
        MC.treeView("customLayerTreeView", e=True, buttonState=(asset, 3, "buttonDown"))  
        MC.treeView("customLayerTreeView", e=True, pc=(3, customLayerTreeViewReceiveButtonPressed))
        MC.treeView("customLayerTreeView", e=True, buttonTransparencyOverride=(asset, 3, True)) 
        MC.treeView("customLayerTreeView", e=True, buttonTransparencyColor=(asset, 3, 0.1,0.1,0.1)) 

        # hide the fakeButtons, needed to create a space between buttons
        MC.treeView("customLayerTreeView", e=True, buttonVisible=(asset, 2, False))
        MC.treeView("customLayerTreeView", e=True, buttonVisible=(asset, 4, False))


    0;  MC.rowLayout(nc=2)
    0;    MC.text(l="", w=176)
    QtButton(handle="addTemplate_QTBUTTON", label="add Template", action=addLayerTemplate,  
             lineColor=BLUE_L, background=BLUE_B, 
             borderRadius=14, paddingTBLR=(0,0,0,0), margin=0, w=110, h=30,
             fontFamily="Arial", fontSize=14, fontWeight="bold")    
    QtButtonEnable("addTemplate_QTBUTTON", False)
    0;    MC.setParent("..")
    0;  MC.setParent("..")
    MC.showWindow("addCustomLayers_WIN")
    MC.window("addCustomLayers_WIN", edit=True, w=width, h=height)

    # set the first available defaultName
    revertToAvailableDefaultName()
    # scriptJob to reEnable main UI on window closing
    # (apparently a scriptJob defined like this one, automatically dies when the window is closed...)
    MC.scriptJob (uiDeleted=["addCustomLayers_WIN", enableMainUI])

    if len(workableAssets) > TREELIST_SIZE:
        # scrollBar active: shrink it
        MC.text("customLayerTextLine", edit=True, label="SCENE ASSET                        CAST     RECEIVE")
    else:
        print "fuck"
        MC.text("customLayerTextLine", edit=True, label="SCENE ASSET                                    CAST     RECEIVE")

def refreshCustomLayersTree(*args):
    MC.treeView("CUSTOM_LAYERS_TREE", edit=True, removeAll=True)
    for item in CUSTOM_LAYERS:
        MC.treeView("CUSTOM_LAYERS_TREE", e=True, addItem=(item, ""))     
        MC.treeView("CUSTOM_LAYERS_TREE", e=True, fn=(item, "fixedWidthFont"))
        MC.treeView("CUSTOM_LAYERS_TREE", e=True, lbc=(item, .165,.165,.165))
        MC.treeView("CUSTOM_LAYERS_TREE", e=True, tc=(item, .9,.9,.9)) 

    if len(CUSTOM_LAYERS) > 0:
        MC.button("CREATE_CUSTOM_LAYERS_QTBUTTON", edit=True, enable=1)
        MC.symbolButton("DELETEALL_SYMBOLBUTTON", edit=True, enable=1)
    else:
        item = "None..."
        MC.treeView("CUSTOM_LAYERS_TREE", e=True, addItem=(item, ""))     
        MC.treeView("CUSTOM_LAYERS_TREE", e=True, fn=(item, "fixedWidthFont"))
        MC.treeView("CUSTOM_LAYERS_TREE", e=True, lbc=(item, .165,.165,.165))
        MC.treeView("CUSTOM_LAYERS_TREE", e=True, tc=(item, .9,.9,.9)) 
        
        MC.button("CREATE_CUSTOM_LAYERS_QTBUTTON", edit=True, enable=0)
        MC.symbolButton("DELETEALL_SYMBOLBUTTON", edit=True, enable=0)


def enableMainUI(*args):
    # Called via a scriptJob every time a secondary window is closed and the main UI need to be reactivated.
    # When the main UI is closed, a scriptJob closes all the secondary window and indirectly calls this 
    try:
        MC.formLayout("GLOBAL_FORM", edit=True, enable=True)
        refreshAssetsList()
    except:
        # Nothing to do, the main UI has been already closed 
        pass

def customLayerTreeViewCastButtonPressed(item, oldState):
    oldState = int(oldState)
    if oldState == 1:
        # from up to down
        changeLayerTreeViewButtonStatus(item, 1, 0)        
    else:
        # from down to up
        changeLayerTreeViewButtonStatus(item, 1, 1)   
        changeLayerTreeViewButtonStatus(item, 3, 0) # only one button can be active at time       
    manageAddTemplateButton()

def customLayerTreeViewReceiveButtonPressed(item, oldState):
    oldState = int(oldState)
    if oldState == 1:
        # from up to down
        changeLayerTreeViewButtonStatus(item, 3, 0)        
    else:
        # from down to up
        changeLayerTreeViewButtonStatus(item, 3, 1)   
        changeLayerTreeViewButtonStatus(item, 1, 0) # only one button can be active at time        
    manageAddTemplateButton()
  
def changeLayerTreeViewButtonStatus(item, button, state):
    global ACTUAL_CUSTOM_LAYER_TREEVIEW
    properIndex = 0 if button == 1 else 1 # button --> array:  1->0, 3->1
    ACTUAL_CUSTOM_LAYER_TREEVIEW[item][properIndex] = state

    stateString = {0: "buttonDown", 
                   1: "buttonUp"}
    icon        = {0: "", 
                   1: ICONS_PATH + "whiteCheck_icon.png"}
    MC.treeView("customLayerTreeView", edit=True, buttonState=(item, button, stateString[state]))  
    MC.treeView("customLayerTreeView", edit=True, image=(item, button, icon[state]))      

def manageAddTemplateButton(*args):
    # activate the button only if both columns ain't empty
    items =  MC.treeView("customLayerTreeView", query=True, children="") or[]
    castEmpty    = True
    receiveEmpty = True
    for item in items:
        if ACTUAL_CUSTOM_LAYER_TREEVIEW[item][0] == 1:
            castEmpty = False
        if ACTUAL_CUSTOM_LAYER_TREEVIEW[item][1] == 1:
            receiveEmpty = False    
    QtButtonEnable("addTemplate_QTBUTTON", (not castEmpty and not receiveEmpty) and ISVALIDNAME)

def customLayerSuffixChanged(*args):
    global ISVALIDNAME

    layerType   = MC.optionMenu("customLayerType_optionMenu", query=True, value=True)
    suffix = MC.textField("customLayerSuffix_textField", query=True, tx=True)
    potentialName = layerType + "_" + suffix   

    # check if the suggested name is valid for maya
    patternRE = RE.compile("([a-zA-Z]+)([a-zA-Z0-9_])*")
    result = patternRE.search(potentialName).group()
    if result != potentialName or suffix == "":
        printLog("The chosen name '" + potentialName + "' is invalid for Maya!\n Reverting to an available default name!", "ERROR")
        revertToAvailableDefaultName() 
        ISVALIDNAME=True
        manageAddTemplateButton()
    else:
        if MC.objExists(potentialName) or potentialName in CUSTOM_LAYERS:
            printLog("The chosen name '" + potentialName + "' is already used.\n Reverting to an available default name!", "ERROR")
            revertToAvailableDefaultName() 
            ISVALIDNAME=True
            manageAddTemplateButton()
        else:
            MC.textField("customLayerSuffix_textField", edit=True, tx=suffix)
            MC.textField("customLayerName_textField", edit=True, tx=potentialName)
            ISVALIDNAME=True
            manageAddTemplateButton()

def revertToAvailableDefaultName(*args):
    global ISVALIDNAME
    # reset the interface to defaul name: "LAYERTYPE_custom#" where # is the first index available
    layerType = MC.optionMenu("customLayerType_optionMenu", query=True, value=True)
    index = 0
    while True:
        indexString = str(index) if index != 0 else "" # avoid the ugly "custom0"
        possibleName = layerType + "_" + "custom" + indexString
        if not MC.objExists(possibleName) and not possibleName in CUSTOM_LAYERS:
            # name available
            MC.textField("customLayerSuffix_textField", edit=True, tx="custom" + indexString)
            MC.textField("customLayerName_textField", edit=True, tx=possibleName, w=180, bgc=(.23, .23, .23))
            ISVALIDNAME = True
            manageAddTemplateButton()
            break
        index += 1    

def addLayerTemplate(*args):
    #CUSTOM_LAYERS = {"layerName" : ["type", addNewLight, {"obj1": [CAST, RECEIVE], ..., "objk": [CAST, RECEIVE]}], ....
    #CUSTOM_LAYER_TREEVIEW[asset] = [0, 0] ...[CAST, RECEIVE]
    global CUSTOM_LAYERS

    customLayerName = MC.textField("customLayerName_textField", query=True, tx=True)
    addNewLightFlag = True
    layerType       = MC.optionMenu("customLayerType_optionMenu", query=True, value=True)

    CUSTOM_LAYERS[customLayerName] = [layerType, addNewLightFlag, ACTUAL_CUSTOM_LAYER_TREEVIEW]
    refreshCustomLayersTree()

    MC.deleteUI("addCustomLayers_WIN")

def deleteAllCustomLayers(*args):
    # delete all custom layer templates
    global CUSTOM_LAYERS

    if len(CUSTOM_LAYERS) == 0:
        printLog("No extra custom layer template to delete!", "NULL")
    else:
        CUSTOM_LAYERS = dict()
        printLog("All custom layer templates deleted!", "SUCCESS")

    refreshCustomLayersTree()

def printCustomLayers(*args):
    pprint(CUSTOM_LAYERS)

def deleteCustomLayer(*args):
    print "delete CUSTOM LAYER"

def editCustomLayer(*args):
    print "edit CUSTOM LAYER"




def createCustomLayers(*args):

    #=============================================================================
    # IMPORT SHADER (IF NOT PRESENT)
    #=============================================================================

    # import the shader of necessary    
    if not MC.objExists("receiveShadows_CAST_SHDWS_SG"):
        try:
            MC.file(RECEIVE_SHADOWS_CAST_SHDWS_PATH, i=True, type="mayaAscii", ignoreVersion=True, mergeNamespacesOnClash=False)
            printLog("")
            printLog("'receiveShadows_CAST_SHDWS' shader imported!", "SUCCESS")
        except:
            fatality("Can't import the following shader:\n  -  receiveShadows_CAST_SHDWS\n\nPlease check the path:\n  -  " + RECEIVE_SHADOWS_CAST_SHDWS_PATH, title="IMPORT ERROR")
   

    #=============================================================================
    # READY TO START
    #=============================================================================
    """ CUSTOM_LAYERS = {"layerName" : ("type", addNewLight, {"obj1": [CAST, RECEIVE], ..., "objk": [CAST, RECEIVE]}), .... """

    printLog("")
    printLog("CREATING CUSTOM RENDER LAYERS")


    # don't touch these
    excludedMeshes = ["shdw_", 
                      "shdws_", 
                      "col_", 
                      "C_", 
                      "COLOR_"]


    for layer in CUSTOM_LAYERS:
        #-------------------------------------------
        # IMPORT LIGHT (one for layer)
        #-------------------------------------------
        # remove the shitty "uiConfigurationScriptNode" and "sceneConfigurationScriptNode" to prevent import nameChash warnings    
        uselessScriptNodes = MC.ls("TMPRR*", type="script")
        if len(uselessScriptNodes) > 0:
            MC.delete(uselessScriptNodes)


        try:
            # import nodes with a prefix "TMPRR_" to avoid clashes
            MC.file(CAST_SHDWS_LIGHT_PATH, i=True, type="mayaAscii", ra=True, ignoreVersion=True, mergeNamespacesOnClash=False, rpr="TMPRR", pr=True, options="v=0;p=17;f=0")
        except:
            fatality("Can't import the following light:\n  -  CAST_SHDWS_ground\n\nPlease check the path:\n  -  " + CAST_SHDWS_LIGHT_PATH, title="IMPORT ERROR")
    

        # Again, delete imported parasites and residui
        uselessScriptNodes = MC.ls("TMPRR*", type="script")
        if len(uselessScriptNodes) > 0:
            MC.delete(uselessScriptNodes)
        if MC.objExists(layer + "_directionalLight"):
            MC.delete(layer + "_directionalLight")

        # Rename properly
        lightName = layer + "_directionalLight"
        MC.rename("TMPRR_CAST_SHDWS_ground", lightName)
 


        #-------------------------------------------
        # CREATE
        #-------------------------------------------
        # It shouldn't exist, but some desynchro could happen
        if MC.objExists(layer):
            MM.eval("renderLayerEditorDeleteLayer RenderLayerTab " + layer + ";") 

        # create layer, enable auto overrides and add light
        newLayer = MC.createRenderLayer(name=layer, makeCurrent=True, empty=True)
        MC.editRenderLayerGlobals(currentRenderLayer=newLayer, useCurrent=True, enableAutoAdjustments=True)
        MC.editRenderLayerMembers(newLayer, lightName, noRecurse=True)

        layerType      = CUSTOM_LAYERS[layer][0]
        # addNewLightTag = CUSTOM_LAYERS[layer][1] ... NOT RELEVANT ANYMORE
        assetsData     = CUSTOM_LAYERS[layer][2]

        for asset in assetsData:
            isCaster   = assetsData[asset][0]
            isReceiver = assetsData[asset][1]
            
            # if asset is not used, skip it!
            if not isCaster and not isReceiver:
                continue
            
            # Get all the mesh belonging to the asset
            meshTransforms = [transform for transform in MC.ls(asset + ":*", type="transform")]  
            
            # you can't work directly on namespaces and meshes!!!
            # ALEMBIC destroys mesh namespaces!!!

            # detect the meshTransforms
            progressBarInitialize(len(meshTransforms))

            for meshTransform in meshTransforms:
                meshes = MC.listRelatives(meshTransform, shapes=True, noIntermediate=True, fullPath=True) or []
                if len(meshes) > 0 and MC.nodeType(meshes[0]) == "mesh":
                    mesh = meshes[0]
                    isValid = True
                    for tag in excludedMeshes:
                        if tag in getParent(mesh):
                            isValid = False
                            break
                    if isValid:
                        # membership and override shader
                        MC.editRenderLayerMembers(newLayer, getParent(mesh), noRecurse=True)
                        

                        # now, work differently for CAST and RECEIVE
                        if isCaster:
                            MC.setAttr(mesh + ".primaryVisibility", 0)
                            MC.setAttr(mesh + ".castsShadows", 1)

                        if isReceiver:    
                            MC.setAttr(mesh + ".primaryVisibility", 1)
                            MC.setAttr(mesh + ".castsShadows", 0)
                            MC.setAttr(mesh + ".receiveShadows", 1)
                            MC.sets(mesh, edit=True, forceElement="receiveShadows_CAST_SHDWS_SG") # We are on the proper layer, so this is an override


                progressBarIncrement()
            progressBarHide()            

        printLog("New render layer '" + layer + "' created!", "SUCCESS")           

    # activate default layer
    MC.editRenderLayerGlobals(currentRenderLayer="defaultRenderLayer", useCurrent=True, enableAutoAdjustments=False)
    
    # clean the UI
    deleteAllCustomLayers()
    inViewMessage(message="Custom Layers created!", position="topLeft", time=2000, status="SUCCESS")

def createCastShadowsGroundLayer(*args):
    """
    if we are here, the button "CREATE" was active and there's at least some SS
    """
    #=============================================================================
    # IMPORT SHADER (IF NOT PRESENT)
    #=============================================================================

    # import the shader of necessary    
    if not MC.objExists("receiveShadows_CAST_SHDWS_SG"):
        try:
            MC.file(RECEIVE_SHADOWS_CAST_SHDWS_PATH, i=True, type="mayaAscii", ignoreVersion=True, mergeNamespacesOnClash=False)
            printLog("")
            printLog("'receiveShadows_CAST_SHDWS' shader imported!", "SUCCESS")
        except:
            fatality("Can't import the following shader:\n  -  receiveShadows_CAST_SHDWS\n\nPlease check the path:\n  -  " + RECEIVE_SHADOWS_CAST_SHDWS_PATH, title="IMPORT ERROR")
   

    #-------------------------------------------
    # IMPORT LIGHT 
    #-------------------------------------------
    # remove the shitty "uiConfigurationScriptNode" and "sceneConfigurationScriptNode" to prevent import nameChash warnings    
    uselessScriptNodes = MC.ls("TMPRR*", type="script")
    if len(uselessScriptNodes) > 0:
        MC.delete(uselessScriptNodes)

    try:
        # import nodes with a prefix "TMPRR_" to avoid clashes
        MC.file(CAST_SHDWS_LIGHT_PATH, i=True, type="mayaAscii", ra=True, ignoreVersion=True, mergeNamespacesOnClash=False, rpr="TMPRR", pr=True, options="v=0;p=17;f=0")
    except:
        fatality("Can't import the following light:\n  -  CAST_SHDWS_ground\n\nPlease check the path:\n  -  " + CAST_SHDWS_LIGHT_PATH, title="IMPORT ERROR")

    # Again, delete imported parasites and residui
    uselessScriptNodes = MC.ls("TMPRR*", type="script")
    if len(uselessScriptNodes) > 0:
        MC.delete(uselessScriptNodes)
    if MC.objExists("CAST_SHDWS_GROUND_directionalLight"):
        MC.delete("CAST_SHDWS_GROUND_directionalLight")

    # Rename properly
    MC.rename("TMPRR_CAST_SHDWS_ground", "CAST_SHDWS_GROUND_directionalLight")    




    #-------------------------------------------
    # CREATE
    #-------------------------------------------
    # YAKARI assets, this time all known ch, pr and ss
    validAssets = [asset for asset in ASSETS_DATA if ASSETS_DATA[asset][0] != None and asset[:2] in ["ch", "pr", "ss"]]
    
    # mesh tags to be ignored
    excludedMeshesForCHPR = ["shdw_", 
                             "shdws_", 
                             "col_", 
                             "C_"]

    excludedMeshesForSS   = ["COLOR_", 
                             "MATTE_"]


    printLog("")
    printLog("CREATING 'CAST_SHDWS_GROUND'")
    progressBarInitialize(numberOfTasks=len(validAssets))

    # delete the old one (if any)
    if MC.objExists("CAST_SHDWS_GROUND"):
        MM.eval("renderLayerEditorDeleteLayer RenderLayerTab CAST_SHDWS_GROUND;") 

    newLayer = MC.createRenderLayer(name="CAST_SHDWS_GROUND", makeCurrent=True, empty=True)
    MC.editRenderLayerGlobals(currentRenderLayer=newLayer, useCurrent=True, enableAutoAdjustments=True)

    # membership of the light
    MC.editRenderLayerMembers(newLayer, "CAST_SHDWS_GROUND_directionalLight", noRecurse=True)

    for asset in validAssets:
            assetTag= asset[:2] # ch, pr or ss
            meshTransforms = [transform for transform in MC.ls(asset + ":*", type="transform")]  

            # detect the meshTransforms
            progressBarInitialize(len(meshTransforms))

            for meshTransform in meshTransforms:
                meshes = MC.listRelatives(meshTransform, shapes=True, noIntermediate=True, fullPath=True) or []
                if len(meshes) > 0 and MC.nodeType(meshes[0]) == "mesh":
                    # atrocious... but this is the real mesh:)
                    mesh = meshes[0]

                    if assetTag in ["ch", "pr"]:
                        #CASTER
                        isValid = True
                        for anomaly in excludedMeshesForCHPR:
                            if anomaly in getParent(mesh):
                                isValid = False
                                break
                        if isValid:
                            MC.setAttr(mesh + ".primaryVisibility", 0)
                            MC.setAttr(mesh + ".castsShadows", 1)
                            MC.editRenderLayerMembers(newLayer, getParent(mesh), noRecurse=True)
                    
                    if assetTag == "ss":
                        # RECEIVER
                        isValid = True
                        for anomaly in excludedMeshesForSS:
                            if anomaly in getParent(mesh):
                                isValid = False
                                break        
                        if isValid:                        
                            MC.setAttr(mesh + ".primaryVisibility", 1)
                            MC.setAttr(mesh + ".castsShadows", 0)
                            MC.setAttr(mesh + ".receiveShadows", 1)
                            MC.sets(mesh, edit=True, forceElement="receiveShadows_CAST_SHDWS_SG") # We are on the proper layer, so this is an override
                            MC.editRenderLayerMembers(newLayer, getParent(mesh), noRecurse=True)


                progressBarIncrement()
            progressBarHide()            

    # deactivate autoOverriding
    MC.editRenderLayerGlobals(currentRenderLayer="defaultRenderLayer", useCurrent=True, enableAutoAdjustments=False)

    printLog("'CAST_SHDWS_GROUND' created!", "SUCCESS")  
    inViewMessage(message="'CAST_SHDWS_GROUND' created!", position="topLeft", time=2000, status="SUCCESS") 





#-------------------------------------------------------------------
# RENDERING SMOOTHING
def applyRenderingSmoothGlobally(*args):
    printLog("\nAPPLYING RENDER SMOOTH GLOBALLY")

    smoothLevel = int(MC.optionMenu("smoothLevel_optionMenu", query=True, value=True))
    meshes = MC.ls(type="mesh", noIntermediate=True, long=True) or [] # not really necessary here; LS returns not None, but []
    progressBarInitialize(numberOfTasks=len(meshes))

    for mesh in meshes:
        applyRenderingSmoothToMesh(mesh, smoothLevel)
        progressBarIncrement()
    progressBarHide()    

    if len(meshes) == 0:
        printLog("No valid mesh found!", "NULL")
    else:
        printLog("'RenderDivisionLevel' globally set to " + str(smoothLevel), "SUCCESS")

def applyRenderingSmoothToSelection(*args):
    printLog("\nAPPLYING RENDER SMOOTH TO SELECTION")

    smoothLevel = int(MC.optionMenu("smoothLevel_optionMenu", query=True, value=True))
    selection = MC.ls(sl=True, type="transform", long=True) 
    progressBarInitialize(numberOfTasks=len(selection))

    objectsDone = 0
    
    for transform in selection:
        handle = DGNode(transform)
        meshes = handle.getMeshChildren(DAGPath=True)
        if len(meshes) == 1:
            applyRenderingSmoothToMesh(meshes[0], smoothLevel)
            objectsDone +=1
            if MC.nodeType(meshes[0]) == "mesh":
                parent = MC.listRelatives(meshes[0], parent=True)[0]
        progressBarIncrement()
    progressBarHide()  

    if objectsDone == 0:
        printLog("No valid meshTransform selected!", "NULL")

def applyRenderingSmoothToMesh(mesh, smoothLevel):
    """ 
    EXCEPTIONS: 
       "pr_fiy01":  "body" and "back" always 0-smoothed
       "pr_sto01":  everything always 1-smoothed 
    """

    # NEVER trust the name of a shape (remember the problem with reference and deformers)
    parent = MC.listRelatives(mesh, parent=True, fullPath=True)[0]
    parentLastTag = (parent.split("|"))[-1]

    temp = parentLastTag.split(":")
    if len(temp) > 1:
        # There's a namespace
        parentNamespace = temp[0] 
        parentShortName = temp[1]

        if "pr_fiy01" in parentNamespace:
            if "body" in parentShortName or "back" in parentShortName:
                smoothLevel = 0 
                #printLog ("Mesh '" + parentShortName+ "' of '" + parentNamespace + "' will be smoothed to 0!", "NULL")
        
        if "pr_sto01" in parentNamespace:
            # every mesh of this asset must be always smoothed to 1
            smoothLevel = 1 
            #printLog ("Mesh '" + parentShortName+ "' of '" + parentNamespace + "' will be smoothed to 1!", "NULL")


    try:
        MC.setAttr(mesh + ".displaySmoothMesh",         2) # Display smooth mesh preview
        MC.setAttr(mesh + ".displaySubdComps",          0) # No subdivisions shown
        MC.setAttr(mesh + ".useGlobalSmoothDrawType",   0) # No global subd method
        MC.setAttr(mesh + ".smoothDrawType",            0) # Basic Catmull-Clark
        MC.setAttr(mesh + ".smoothLevel",               0) # Don't touch this
        MC.setAttr(mesh + ".useSmoothPreviewForRender", 0) # Customize smoothing for rendering
        MC.setAttr(mesh + ".renderSmoothLevel",         smoothLevel) # This is what really matters here!!!
        printLog("Smoothing set to " + str(smoothLevel) + " for object '" + parentLastTag + "'", "OK")

    except Exception as error:
        print "[WARNING] Something went wrong!\n" + str(error)   





#======================================================================
# ALEMBIC
#======================================================================
ALEMBIC_DEBUG = False

def getIObjectFromName(name, IRoot):
    return checkAndTraverse(IRoot, name)

def traverseXForms(IObject, dataToDump):
    floatingPointLimit = 1e-11 
    metaData= IObject.getMetaData()
    # check if it's an XForm
    if AL.AbcGeom.IXform.matches(metaData):
        IXformWrap = AL.AbcGeom.IXform(IObject, AL.Abc.WrapExistingFlag(1)) 
        numSamples = IXformWrap.getSchema().getNumSamples()
        
        if ALEMBIC_DEBUG: print IObject.getName(), numSamples 
        
        xformName = IObject.getName()
        # "STATIC"   -> 0 or not, but not animated: just store a single value
        # "ANIMATED" -> a non trivial animation inside: store the full array
        # dataToDump[xformName] = value
        # dataToDump[xformName] = [-, -, -, -, ...]
        
        # STAI ATTENTO A DUMPARE SOLO CIO CHE SERVE. NON LO SCALE CHE GIA FUNZONA
        #(senno raddoppi), serve solo rimpiazare il falso zero 1e-12 con un valido s solido zero...
        #
        # morale, se e' > 1e-11 e' legale. senno lo rimpiazzi con 1e-11 (o zero, NULLA DI PIU)
        # ---- nota che isConstant() e' valutato tu TUTTO lo schema... non separatamente sui canali, per cui e un po uno spreco.. ma amen

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
    printLog("")
    printLog("SAVING DATA FOR 3DSMAX")


    dataFor3DSMax = {}


    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
    # ALEMBICS
    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
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



    if None not in (episode, shot):
        # Scene name is valid
        shortDumpName = episode + "_" + shot + "_DATAFOR3DSMAX.txt"
        path = "Y:\\01_SAISON_4\\09_EPISODES\\04_Fabrication_3D\\" + episode + "\\sh" + shot + "\\lit\\"

        #00;print "episode, shot == ", episode, shot
        #00;print "shortDumpName == ", shortDumpName
        #00;print "path == ", path
        
        # Delete all files with the "_DATAFOR3DSMAX.tx" tag; then write a new one
        items = OS.listdir(path) 
        for item in items:
            if "_DATAFOR3DSMAX" in item:
                try:
                    OS.remove(path + item)
                except Exception as exc:
                    fatality("Can't delete the file '" + item + "'!\nCan't proceed, sorry!")

        dumpName = path + shortDumpName
        fileHandle = None
        try:
            serialized = JSON.dumps(dataFor3DSMax, indent=2)
            fileHandle = open(dumpName, "w")
            fileHandle.write(serialized)
            printLog("'" + shortDumpName + "' written in folder:\n                      " + cutInHalfString(path)[0] + "\n                      " + cutInHalfString(path)[1], "SUCCESS")
        except Exception as e:
            fatality("Can't save dump, sorry!\n" + str(e))
        finally:
            if fileHandle != None:
                fileHandle.close()        

    else:
        fatality("This scene has not a valid name; can't save dump, sorry!")
    

    inViewMessage(message="'_DATAFOR3DSMAX.txt' successfully saved!", position="topLeft", time=2000, status="SUCCESS")



""" ?????????????????????????????????? """
""" ?????????????????????????????????? """
""" ?????????????????????????????????? """
def dumpLightLinker1(*args):
    lightLinker1Node = "lightLinker1"
    lightLinker1NodeDict = {}
    # (compound, light, node)
    compounds = [(".link",         "light",              "object"), 
                 (".ignore",       "lightIgnored",       "objectIgnored"), 
                 (".shadowLink",   "shadowLight",        "shadowObject"), 
                 (".shadowIgnore", "shadowLightIgnored", "shadowObjectIgnored")]
    for triple in compounds:
        # get the list of valid indices of the compound (I guess not sparse...)
        validIndices = MC.getAttr(lightLinker1Node + triple[0], multiIndices=True) or []
        for index in validIndices:
            lightAttribute  = lightLinker1Node + triple[0] + "[" + str(index) + "]." + triple[1]
            objectAttribute = lightLinker1Node + triple[0] + "[" + str(index) + "]." + triple[2]
            # NOTE: "light" can be even a set and "object" a shadingEngine
            lights = MC.listConnections(lightAttribute, source=True) or []
            objects = MC.listConnections(objectAttribute, source=True) or []
            print lightAttribute, lights
            print objectAttribute, objects
                










"""
==================================================================================================================================================
--------------------------------------------------------------------------------------------------------------------------------------------------
88888888ba                                                   
88      "8b                                                  
88      ,8P                                                  
88aaaaaa8P'  8b,dPPYba,   ,adPPYba,    ,adPPYba,  ,adPPYba,  
88""""""'    88P'   "Y8  a8"     "8a  a8"     ""  I8[    ""  
88           88          8b       d8  8b           `"Y8ba,   
88           88          "8a,   ,a8"  "8a,   ,aa  aa    ]8I  
88           88           `"YbbdP"'    `"Ybbd8"'  `"YbbdP"'  
--------------------------------------------------------------------------------------------------------------------------------------------------
==================================================================================================================================================
"""

def cutInHalfString(text=""):
    half = int(len(text)/2.0)
    return [text[:half], text[half:]]


#----------------------------------------------------------------------------
# PROGRESS BAR
def progressBarInitialize(numberOfTasks=0):
    MC.progressBar("PROGRESS_BAR", edit=True, minValue=-1, maxValue=numberOfTasks, progress=0, manage=True)

def progressBarIncrement():
    MC.progressBar("PROGRESS_BAR", edit=True, step=1)

def progressBarHide():
    MC.progressBar("PROGRESS_BAR", edit=True, manage=False)


#----------------------------------------------------------------------------
# INVIEW MESSAGE
def inViewMessage(message="", position="topLeft", time=2000, status="SUCCESS"):
    # A fancy inView message (LEFT TOP)
    if  status  == "SUCCESS":
        COLOR = "#00ff00"
        BKC = 0x00007700
    elif status == "WARNING":
        COLOR = "#ff9900"
        BKC = 0x00775500
    elif status =="ERROR":
        COLOR = "#ff0000"
        BKC = 0x00770000   
    MC.inViewMessage(amg="<font color=" + COLOR + ">" + message + "</font>", bkc=BKC, 
                     pos=position, fade=True , a=.5, fts=18, fit=100, fst=time, fot=100)


#----------------------------------------------------------------------------
# UI LOG
def clearLog():
    # A brand new log
    MC.scrollField("UNIVERSAL_LOG", edit=True, clear=True)

def printLog(message="", status=""):
    STATUS_INFO = {""        :["",            (.23,.23,.23)],
                   "NULL"    :["[NULL]  ",    (.23,.23,.23)],
                   "OK"      :["[OK]  ",      "#FFFFFF"],
                   "SUCCESS" :["[SUCCESS]  ", (.23,.60,.23)],
                   "WARNING" :["[WARNING]  ", (.60,.60,.23)],
                   "ERROR"   :["[ERROR]  ",   (.60,.23,.23)],
                   "FATALITY":["[FATALITY]  ", "#FFAA00"]}
    #message = "<font color=\"" + str(STATUS_INFO[status][1]) + "\"> " + message + "</font>"               
    MC.scrollField("UNIVERSAL_LOG", edit=True, it=("" if status=="" else "  ") + STATUS_INFO[status][0]+message+"\n", ip=0) 

    #print STATUS_INFO[status][0]+" "+message


#----------------------------------------------------------------------------
# FATALITY
def clearFatality():
    # Delete fatality windoz
    if MC.window("fatality_WIN", ex=1):
        MC.deleteUI("fatality_WIN") 

def fatality(message="", culprits=[], title="FATAL ERROR"):
    message = "\n" + message + "\n"
    if MC.window("fatality_WIN", ex=1):
        MC.deleteUI("fatality_WIN") 
    MC.window("fatality_WIN", t="FATALITY", tlb=1, s=1, mb=0, bgc=(0,0,0))

    MC.columnLayout() 
    MC.button(l=title, h=30, bgc=(1,0,0))
    MC.columnLayout("_layoutOne", co=("left",16)) 
    QtText(handle="", label=message, color=(180, 180, 180), paddingTBLR=(0, 0, 0, 0), margin=0, fontFamily="Arial", fontSize=16, fontWeight="normal")

    #MC.text("pippolo", l=message, align="left", rs=True)
    if len(culprits) > 0:
        MC.setParent("..")
        MC.text("\n" + " " * 7 + "CULPRIT NODE(S)")
        MC.columnLayout("_layoutTwo", co=("left",0))
        MC.columnLayout("_layoutThree")
        for culprit in culprits:
            # Apparently all imports are only visible in the script; so, MC.select won't be callable from the UI
            MC.button(l=culprit + "\n[" + MC.nodeType(culprit).upper() + "]", 
                      c="import maya.cmds as MC; MC.select(\"" + culprit + "\", noExpand=True, r=True)")
        pointer = OMUI.MQtUtil.findLayout("_layoutTwo")      
        widget = SHIBOKEN.wrapInstance(long(pointer), QTGUI.QWidget)
        widget.setStyleSheet("""font-style: normal;font-size: 18pt;font-weight: bold;
                                background:qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(0,0,0), stop:1 rgb(80,0,0));
                                color:rgb(255,255,255);
                             """)
        pointer = OMUI.MQtUtil.findLayout("_layoutThree")      
        widget = SHIBOKEN.wrapInstance(long(pointer), QTGUI.QWidget)
        widget.setStyleSheet("""font-style:plain; 
                                background:rgb(100,0,0);
                                color:rgb(255,200,200);
                             """)    
    
    MC.showWindow("fatality_WIN")
    # Let's prettyColor with Qt:) weeeeeeeeeee...
    pointer = OMUI.MQtUtil.findLayout("_layoutOne")      
    widget = SHIBOKEN.wrapInstance(long(pointer), QTGUI.QWidget)
    widget.setStyleSheet("""font-style:plain; 
                            background:qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(60,0,0), stop:1 rgb(0,0,0));
                            color:rgb(255,255,255);
                         """)
    # BRUTAL ABORT, sorry!
    #MC.window("fatality_WIN", edit=1, w=size)
    printLog("Can't proceed!", "FATALITY")
    inViewMessage(message="FATALITY\ncan't proceed", position="topLeft", time=2500, status="ERROR")

    #hide the progressBar 
    progressBarHide()   

    MC.error("FATALITY: Can't proceed!")
   


#----------------------------------------------------------------------------
# SOFT WARNING
def missingAmbientWarning(assetList):
    # Delete first
    if MC.window("missingAmbientWarning_WIN", ex=1):
        MC.deleteUI("missingAmbientWarning_WIN")

    width = 260
    height = 110
    missingAmbientWarning_WIN = MC.window("missingAmbientWarning_WIN", t="WARNING", tlb=1, s=1, mb=0, bgc=(0,0,0))
    MC.columnLayout(w=width) 

    MC.button(l="MISSING AMBIENT PRESETS", w=width, h=30, bgc=(1,.5,0))
    MC.columnLayout("_layoutOne", co=("left",16), w=width) 

    message = "\nThe following assets haven't the required preset!\n Please apply to them another preset manually.\n\n"
    for asset in assetList:
        message += " - " + asset + "\n"
    MC.text(l=message, align="left", rs=True)

    MC.showWindow(missingAmbientWarning_WIN)
    # Let's prettyColor with Qt:) weeeeeeeeeee...
    pointer = OMUI.MQtUtil.findLayout("_layoutOne")      
    widget = SHIBOKEN.wrapInstance(long(pointer), QTGUI.QWidget)
    widget.setStyleSheet("""font-style:plain; 
                            background:qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(80,30,0), stop:1 rgb(0,0,0));
                            color:rgb(255,255,255);
                         """)

    MC.window(missingAmbientWarning_WIN, edit=1, w=width, h=height)
    inViewMessage(message="WARNING: missing presets!", position="topLeft", time=2500, status="WARNING")



#----------------------------------------------------------------------------
# REPORT
def clearReport():
    global REPORT_TEXT
    # A brand new report
    if MC.window("report_WIN", ex=1):
        MC.deleteUI("report_WIN") 
    REPORT_TEXT = ""

def appendReport(message, bars=False, upperBar=False, barSymbol="-", newLines=0):
    global REPORT_TEXT
    # Add a text to the report "REPORT_TEXT"
    separator = barSymbol * 120
    if bars or upperBar:
        REPORT_TEXT += separator + "\n"
      
    if isinstance(message, list) or isinstance(message, dict):
        prettyMessage = JSON.dumps(message, indent=2)
        REPORT_TEXT += prettyMessage + "\n"
    else:
        REPORT_TEXT += message + "\n"  
        
    if bars and not upperBar:
        REPORT_TEXT += separator + "\n"    
    if newLines > 0:
        for i in range(newLines):
            REPORT_TEXT += "\n"

def showPartialReport(*args):
    global REPORT_TEXT
    # Just show the report; do this after a heavy crash
    if REPORT_TEXT != "":
        showReport(title="PARTIAL REPORT", status="PARTIAL")

def showReport(title="", status="SUCCESS"):
    global REPORT_TEXT
    # Show a window with the content of the globalVariable REPORT_TEXT 
    if MC.symbolCheckBox("DETAILEDREPORT_SYMBOLCHECKBOX", query=True, value=True) == False:
        # autoReport not active: do nothing
        return
    size = 900
    if MC.window("report_WIN", ex=1):
        MC.deleteUI("report_WIN") 
    MC.window("report_WIN", t="[YAKARI_renderLibrary] report", tlb=1, s=0, mb=0)
    MC.columnLayout()
    MC.button(l=title, w=size, h=30, bgc=(.3,.3,.3))
    MC.scrollField(w=size, h=600, editable=False, wordWrap=True, text=REPORT_TEXT)

    if status == "SUCCESS":
        MC.button(l="SUCCESS", w=size, bgc=(.2,.8,.2))
    elif status == "FAILURE":
        MC.button(l="FAILURE", w=size, bgc=(1,.2,.2))
    elif status == "PARTIAL":
        MC.button(l="PARTIAL", w=size, bgc=(.3,.3,.3))

    MC.showWindow("report_WIN")
    MC.window("report_WIN", edit=True, w=size, h=655)


#----------------------------------------------------------------------------
# DEBUG
def printDebug(message="", objects=[]):
    # Check if the "HARD DEBUG" symbolCheckBox is on
    if MC.symbolCheckBox("HARDDEBUG_SYMBOLCHECKBOX", query=True, value=True):
        print message
        for object in objects:
            print " - " + object 

def funcDebug():   
    if MC.symbolCheckBox("HARDDEBUG_SYMBOLCHECKBOX", query=True, value=True):
        print "\n\n--------------------------------------------------------------------------------"
        if len(INSPECT.stack()) == 2: 
            # directly called from UI or direct call
            print("FUNCTION CALL: " + INSPECT.stack()[1][3] + "\n[caller: UI]") 
        else:
            # INSPECT.stack() is a list, the function frames... [0]=actual, [1]=previous(i.e. orig func), [2]=caller of previous...
            print("FUNCTION CALL: " + INSPECT.stack()[1][3] + "\n[caller: " + INSPECT.stack()[2][3] + "]") 
        print "--------------------------------------------------------------------------------"
       
# Something went really bad; I lost the first debug, badly implemented. so I need this shit
# (it's activated with the FINAL_DEBUG global variable)       
def finalFuncDebug():   
    if FINAL_DEBUG:
        print "\n--------------------------------------------------------------------------------"
        if len(INSPECT.stack()) == 2: 
            # directly called from UI or direct call
            print("FUNCTION CALL: " + INSPECT.stack()[1][3] + "\n[caller: UI]") 
        else:
            # INSPECT.stack() is a list, the function frames... [0]=actual, [1]=previous(i.e. orig func), [2]=caller of previous...
            print("FUNCTION CALL: " + INSPECT.stack()[1][3] + "\n[caller: " + INSPECT.stack()[2][3] + "]") 

def finalPrintDebug(message="", data=""):
    # Check if the "HARD DEBUG" symbolCheckBox is on
    if FINAL_DEBUG:
        print message
        print data

#----------------------------------------------------------------------------
# GET NODE INFORMATIONS
def getNodeFromPlug(plug):
    # plugs=False returns the nodeName, shapes=True the true node, not the transform
    nodes = MC.listConnections(plug, plugs=False, source=True, destination=False, shapes=True)
    if nodes != None:
        return nodes[0]
    else:
        return None    

def getAttrFromPlug(plug):
    nodes = MC.listConnections(plug, plugs=True, source=True, destination=False, shapes=True)
    if nodes != None:
        attrName = nodes[0].replace(getNodeFromPlug(plug) + ".", "")
        return attrName
    else:
        return None    

def getNamespace(inObj):
    i = inObj.rfind(":")
    if i != -1:
        return inObj[0:i]
    else:
        return ""

def getParent(inNode):
    # Always in full DAGPath mode
    return MC.listRelatives(inNode, parent=True, fullPath=True)[0]

def getDAGPath(inObj):
    # The full DAGPath
    return MC.ls(inObj, long=True)[0]

def getShortDAGPath(inObj):
    # Returns the shortest unambiguous DAGPath 
    return MC.ls(inObj, long=False)[0]

def getActiveIDs(inArrayAttr):
    arrayIDs = []
    arrayAttrs = MC.listAttr(inArrayAttr, multi=True)
    if arrayAttrs != None:
        for arrayAttr in arrayAttrs:
            if "." in arrayAttr:
                continue
            firstIndex = arrayAttr.find("[")
            lastIndex = arrayAttr.find("]")
            if firstIndex == -1 or lastIndex == -1 or firstIndex >= lastIndex:
                appendReport("WARNING", "Can't get brackets indices for ["+ arrayAttr +"]!")
                continue
            arrayIDs.append(int(arrayAttr[firstIndex+1:lastIndex]))
        return arrayIDs
    else:
        # No shadingEngine override: return empty LIST
        return []    

def getReferenceInfo(node):  
    # Returns the reference info for a referenced node
    if MC.referenceQuery(node, isNodeReferenced=True):
        result = {"nodeName":"", "fileName":"", "nameSpace":""} 
        filename = MC.referenceQuery(obj, filename=True)
        result["fileName"]  = filename
        result["nameSpace"] = MC.referenceQuery(filename, referenceNode=True).rstrip("RN")
        result["nodeName"]  = updateDAGPath(getDAGPath(node), "")
        return result
    else:
        return N













"""
==================================================================================================================================================
--------------------------------------------------------------------------------------------------------------------------------------------------     


     QQQQQQQQQ              tttt          
   QQ:::::::::QQ         ttt:::t          
 QQ:::::::::::::QQ       t:::::t          
Q:::::::QQQ:::::::Q      t:::::t          
Q::::::O   Q::::::Qttttttt:::::ttttttt    
Q:::::O     Q:::::Qt:::::::::::::::::t    
Q:::::O     Q:::::Qt:::::::::::::::::t    
Q:::::O     Q:::::Qtttttt:::::::tttttt    
Q:::::O     Q:::::Q      t:::::t          
Q:::::O     Q:::::Q      t:::::t          
Q:::::O  QQQQ:::::Q      t:::::t          
Q::::::O Q::::::::Q      t:::::t    tttttt
Q:::::::QQ::::::::Q      t::::::tttt:::::t
 QQ::::::::::::::Q       tt::::::::::::::t
   QQ:::::::::::Q          tt:::::::::::tt
     QQQQQQQQ::::QQ          ttttttttttt  
             Q:::::Q                      
              QQQQQQ 


--------------------------------------------------------------------------------------------------------------------------------------------------
==================================================================================================================================================
"""

def colorizeInterfaceWithQt(interface="", gradient="rainbow", textColor=(255, 255, 255), direction="leftToRight"):
    textColorString = str(textColor[0]) + ", " + str(textColor[1]) + ", " + str(textColor[2])
    gradientTemplates = {"rainbow": "stop:0 rgb(255, 0, 0), stop:.25 rgb(255,255,0), stop:.5 rgb(0, 255, 0), stop:.75 rgb(0,255,255), stop:1 rgb(0, 0, 255)",
                         "shit":    "stop:.0 rgb(0, 0, 0), stop:1 rgb(255, 0, 0)"}
    directions = {"leftToRight": "x1:0, y1:0, x2:1, y2:0", 
                  "topToBottom": "x1:0, y1:0, x2:0, y2:1", 
                  "diagonal":    "x1:0, y1:0, x2:1, y2:1"}                     

    """ HERE CHECK THE TYPE OF OBJECT, CONTROL OR LAYOUT, cause they have a different syntax """
    UIType = MC.objectTypeUI(interface)
    print "UITYPE = ", UIType
    if "ayout" in UIType:
        # it's a layout probably
        pointer = OMUI.MQtUtil.findLayout(interface)
    else: 
        # probably a control  
        pointer = OMUI.MQtUtil.findControl(interface)
    widget  = SHIBOKEN.wrapInstance(long(pointer), QTGUI.QWidget)
    widget.setStyleSheet("background:qlineargradient(" + directions[direction] + "," + gradientTemplates[gradient] + "); color:rgb(" + textColorString + ");")

def QtOverrides(*args):
    object  = None
    pointer = OMUI.MQtUtil.findControl(object)      
    widget  = SHIBOKEN.wrapInstance(long(pointer), QTGUI.QWidget)
    widget.setStyleSheet("""border-radius: 12px;
                            border-width: 2px;
                            border-style: dot-dot-dash;
                            border-color: black;
                            font-style: italic;
                            font-size: 12px;
                            text-decoration: line-through;
                            spacing: 20;
                         """)
        
def QtButtonEnable(handle="", enable=True):
    MC.button(handle, edit=True, enable=enable)
    
def QtButton(handle="", label="", action="", lineColor=(100,220,100), background=(80,130,80), borderRadius=16, paddingTBLR=(20,20,10,10), margin=0, w=40, h=40, fontFamily="Arial", fontSize=14, fontWeight="bold", annotation=None):
    # Parasites the commandEngine with some Qt features...   
    if handle != "":          
        handle = MC.button(handle, l=label, w=w, h=h)     
    else:
        handle = MC.button(l=label, w=w, h=h)     
    
    borderColorWeight = 1
    borderColor = tuple(x * borderColorWeight for x in lineColor)
    #borderColor = (lineColor[0] * borderColorWeight, lineColor[1] * borderColorWeight, lineColor[2] * borderColorWeight)                   
    styleSheet  = "QPushButton{border-radius: " + str(borderRadius) + "px;" +\
                              "border-width: 2px;" +\
                              "border-style: solid;" +\
                              "font-size: " + str(fontSize) + "px;" +\
                              "font-family: " + fontFamily + ";" +\
                              "font-weight: " + fontWeight + ";" +\
                              "font-style: normal;" +\
                              "border-color: rgb" + str(background) + ";" +\
                              "color: rgb" + str(lineColor) + ";" +\
                              "background: rgb" + str(background) + ";" +\
                              "padding-top:" + str(paddingTBLR[0]) + "px;" +\
                              "padding-bottom:" + str(paddingTBLR[1]) + "px;" +\
                              "padding-left:" + str(paddingTBLR[2]) + "px;" +\
                              "padding-right:" + str(paddingTBLR[3]) + "px;" +\
                              "margin: " + str(margin) + "px}"      
    styleSheet += "QPushButton:disabled{background: rgb(90, 90, 90);" +\
                                       "color: rgb(70, 70, 70);" +\
                                       "border-color: rgb(90, 90, 90);}"
    hoverAdd          = 50
    hoverLineColor    = (min(lineColor[0]  + hoverAdd, 255), min(lineColor[1]  + hoverAdd, 255), min(lineColor[2]  + hoverAdd, 255)) 
    hoverBackground   = (min(background[0] + hoverAdd, 255), min(background[1] + hoverAdd, 255), min(background[2] + hoverAdd, 255))
    pressedAdd        = 90
    pressedLineColor  = (min(lineColor[0]  + pressedAdd, 255), min(lineColor[1]  + pressedAdd, 255), min(lineColor[2]  + pressedAdd, 255))              
    pressedBackground = (min(background[0] + pressedAdd, 255), min(background[1] + pressedAdd, 255), min(background[2] + pressedAdd, 255))          
    styleSheet += "QPushButton:hover{border-width:3px;" +\
                                    "background:rgb" + str(hoverBackground) + ";" +\
                                    "color:rgb" + str(hoverLineColor) + ";" +\
                                    "border-color:rgb" + str(hoverLineColor) + ";}"
    styleSheet += "QPushButton:pressed{border-width:3px;" +\
                                      "background:rgb" + str(pressedBackground) + ";" +\
                                      "color:rgb" + str(pressedLineColor) + ";" +\
                                      "border-color:rgb" + str(pressedLineColor) + ";}"                                                      
    pointer = OMUI.MQtUtil.findControl(handle)  
    widget  = SHIBOKEN.wrapInstance(long(pointer), QTGUI.QPushButton)
    widget.clicked.connect(action)
    widget.setStyleSheet(styleSheet)   
    if annotation != None:
        MC.button(handle, edit=True, ann=annotation)

def QtText(handle="", label="", color=(180, 180, 180), paddingTBLR=(0, 0, 0, 0), margin=0, fontFamily="Arial", fontSize=14, fontWeight="normal", align="left"):
    # Parasites the commandEngine with some Qt features...   
    
    if handle == "": 
        # NECESSARY; if control's name is "", Maya doesn't assign a valid name to the controller and fails...           
        handle = MC.text() 
    else:    
        handle = MC.text(handle)                      

    styleSheet = "font-size: " + str(fontSize) + "px;" +\
                 "font-family: " + fontFamily + ";" +\
                 "font-weight: " + fontWeight + ";" +\
                 "font-style: normal;" +\
                 "color: rgb" + str(color) + ";" +\
                 "padding-top:" + str(paddingTBLR[0]) + "px;" +\
                 "padding-bottom:" + str(paddingTBLR[1]) + "px;" +\
                 "padding-left:" + str(paddingTBLR[2]) + "px;" +\
                 "padding-right:" + str(paddingTBLR[3]) + "px;" +\
                 "margin: " + str(margin) + "px}"      
                                                    
    pointer = OMUI.MQtUtil.findControl(handle)  
    widget  = SHIBOKEN.wrapInstance(long(pointer), QTGUI.QPushButton)
    widget.setStyleSheet(styleSheet)
    MC.text(handle, edit=True, l=label, align=align)

def QtSymbolButton(name="", image="circle.png", command="", ann="EMPTY"):
    handle = MC.symbolButton(name, image=image, command=command, ann=ann, h=52, w=52)
    """
    pointer = OMUI.MQtUtil.findControl(handle)      
    widget  = SHIBOKEN.wrapInstance(long(pointer), QTGUI.QWidget)
    widget.setStyleSheet(border-radius: 22px;
                            border-width: 1px;
                            border-style: solid;
                            border-color: rgb(0,140,140);
                            margin: 1px;
                            background: rgb(0,100,100);
                         )
    widget.setCursor(QTGUI.IBeamCursor)
    """
    return handle

def QtCustomizeWindow(handle=""):
    pointer = OMUI.MQtUtil.findWindow(handle)  
    window  = SHIBOKEN.wrapInstance(long(pointer), QTGUI.QWidget)  
    print window.windowTitle()

def QtFrameLayout(label="", borderStyle="etchedIn", backgroundColor=(.3, .5, .8), borderVisible=True, mw=4, mh=4, w=100, enable=True):
    handle = MC.frameLayout(l=label, bs=borderStyle, bgc=backgroundColor, bv=borderVisible, mw=mw, mh=mh, w=w, enable=enable)
    return handle   









"""
==================================================================================================================================================
--------------------------------------------------------------------------------------------------------------------------------------------------                                                                                                                         
888       888 8888888b.         d8888 8888888b.  8888888b.  8888888888 8888888b.   .d8888b.  
888   o   888 888   Y88b       d88888 888   Y88b 888   Y88b 888        888   Y88b d88P  Y88b 
888  d8b  888 888    888      d88P888 888    888 888    888 888        888    888 Y88b.      
888 d888b 888 888   d88P     d88P 888 888   d88P 888   d88P 8888888    888   d88P  "Y888b.   
888d88888b888 8888888P"     d88P  888 8888888P"  8888888P"  888        8888888P"      "Y88b. 
88888P Y88888 888 T88b     d88P   888 888        888        888        888 T88b         "888 
8888P   Y8888 888  T88b   d8888888888 888        888        888        888  T88b  Y88b  d88P 
888P     Y888 888   T88b d88P     888 888        888        8888888888 888   T88b  "Y8888P"  
                                                                                            
==================================================================================================================================================
--------------------------------------------------------------------------------------------------------------------------------------------------                                                                                                                         
"""                                                                                                                     
#======================================================================================================================
#----------------------------------------------------------------------------------------------------------------------
# MAYA NODE WRAPPERS
#----------------------------------------------------------------------------------------------------------------------
#======================================================================================================================
class DGNode():
    """
    Simple first wrapper to a DG node...
    (crea una classe generica DGNodes, con i comandi tipici dei DG, poi eredita specializzando in 
     DAG, poi mesh, nurbs etc etc; la classe base definisce i metodi validi per tutti, salvo poi
     fare override quando serve nelle derivate...)
    - inevitabilmente, dovrai ritornare dei DGNodes e wrappare molta altra roba 
    - TIENI CONTO CHE E INEVITABILMENTE PIU LENTO
    """
    def __init__(self, node):
        if MC.objExists(node):
            self.name = MC.ls(node, long=True)
            self.type = MC.nodeType(node)
        else:
            MC.error("[FATAL] The name '" + node + "' is not bound to any node! Can't create a DGNode.")    
            
    def getParent(self, DAGPath=True):
        """
        Gets the parent, None if son of the world
        """
        parents = MC.listRelatives(self.name, parent=True, fullPath=DAGPath) or []
        if len(parents) > 0:
            return parents[0]
        else:
            None
            
    def getMeshChildren(self, DAGPath=True, noIntermediate=True):
        """
        MAYA BUG: in listRelatives, you can't have both "type=" and "noIntermediate="...
        """
        meshes = MC.listRelatives(self.name, children=True, type="mesh", fullPath=DAGPath) or []
        validMeshes = MC.ls(meshes, noIntermediate=noIntermediate, long=DAGPath) # kinda hacky but it works
        return validMeshes

class ____DGNode():
    def __init__(self, node):
        if MC.objExists(node):
            self.name = MC.ls(node, long=True)[0]
            self.type = MC.nodeType(node)
        else:
            MC.error("[FATAL] The name '" + node + "' is not bound to any node! Can't create a DGNode.")    
    def __str__(self):
        return self.name
        
    def attrExists(self, attr=""):
        return MC.attributeQuery(attr, node=self.name, exists=True)
                        
    def attrLocked(self, attr=None):
        if attr != None and self.attrExists(attr):
            return MC.getAttr(self.name + "." + attr, lock=True)
        else:
            MC.error("[ERROR] The node '" + self.name + "' has not the attribute '" + attr + "'!")

    def lockAttr(self, attr):
        if attr != None and self.attrExists(attr):      
            MC.setAttr(self.name + "." + attr, lock=True)
        else: 
            MC.error("[ERROR] The node '" + self.name + "' has not the attribute '" + attr + "'!")

    def unlockAttr(self, attr):
        if attr != None and self.attrExists(attr):      
            MC.setAttr(self.name + "." + attr, lock=False)
        else: 
            MC.error("[ERROR] The node '" + self.name + "' has not the attribute '" + attr + "'!")
    
    def select(self, replace=False, toggle=False, add=False, deselect=False):
        if replace:
            MC.select(self.name, replace=True)
        elif toggle:
            MC.select(self.name, toggle=True)
        elif add:
            MC.select(self.name, add=True)
        elif deselect:
            MC.select(self.name, deselect=True)        
        else:
            # invoking a .select() does a replace
            MC.select(self.name, replace=True)    
              
    def attrConnected(self, attr=""):
        pass
    def sourceConnection(self, attr=""):
        pass
    def destinationConnections(self, attr=""):
        pass            
        














"""
==================================================================================================================================================
--------------------------------------------------------------------------------------------------------------------------------------------------
888b      88                        88              88888888ba,                                                                          
8888b     88                        88              88      `"8b                                                                         
88 `8b    88                        88              88        `8b                                                                        
88  `8b   88   ,adPPYba,    ,adPPYb,88   ,adPPYba,  88         88  88       88  88,dPYba,,adPYba,   8b,dPPYba,    ,adPPYba,  8b,dPPYba,  
88   `8b  88  a8"     "8a  a8"    `Y88  a8P_____88  88         88  88       88  88P'   "88"    "8a  88P'    "8a  a8P_____88  88P'   "Y8  
88    `8b 88  8b       d8  8b       88  8PP"""""""  88         8P  88       88  88      88      88  88       d8  8PP"""""""  88          
88     `8888  "8a,   ,a8"  "8a,   ,d88  "8b,   ,aa  88      .a8P   "8a,   ,a88  88      88      88  88b,   ,a8"  "8b,   ,aa  88          
88      `888   `"YbbdP"'    `"8bbdP"Y8   `"Ybbd8"'  88888888Y"'     `"YbbdP'Y8  88      88      88  88`YbbdP"'    `"Ybbd8"'  88     
                                                                                                    88
                                                                                                    88

     ,adPPYba,   ,adPPYba,   8b,dPPYba,   ,adPPYba,                                                                                   
    a8"     ""  a8"     "8a  88P'   "Y8  a8P_____88                                                                                   
    8b          8b       d8  88          8PP"""""""                                                                                      
    "8a,   ,aa  "8a,   ,a8"  88          "8b,   ,aa                                                                                      
     `"Ybbd8"'   `"YbbdP"'   88           `"Ybbd8"' 
--------------------------------------------------------------------------------------------------------------------------------------------------
==================================================================================================================================================
"""
STORED_ATTRS          = {}

#------------------------------------------------------------------------------------------------------------
# Registered attribute types
#------------------------------------------------------------------------------------------------------------
# An attribute with this label rejects TYPE IDENTIFICATION! No idea why this happens
WEIRD_LABELS          = ["edge[", 
                         "face["] 

# Standard uncompound types; they're dumpable
RELEVANT_ATTR_TYPES   = ["byte", 
                         "char", 
                         "short", 
                         "long", 
                         "float", 
                         "double",
                         "bool", 
                         "enum", 
                         "string",
                         "doubleLinear", 
                         "floatLinear", 
                         "doubleAngle", 
                         "time"]

# Compound/weird/undumpable attributes (or already dumped per-component)                        
IRRELEVANT_ATTR_TYPES = ["None", # String representation of the getAttr(type)-result "null" for undefined declared attrs  
                         "TdataCompound", 
                         "generic",
                         "addr", 
                         "void",
                         "attributeAlias",
                         "function",
                         "dataReferenceEdits",
                         "matrix", # Numeric compounds
                         "long2", 
                         "long3", 
                         "float2", 
                         "float3",
                         "float4", 
                         "double2", 
                         "double3", 
                         "double4",
                         "doubleArray", # Arrays
                         "pointArray", 
                         "stringArray", 
                         "Int32Array", 
                         "mesh", # Geometries
                         "dataPolyComponent", 
                         "componentList",  
                         "nurbsCurve",
                         "nurbsCurveHeader"]  

# Types to be skipped, yet not listed as IRRELEVANT
UNREGISTERED_ATTR_TYPES      = []                                      

#------------------------------------------------------------------------------------------------------------
# CORE
#------------------------------------------------------------------------------------------------------------
def doLoadNodesDump(*args):
    path = MC.fileDialog2(fileFilter="*.txt", fileMode=1, dialogStyle=1, caption="Open a layers dump file")
    loadNodesDump(path)

def loadNodesDump(path):
    if path != None and len(path) > 0:
        path = path[0]
        f = None
        nodesDump = None
        try:
            f = open(path, "r")
            nodesDump = JSON.loads(f.read())
        except Exception as e:
            fatality("Unable to load:\n" + path + "\n\nReason:\n" + str(e))
        finally:
            if f != None:
                f.close()
    
    # INITIALIZE THE PROGRESS BAR
    thingsToDo = 0
    for key in nodesDump:
        thingsToDo += len(nodesDump[key]) 
    progressBarInitialize(numberOfTasks=thingsToDo)

    # Apply dump to existing nodes
    for node in nodesDump.keys():
        #print "\n\n---------------------------\n" + node + "\n---------------------------"           
        for attr in nodesDump[node].keys():
            #print attr
            (type, value) = nodesDump[node][attr]
            try:
                if value != None:
                    if type != "string":
                        MC.setAttr(node + "." + attr, value)    
                    else:
                        MC.setAttr(node + "." + attr, value, type="string") 
            except Exception as e:
                MC.warning("[WARNING] " + str(e))            
            progressBarIncrement()              
    progressBarHide()

def detectUnregisteredTypes(nodeList):
    for node in nodeList:
        attrList = MC.listAttr(node, hasData= True, multi=True, shortNames=False)
        for attr in attrList:
            # avoid anomalies
            isAcceptable = True
            for anomaly in WEIRD_LABELS:
                if anomaly in attr:
                    # Is it a "real" attribute? It refuses any getAttr...
                    isAcceptable = False
            if isAcceptable == False:
                continue   
            attrType = str(MC.getAttr(node + "." + attr, type=True)) # The str() convert null in "None"
            if not attrType in RELEVANT_ATTR_TYPES and not attrType in IRRELEVANT_ATTR_TYPES:
                print "SHIT: " + node + "." + attr + "  TYPE:" + attrType
                WEIRD_ATTR_TYPES.append(attrType)
         
def storeNodes(*args):
    clearLog()
    STORED_ATTRS.clear()
    
    nodeList = MC.ls(sl=True)
    storedNodes_text = ""
    for node in nodeList:
        storedNodes_text += node + "\n"
    if storedNodes_text == "":
        storedNodes_text = "..."    
    MC.scrollField("storedNodes_scrollField", edit=True, text=storedNodes_text)

    for node in nodeList:
        STORED_ATTRS[node] = {}
        # The trick here is to force Maya to list all the compounds; 
        # then detect and avoid the TData and all the other shit.
        attrList = MC.listAttr(node, hasData= True, multi=True, shortNames=False)
        progressBarInitialize(numberOfTasks=len(attrList))
        for attr in attrList:
            # avoid anomalies
            isAcceptable = True
            for anomaly in WEIRD_LABELS:
                if anomaly in attr:
                    # Is it a "real" attribute? It refuses any getAttr...
                    isAcceptable = False
            if isAcceptable == False:
                continue   
            attrType = MC.getAttr(node + "." + attr, type=True)
            if attrType in RELEVANT_ATTR_TYPES: 
                STORED_ATTRS[node][attr] = (attrType, MC.getAttr(node + "." + attr))
            progressBarIncrement()
        progressBarHide()        

def saveNodesDump(*args):
    print JSON.dumps(STORED_ATTRS, indent=2)
    path = MC.fileDialog2(fileFilter="*.txt", fileMode=0, dialogStyle=1, caption="Save nodes dump:")
    #path = ["C:/Users/guido.pollini/Desktop/RENDERING/TESTS/ch_strai_GUIDUMP.txt"] #Temporary dump
    if path != None and len(path) > 0:
        path = path[0]
        f = None
        try:
            dump = JSON.dumps(STORED_ATTRS, indent=2)
            f = open(path, "w")
            f.write(dump)
        except Exception as e:
            print "FUCK"
            #appendReport("ERROR", "Cannot save layers to [" + path + "]: " + str(e))
        finally:
            if f != None:
                f.close()
        #appendReport("OK", "LayersDump written to [" + path + "]")

def detectChanges(*args):
    clearLog()
    printLog("DETECTED CHANGES:")

    detectedChanges_text = ""
    for node in STORED_ATTRS.keys():
        progressBarInitialize(numberOfTasks=len(STORED_ATTRS[node]))
        for attr in STORED_ATTRS[node].keys():
            #
            # INSERISCI UN TRY EXCEPT... and intercept the result in a
            # SCROLL TEXT "universal log", normalmentez visibile, con un "printLog"
            # se non esiste la finestra, fai output sullo scvript editor
            #
            if attr == "binMembership":
                continue
            value = MC.getAttr(node + "." + attr)
            if STORED_ATTRS[node][attr][1] != value:
                detectedChanges_text += " - "+node+"."+attr+":   "+str(STORED_ATTRS[node][attr][1])+" --> "+str(value)+"\n"   
            progressBarIncrement()
        progressBarHide()         
    if detectedChanges_text == "":
        detectedChanges_text = "none"
    printLog(detectedChanges_text)
  


 































"""
==================================================================================================================================================
--------------------------------------------------------------------------------------------------------------------------------------------------
88               88           
88               ""    ,d     
88                     88     
88  8b,dPPYba,   88  MM88MMM  
88  88P'   `"8a  88    88     
88  88       88  88    88     
88  88       88  88    88,    
88  88       88  88    "Y888  
--------------------------------------------------------------------------------------------------------------------------------------------------
==================================================================================================================================================
"""
UI_PERMANENTLY_UNLOCKED = False

def unlockUIPermanently(*args):
    global UI_PERMANENTLY_UNLOCKED
    UI_PERMANENTLY_UNLOCKED = True
    print "UNLOCKED"
    lockUnlockUI()

def lockUI(*args):
    MC.columnLayout("PROD_PLACEHOLDER", edit=True, enable=0)
    MC.symbolButton("YAKARI_LOGO", edit=True, enable=0)
    # That stupid "seasonLogo"


def unlockUI(*args):
    MC.columnLayout("PROD_PLACEHOLDER", edit=True, enable=1)
    MC.symbolButton("YAKARI_LOGO", edit=True, enable=1)
    # That stupid "seasonLogo"

def lockUnlockUI(*args):
    # I forgot to disable the API callback. So, it will stay active forever;
    # An error here means that the callBack is still active; don't do anything at all 
    try:
        # check if the SCENENAME is correct
        # (e.g; disable the UI when scenen not saved)

        if CURRENT_UIMODE != "PROD":
            # just prod mode must be unlocked
            print CURRENT_UIMODE
            return 
        if UI_PERMANENTLY_UNLOCKED:
            unlockUI()
            return

        MC.refresh()
        episode, shot = getProperEpisodeShotName()
        print episode, shot
        if episode is not None and shot is not None:
            # probably valid
            unlockUI()
        else:
            lockUI()    
        """
        sceneName = MC.file(q=True, sceneName=True, shortName=True)
        tokens = sceneName.split("_")
        if len(tokens) >= 2 and "YKR" in tokens[0]:  
            # probably valid
            unlockUI()
        else:
            lockUI()
        """    
    except:
        pass        

def closeSecondaryWindows(*args):
    # Close all secondary windows
    if MC.window("fatality_WIN", ex=1):
        MC.deleteUI("fatality_WIN") 
    if MC.window("addCustomLayers_WIN", ex=1):
        MC.deleteUI("addCustomLayers_WIN")
    if MC.window("manageCombineGroups_WIN", ex=1):
        MC.deleteUI("manageCombineGroups_WIN") 
    if MC.window("granularOptions_WIN", ex=1):
        MC.deleteUI("granularOptions_WIN")  


CALLBACK_ID = None
CURRENT_UIMODE = "PROD"

def initializeUI(*args):
    # If you don't do this, invoking the initializeUI() will crash. 
    # The global variables won't be initialized
    global COMBINED_ASSETS
    global AVAILABLE_GROUPS
    global COMBINED_ASSETS_LOCAL
    global AVAILABLE_GROUPS_LOCAL
    COMBINED_ASSETS  = {}
    AVAILABLE_GROUPS = []
    COMBINED_ASSETS_LOCAL  = {}
    AVAILABLE_GROUPS_LOCAL = []
    
    global INITIALIZE_COMBINED_DATA_ON_REFRESH
    INITIALIZE_COMBINED_DATA_ON_REFRESH = True 


    global CALLBACK_UI
    print "#--------------------------#"
    print "   YAKARI_renderLibrary  "
    print "  (" + VERSION + ")"
    print "#--------------------------#"

    YAKARI_renderLibraryUI()
    refreshAssetsList()
    sceneListener()
    selectionListener()
  
    closeSecondaryWindows()  

    prodModeClicked()
    CALLBACK_ID = OM.MSceneMessage.addCallback(OM.MSceneMessage.kAfterSave, lockUnlockUI)

    # deactivate viewPort 2.0
    #deactivateViewport20()


#OM.MSceneMessage.removeCallback(id)





















