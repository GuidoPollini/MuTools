# Avoid pointing to Toonkit WKG shit
"""
import os
myFuckingPath = "Y:/01_SAISON_4/05_UTILE/Rendu/13_REMOTE_MAYA"
if myFuckingPath not in os.sys.path:
        os.sys.path.append(myFuckingPath)

import remoteMaya_client
reload(remoteMaya_client)
"""





print '[{0}] loading from "{1}"...'.format(__name__, __file__)





import maya.cmds       as MC
import maya.mel        as MM
import maya.OpenMayaUI as OMUI

import PySide.QtCore   as QC
import PySide.QtGui    as QG 
import shiboken

import getpass
import os
import socket
import subprocess
import time
import urllib2




def refreshShotList(*args):
    episodeName = MC.optionMenu("EPISODES_OPTIONMENU", query=True, value=True)
    episodePath = "Y:/01_SAISON_4/09_EPISODES/04_Fabrication_3D/" + episodeName
    shotList = [x for x in os.listdir(episodePath) if x.startswith("sh")]
    try:
    	MC.deleteUI("VOID")
    except:
        pass	
    MC.text("SHOT_TEXT", edit=1, enable=1)    
    MC.deleteUI("SHOTS_OPTIONMENU")
    0;  MC.optionMenu("SHOTS_OPTIONMENU", p="HOLDER", changeCommand="pass")
    for shot in shotList:
    	MC.menuItem(label=shot, p="SHOTS_OPTIONMENU")
    

def inspectShot():
    episodeName = MC.optionMenu("EPISODES_OPTIONMENU", query=True, value=True)
    shotName    = MC.optionMenu("SHOTS_OPTIONMENU", query=True, value=True)
    path = "Y:/01_SAISON_4/09_EPISODES/04_Fabrication_3D/" + episodeName + "/" + shotName + "/ani/maya/"
    mayaAsciiFiles = [x for x in os.listdir(path) if x.endswith(".ma")] or []
    if len(mayaAsciiFiles) == 0:
    	MC.error("No Maya ASCII found!")
    
    command = 'MC.file("' + path + mayaAsciiFiles[0] + '", f=True, options="v=0;", loadReferenceDepth="none", ignoreVersion=True, typ="mayaAscii", o=True)'
    execRemoteCommand(command)
    	


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
                              "border-color: rgb" + str(borderColor) + ";" +\
                              "color: rgb" + str(lineColor) + ";" +\
                              "background: rgb" + str(background) + ";" +\
                              "padding-top:" + str(paddingTBLR[0]) + "px;" +\
                              "padding-bottom:" + str(paddingTBLR[1]) + "px;" +\
                              "padding-left:" + str(paddingTBLR[2]) + "px;" +\
                              "padding-right:" + str(paddingTBLR[3]) + "px;" +\
                              "margin: " + str(margin) + "px}"      
    styleSheet += "QPushButton:disabled{background: rgb(80, 80, 80);" +\
                                       "color: rgb(100, 100, 100);" +\
                                       "border-color: rgb(100, 100, 100);}"
    hoverAdd          = 20
    hoverLineColor    = (min(lineColor[0]  + hoverAdd, 255), min(lineColor[1]  + hoverAdd, 255), min(lineColor[2]  + hoverAdd, 255)) 
    hoverBackground   = (background[0] + hoverAdd, background[1] + hoverAdd, background[2] + hoverAdd)
    pressedAdd        = 30
    pressedLineColor  = (min(lineColor[0]  + pressedAdd, 255), min(lineColor[1]  + pressedAdd, 255), min(lineColor[2]  + pressedAdd, 255))              
    pressedBackground = (background[0] + pressedAdd, background[1] + pressedAdd, background[2] + pressedAdd)          
    styleSheet += "QPushButton:hover{border-width:3px;" +\
                                    "background:rgb" + str(hoverBackground) + ";" +\
                                    "color:rgb" + str(hoverLineColor) + ";" +\
                                    "border-color:rgb" + str(hoverLineColor) + ";}"
    styleSheet += "QPushButton:pressed{border-width:3px;" +\
                                      "background:rgb" + str(pressedBackground) + ";" +\
                                      "color:rgb" + str(pressedLineColor) + ";" +\
                                      "border-color:rgb" + str(pressedLineColor) + ";}"                                                      
    pointer = OMUI.MQtUtil.findControl(handle)  
    widget  = shiboken.wrapInstance(long(pointer), QG.QPushButton)
    widget.clicked.connect(action)
    widget.setStyleSheet(styleSheet)   
    if annotation != None:
        MC.button(handle, edit=True, ann=annotation)








