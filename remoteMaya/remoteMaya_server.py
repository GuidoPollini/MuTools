#! /usr/bin/env python
# -*- coding: utf-8 -*-

#------------------------------------------------------------------------------------------
# remoteMaya_server
#------------------------------------------------------------------------------------------

import socket
def sendMessage(message):
    #print "sending'" + message + "'..."
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 7777))
    
    #client.send("remoteMaya_client.mayaClient.receiveFromServer('" + message + "')")
    # This one would fail: exec is executed in teh namespace of its module, which
    # is already 'remoteMaya_client'...
    #client.send("mayaClient.receiveFromServer('" + message + "')")
    client.send(message)

    client.close()
    #print "sent:)"


print "Initializing:"
print " - loading [MayaCore]"

""" MAYA STANDALONE """
# Start Maya standalone
import maya.standalone       as SA
SA.initialize()



""" SERVER """
import socket                as SOCKET
import wsgiref.simple_server as SS



def commandHandler(environment, responseCallable):
    queryString = environment.get("QUERY_STRING")
    #
    # "     ==> %22
    # space ==> %20
    #
    receivedCommand = queryString.replace("%22", "\"")
    receivedCommand = receivedCommand.replace("%20", " ")

    try:
        print "\n\n\n--------------------------------------------------------------------------------Received command:", receivedCommand
        print "--------------------------------------------------------------------------------", 
        
        if 'MC.ls' in receivedCommand:
            stringResult = str(eval(receivedCommand))
            sendMessage(stringResult)
        else:    
            exec receivedCommand

        print "==> SUCCESS\n"

    except Exception as exc:
        print "==> ERROR", exc
        #responseCallable("200 OK", [("Content-type", "text/plain")])
        #return "ERROR: can't executr the following statement:" + receivedCommand + str(exc)

    finally:
        print "1111111"
        responseCallable("200 OK", [("Content-type", "text/plain")])
        print "2222222"
        return "fuckYou"
    """

    if not environment.get("QUERY_STRING"):
        responseCallable("404 Not Found", [("Content-type", "text/plain")])
        return "BAD"
    
    responseCallable("200 OK", [("Content-type", "text/plain")])
    
    if queryString == "quit":
        quit()
        return "... QUIT!"
    
    return "OK"
    """

localIP = SOCKET.gethostbyname(SOCKET.gethostname())
serverInstance = SS.make_server(localIP, 8000, commandHandler)


def quit():
    print "\n"    
    print "                  _ _   "
    print "       __ _ _   _(_) |_ "
    print "      / _` | | | | | __|"
    print "     | (_| | |_| | | |_ "
    print "      \__, |\__,_|_|\__|"
    print "         |_|            "
    
    MC.quit(force=True)

    # You need a separate thread to ask for ".shutdown()"
    import threading
    threading.Thread(target=serverInstance.shutdown).start()





# Now you can import...
print " - loading [commandEngine]"
import maya.cmds             as MC

print " - loading [ToonKitNodes]"
MC.loadPlugin("tkSoftIKNode.mll")
MC.loadPlugin("tkSpringNode.mll")

print " - loading [ExocortexAlembic]"
MC.loadPlugin("MayaExocortexAlembic.mll")

print " - loading [MentalRay]"
MC.loadPlugin("Mayatomr.mll", quiet=True)

# Without "poll_interval", it would be unstoppable

text = """                                  _                                     
         _ __ ___ _ __ ___   ___ | |_ ___   _ __ ___   __ _ _   _  __ _ 
        | '__/ _ \ '_ ` _ \ / _ \| __/ _ \ | '_ ` _ \ / _` | | | |/ _` |
        | | |  __/ | | | | | (_) | ||  __/ | | | | | | (_| | |_| | (_| |
        |_|  \___|_| |_| |_|\___/ \__\___| |_| |_| |_|\__,_|\__, |\__,_|
                                                            |___/ """      
print "--------------------------------------------------------------------------------"                                                        
print "\n"*6
print text 
print "\n"*5
print "--------------------------------------------------------------------------------"

print ("Ready to serve (local IP = " + (str(localIP) + ":8000") + ")").center(80),

try:
    # This will be 'exec'uted in the module 'remoteMaya_client', so non namespace needed!!!
    sendMessage("mayaClient.remoteMayaLoaded()")
except Exception as exc:
    print "FAILED", str(exc)

 

serverInstance.serve_forever(poll_interval=0.5)
