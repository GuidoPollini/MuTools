import maya.cmds as MC
import maya.mel  as MM

class LostConnection(Exception):
    def __init__(self, data=None):
        self.data = data
        print '[MESSAGE]', self.data

"""
When maya is busy, apparently the size of the queue is 6; 6 messages are acceptable, but
the 7th forces Maya to shut down the connection... I don't understant!
"""


internalPortId   = 1000
internalPortName = ':' + str(internalPortId)

externalPortId = 2000


def commandPort_callbackPython(message):
    print 'commandPort_callback:', message

melWrapper = """
    global proc commandPort_callbackMEL(string $arg){
        python("commandPort_callbackPython(\\"" + $arg + "\\")");
    }
"""



print melWrapper
MM.eval(melWrapper)

if MC.commandPort(internalPortName, query=True):
    MC.commandPort(name=internalPortName, close=True)
    # During a script the eventLoop is disabled and 'commandPort' works with the eventLoop;
    # Just force an eventLoop refresh!
    MC.refresh()
 
#MC.commandPort(name=internalPortName, echoOutput=False, noreturn=False,
#               prefix='commandPort_callbackMEL', returnNumCommands=True)
               
MC.commandPort(name=internalPortName, echoOutput=True, noreturn=True,
               returnNumCommands=True)


import socket
def sendMessage(portId, message):
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        mySocket.connect(('127.0.0.1', portId))
    except Exception as exc:
        raise LostConnection(exc)
    mySocket.send(message)
    mySocket.close()
    

sendMessage(externalPortId, 'FUCK YOU')

import time
time.sleep(10)