class MayaClient(object):
    #def __new__(cls):
    #    pass


    def __init__(self):
        #self._stack = []
        #self._iswaiting = False
        pass

    @staticmethod
    def _urlify(message):
        message = message.replace("\"", "%22")
        message = message.replace(" ",  "%20")
        return message


    def sendToServer(self, message):
        try:
            mayaServerURL = 'http://' + socket.gethostbyname(socket.gethostname()) + ':8000/?'
            query = urllib2.urlopen(mayaServerURL + MayaClient._urlify(message), data='') # With this (not None) it becomes a POST
            #print query.read()
            print 'Message "' + message + '" sent!'

        except urllib2.URLError as exc:
            print str(exc)
            MC.error('[FATAL] "remoteMaya" is dead:(')
     

    def receiveFromServer(self, message):
        print 'Received from server:', message
        exec message
        # Does this execute the 'message' in Maya's idle time? Otherwise is it the same?
        #MC.evalDeferred(message)


    def waitForAnswer(self):
        pass


    def remoteMayaLoaded(self):
        MC.deleteUI("waitUI_WIN") 
        remoteMayaUI()
        #MC.evalDeferred('MC.rowLayout("HOLDER", edit=True, enable=1)')

    def manualCommand(self, *args):     
        message = MC.textField("COMMAND_TEXTFIELD", query=True, text=True)
        self.sendToServer(message)

mayaClient = MayaClient()




def remoteMayaUI(*args):
    if MC.window("remoteMayaUI_WIN", ex=1):
        MC.deleteUI("remoteMayaUI_WIN") 
    MC.window("remoteMayaUI_WIN", t="REMOTE MAYA", tlb=1, s=0, mb=0)
    MC.columnLayout()
    MC.rowLayout("HOLDER", nc=4, enable=1)
    0;  MC.text(label="    Episode")
    0;  MC.optionMenu("EPISODES_OPTIONMENU", changeCommand=refreshShotList)
    0;  MC.text("SHOT_TEXT", label="    Shot", enable=0)
    0;  MC.optionMenu("SHOTS_OPTIONMENU", changeCommand="pass", enable=0)

    MC.menuItem(label="", p="SHOTS_OPTIONMENU", enable=0)

    episodePath = "Y:/01_SAISON_4/09_EPISODES/03_Fabrication_2D/"
    episodeList = [x for x in os.listdir(episodePath) if len(x) >= 3 and x[:3] == "YKR"]
    0;  MC.setParent("..")
    MC.menuItem("VOID", label="...", p="EPISODES_OPTIONMENU")

    for episode in episodeList:
        MC.menuItem(label=episode, p="EPISODES_OPTIONMENU")
    MC.rowLayout(nc=2)
    0;  MC.text(l="", w=68)
    0;  QtButton(handle="INSPECT", label="INSPECT", action=inspectShot,  
                 lineColor=(100,240,100), background=(60,120,60), 
                 borderRadius=14, paddingTBLR=(0,0,0,0), margin=0, w=120, h=30,
                 fontFamily="Arial", fontSize=16, fontWeight="bold")
    MC.setParent("..")
    MC.textField("COMMAND_TEXTFIELD", text = "", changeCommand=mayaClient.manualCommand)
    MC.scrollField("PNG_UNIVERSAL_LOG", h=430, font="plainLabelFont", editable=False, wordWrap=True, text="Ready...\n", bgc=(.2,.2,.2))
    MC.progressBar("PNG_PROGRESS_BAR", h=16, w=260, manage=0)
    
    MC.showWindow("remoteMayaUI_WIN")
    MC.window("remoteMayaUI_WIN", edit=True, w=600, h=300)


def commandPort_callbackPython(message):
    print "commandPort_callback: ", message
    mayaClient.receiveFromServer(message)

melWrapper = 'global proc commandPort_callbackMEL(string $arg){' +\
             'python(("' + __name__ + '.commandPort_callbackPython(\\"" + $arg + "\\")"));' +\
             '}'

MM.eval(melWrapper)

if MC.commandPort(":7777", query=True):
    MC.commandPort(name=":7777", close=True)
    # Without this, apparently the eventLoop is not updated: the following command would fail!!!
    #
    # Probable: during a script, the eventLoop is disabled, unless you force the update with MC.refresh()
    # (the commandPort system is tied to the UI eventLoop; you don't have it in mayapy!)
    MC.refresh()
 
MC.commandPort(name=":7777", echoOutput=False, noreturn=False,
               prefix="commandPort_callbackMEL", returnNumCommands=True)





actualEnv = os.environ.copy() # .copy() is a <dict> method for shallow copy
varToNullify = ["MAYADEV_APP_PATH", "LOCAL_PATH", "SERVER_PATH", "PROMPT", "MAYA_APP_PATH", "MAYA_CUSTOM_TEMPLATE_PATH"]
for var in varToNullify:
    actualEnv[var] = ""
 
modifiedVars = {
"MAYA_MODULE_PATH": "C:/Program Files/Autodesk/Maya2015/modules;C:/Users/guido.pollini/Documents/maya/2015-x64/modules;C:/Users/guido.pollini/Documents/maya/modules;C:/Program Files/Common Files/Autodesk Shared/Modules/maya/2015",
"PYTHONPATH": "C:/Program Files/Autodesk/Maya2015/plug-ins/bifrost/scripts/presets;C:/Program Files/Autodesk/Maya2015/plug-ins/bifrost/scripts;C:/ExocortexAlembic/Maya2015/Module/scripts;C:/Program Files/Autodesk/Maya2015/plug-ins/fbx/scripts;C:/Program Files/Autodesk/mentalrayForMaya2015/scripts/AETemplates;C:/Program Files/Autodesk/mentalrayForMaya2015/scripts/mentalray;C:/Program Files/Autodesk/mentalrayForMaya2015/scripts/unsupported;C:/Program Files/Autodesk/mentalrayForMaya2015/scripts;C:/Program Files/Autodesk/Maya2015/plug-ins/substance/scripts;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/cafm;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/xmaya;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/brushes;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/dialogs;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/fxmodules;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/tabs;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/util;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/widgets;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts",
"MAYA_PRESET_PATH": "C:/Program Files/Autodesk/Maya2015/plug-ins/bifrost/presets;C:/ExocortexAlembic/Maya2015/Module/presets;C:/Program Files/Autodesk/Maya2015/plug-ins/fbx/presets;C:/Program Files/Autodesk/mentalrayForMaya2015/presets/attrPresets;C:/Program Files/Autodesk/mentalrayForMaya2015/presets/attrPresets/maya_bifrost_liquid;C:/Program Files/Autodesk/mentalrayForMaya2015/presets/attrPresets/mia_material;C:/Program Files/Autodesk/mentalrayForMaya2015/presets/attrPresets/mia_material_x;C:/Program Files/Autodesk/mentalrayForMaya2015/presets/attrPresets/mia_material_x_passes;C:/Program Files/Autodesk/mentalrayForMaya2015/presets;C:/Program Files/Autodesk/Maya2015/plug-ins/substance/presets;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/presets",
"XBMLANGPATH": "C:/Users/guido.pollini/Documents/maya/2015-x64/prefs/icons;C:/Users/guido.pollini/Documents/maya/prefs/icons;C:/ProgramData/Autodesk/maya/2015;C:/Program Files/Autodesk/Maya2015/icons;C:/Program Files/Autodesk/Maya2015/app-defaults;C:/Program Files/Autodesk/Maya2015/icons/paintEffects;C:/Program Files/Autodesk/Maya2015/icons/fluidEffects;C:/Program Files/Autodesk/Maya2015/icons/hair;C:/Program Files/Autodesk/Maya2015/icons/cloth;C:/Program Files/Autodesk/Maya2015/icons/live;C:/Program Files/Autodesk/Maya2015/icons/fur;C:/Program Files/Autodesk/Maya2015/icons/muscle;C:/Program Files/Autodesk/Maya2015/icons/turtle;C:/Program Files/Autodesk/Maya2015/icons/FBX;C:/Program Files/Autodesk/Maya2015/icons/mayaHIK;C:/Program Files/Autodesk/Maya2015/plug-ins/bifrost/icons;C:/ExocortexAlembic/Maya2015/Module/icons;C:/Program Files/Autodesk/Maya2015/plug-ins/fbx/icons;C:/Program Files/Autodesk/mentalrayForMaya2015/icons;C:/Program Files/Autodesk/Maya2015/plug-ins/substance/icons;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/icons",
"MAYA_PLUG_IN_PATH": "C:/Users/guido.pollini/Documents/maya/2015-x64/plug-ins;C:/Users/guido.pollini/Documents/maya/plug-ins;C:/Program Files/Autodesk/Maya2015/bin/plug-ins;C:/Program Files/Autodesk/Maya2015/plug-ins/bifrost/plug-ins;C:/ExocortexAlembic/Maya2015/Module/plug-ins;C:/Program Files/Autodesk/Maya2015/plug-ins/fbx/plug-ins;C:/Program Files/Autodesk/mentalrayForMaya2015/plug-ins;C:/Program Files/Autodesk/Maya2015/plug-ins/substance/plug-ins;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/plug-ins",
"PATH": "C:/Program Files/Autodesk/Maya2015/bin/Cg;C:/Program Files/Autodesk/Maya2015/bin;C:/windows/system32;C:/windows;C:/windows/System32/Wbem;C:/windows/System32/WindowsPowerShell/v1.0/;C:/Program Files/Puppet Labs/Puppet/bin;C:/Program Files/Common Files/Autodesk Shared/;C:/Program Files (x86)/Autodesk/Backburner/;C:/Program Files (x86)/QuickTime/QTSystem/;C:/Program Files/TortoiseGit/bin;C:/Program Files (x86)/Skype/Phone/;C:/windows/system32/config/systemprofile/.dnx/bin;C:/Program Files/Microsoft DNX/Dnvm/;C:/Program Files/Microsoft SQL Server/130/Tools/Binn/;C:/Program Files/Microsoft SQL Server/120/Tools/Binn/;C:/Program Files (x86)/Windows Kits/10/Windows Performance Toolkit/;C:/Program Files/Microsoft SQL Server/110/Tools/Binn/;C:/Program Files (x86)/Microsoft SDKs/TypeScript/1.0/;C:/Users/guido.pollini/AppData/Local/Google/Chrome/Application;C:/windows/system32;C:/windows;C:/windows/System32/Wbem;C:/windows/System32/WindowsPowerShell/v1.0/;C:/Program Files/Puppet Labs/Puppet/bin;C:/Program Files/Common Files/Autodesk Shared/;C:/Program Files (x86)/Autodesk/Backburner/;C:/Program Files (x86)/QuickTime/QTSystem/;C:/wamp/bin/php/php5.6.15;C:/Program Files/Autodesk/Maya2015/plug-ins/bifrost/bin;C:/Program Files/Autodesk/mentalrayForMaya2015/bin;C:/Program Files/Autodesk/Maya2015/plug-ins/substance/bin;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/bin",
"MAYA_SCRIPT_PATH": "Y:/01_SAISON_4/09_EPISODES/04_Fabrication_3D/YKR400/sh004/lay/maya/work/scripts;C:/Users/guido.pollini/Documents/maya/2015-x64/scripts;C:/Users/guido.pollini/Documents/maya/scripts;C:/Users/guido.pollini/Documents/maya/2015-x64/presets;C:/Users/guido.pollini/Documents/maya/2015-x64/prefs/shelves;C:/Users/guido.pollini/Documents/maya/2015-x64/prefs/markingMenus;C:/Users/guido.pollini/Documents/maya/2015-x64/prefs/scripts;C:/Program Files/Autodesk/Maya2015/scripts;C:/Program Files/Autodesk/Maya2015/scripts/startup;C:/Program Files/Autodesk/Maya2015/scripts/others;C:/Program Files/Autodesk/Maya2015/scripts/AETemplates;C:/Program Files/Autodesk/Maya2015/scripts/unsupported;C:/Program Files/Autodesk/Maya2015/scripts/paintEffects;C:/Program Files/Autodesk/Maya2015/scripts/fluidEffects;C:/Program Files/Autodesk/Maya2015/scripts/hair;C:/Program Files/Autodesk/Maya2015/scripts/cloth;C:/Program Files/Autodesk/Maya2015/scripts/live;C:/Program Files/Autodesk/Maya2015/scripts/fur;C:/Program Files/Autodesk/Maya2015/scripts/muscle;C:/Program Files/Autodesk/Maya2015/scripts/turtle;C:/Program Files/Autodesk/Maya2015/scripts/FBX;C:/Program Files/Autodesk/Maya2015/scripts/mayaHIK;C:/Program Files/Autodesk/Maya2015/plug-ins/bifrost/scripts/presets;C:/Program Files/Autodesk/Maya2015/plug-ins/bifrost/scripts;C:/ExocortexAlembic/Maya2015/Module/scripts;C:/Program Files/Autodesk/Maya2015/plug-ins/fbx/scripts;C:/Program Files/Autodesk/mentalrayForMaya2015/scripts/AETemplates;C:/Program Files/Autodesk/mentalrayForMaya2015/scripts/mentalray;C:/Program Files/Autodesk/mentalrayForMaya2015/scripts/unsupported;C:/Program Files/Autodesk/mentalrayForMaya2015/scripts;C:/Program Files/Autodesk/Maya2015/plug-ins/substance/scripts;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/cafm;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/xmaya;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/brushes;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/dialogs;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/fxmodules;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/tabs;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/util;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/widgets;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts",
"MAYA_PLUG_IN_RESOURCE_PATH": "C:/Program Files/Autodesk/Maya2015/plug-ins/bifrost/resources;C:/ExocortexAlembic/Maya2015/Module/resources;C:/Program Files/Autodesk/Maya2015/plug-ins/fbx/resources;C:/Program Files/Autodesk/mentalrayForMaya2015/resources;C:/Program Files/Autodesk/Maya2015/plug-ins/substance/resources;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/resources"
}
for var in modifiedVars:
    actualEnv[var] = modifiedVars[var]

actualEnv["PROD_SERVER"] = "Y:"    




# Path to Toonkit's plug-ins
userName = getpass.getuser()
actualEnv["MAYA_PLUG_IN_PATH"] += ";C:/Users/" + userName + "/Documents/WKG_Yakari/Toonkit_Module/Maya2015/plug-ins"





# OBSCENE... replace "guido.pollini" with the local userName
for var in modifiedVars:
    modifiedVars[var] = modifiedVars[var].replace("guido.pollini", userName)




# If the server is on the WKG_Yakari, apparently the userSetup.py is automatically invoked... why?
mayapyProcess = subprocess.Popen("mayapy.exe  \"Y:/01_SAISON_4/05_UTILE/Rendu/13_REMOTE_MAYA/remoteMaya_server.py\"", env=actualEnv)
# .Popen(... ) --> <Popen>
# To kill it, use .terminate()





if MC.window("waitUI_WIN", ex=1):
    MC.deleteUI("waitUI_WIN") 
MC.window("waitUI_WIN", t="PLEASE WAIT", tlb=1, s=0, mb=0)
MC.columnLayout()
MC.text(l="Please wait...", h=100, w=100, bgc=(1, 0, 0))
MC.showWindow("waitUI_WIN")
#remoteMayaUI()





t = os.path.getmtime(__file__) # Seconds passed between Epoch and last modification 
formattedTime = time.strftime("%d/%m/%y, %H:%M:%S", time.localtime(t))
print '[{0}] loaded (last update {1})'.format(__name__, formattedTime)









""" EXOSHIT """
#MC.file("Y:/01_SAISON_4/09_EPISODES/04_Fabrication_3D/YKR407/sh043/lit/maya/YKR407_043_lit.ma", f=True, options="v=0;", ignoreVersion=True, typ="mayaAscii", o=True)
#exoCommand = "in=101;out=318;step=1;substep=1;filename=C:/Users/guido.pollini/Desktop/exportProva.abc;objects=ch_litth:body;ogawa=1;purepointcache=1;dynamictopology=0;normals=0;uvs=0;facesets=0;globalspace=0;withouthierarchy=0;transformcache=0"
#MC.ExocortexAlembic_export(j=exoCommand)