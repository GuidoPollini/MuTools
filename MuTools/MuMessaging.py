__version__ = '1.0.3'
print '--> Executing MuMessaging...'



import maya.cmds as MC
import maya.mel  as MM

import __main__ # To access the 'singletons'
import socket
import time


"""
===========================================================================================
===========================================================================================
Apparently, when Maya is busy there's a limit of 6 (SIX) messages that the open 
commandPort can queue; one more and the connection is lost...

There's a  way to continue using the commandPort system, but increase the 
'busyMaya's commandPort queue size?????
===========================================================================================
===========================================================================================
"""




def sendMessage(externalPortId, message):
    """
    Send a string message to an external port
    """
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        mySocket.connect(('127.0.0.1', externalPortId))

    except Exception as exc:
        raise LostConnection(exc)

    mySocket.send(message)
    mySocket.close()




class LostConnection(Exception):
    """
    Apparently, 'commandPort' can't detect when the connection was really lost or
    the 6 messages queue limit was reached.
    """
    def __init__(self, sourceException=None):
        # Save the original exception, for possible inspection
        self.sourceException = sourceException




class CommandPort(object):
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    SINGLETON (on __main__)

    First try to define a singleton object, i.e.: 
     - an object who lives in the __main__ namespace;
     - every module can access it;
     - it's a SHARED object (shared state, etcect)
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """
    Anywhere access to the singleton instance via __init__:
    - port = CP.CommandPort()
    It's a interpreter-level global object; passing via .CommandPort()
    allows to forget its global name!
    """
    
    print '==> EXEC <CommandPort> class code...'
    _singletonName      = 'commandPortSingleton'



    def __new__(cls, portId=None, callback=None):        
        if hasattr(__main__, CommandPort._singletonName):
            print 'SINGLETON EXISTS!'
            return getattr(__main__, CommandPort._singletonName)

        else:
            # Create a new virgin CommandPort object
            commandPortInstance = super(CommandPort, cls).__new__(cls)
            print 'SINGLETON CREATED!'

            # ... and make it interprer-level global (__main__)
            setattr(__main__, CommandPort._singletonName, commandPortInstance)

            # Open physically a Maya port and customize the object
            commandPortInstance._openPort(portId, callback)

            return commandPortInstance



    @staticmethod
    def microSleep(duration=0.01):
        # 'commandPort' works with the main eventLoop; when closing and opening
        # it needs a micro pause to refresh its internals!
        # - 0.01 works even when close/open are fired rapidly;
        # - 0.0001 fails
        time.sleep(duration)



    @staticmethod
    def deleteSingleton():
        if hasattr(__main__, CommandPort._singletonName):
            print 'SINGLETON DELETED!'
            commandPortObj = getattr(__main__, CommandPort._singletonName)

            MC.commandPort(name=':' + str(commandPortObj.portId()), close=True)
            CommandPort.microSleep()

            delattr(__main__, CommandPort._singletonName)



    def __init__(self, portId=1000, callback=None):
        print '__init__'
        self._portId          = portId
        self._callback        = callback
        self._callbackEnabled = True if callback else False



    def __repr__(self):
        return '"portId:{0}"<CommandPort>'.format(self.portId())



    def _openPort(self, portId=None, callback=None):
        singleton = getattr(__main__, CommandPort._singletonName)

        # The string in _singletonName is a __main__-name and Python called by MEL lives
        # in the interpreter namespace/module __main__; hence what follows is legal:
        '''
        global proc _commandPort_melCallback(string $arg){
            python("commandPortSingleton._messageReceived(\"" + $arg + "\")");
        }
        '''

        melCallbackWrapper = """
        global proc _commandPort_melCallback(string $arg){{
            python("{0}(\\"" + $arg + "\\")");
        }}
        """.format(CommandPort._singletonName + '._messageReceived')
        MM.eval(melCallbackWrapper)
        

        """ NO, THE CALLBACK IS NOW DYNAMIC """
        # If the port is already present, close it and rebuild; otherwise the callback won't change!
        portIdString = ':' + str(portId)

        if MC.commandPort(portIdString, query=True):
            MC.commandPort(name=portIdString, close=True)
            CommandPort.microSleep()

            print 'commandPort ' + str(portIdString) + 'closed!'


        MC.commandPort(name=portIdString, 
                       prefix='_commandPort_melCallback',
                       echoOutput=False, 
                       noreturn=False,
                       returnNumCommands=False)
        CommandPort.microSleep()


        print 'PORT OPEN!'
        self._portId = portId



    def portId(self):
        return self._portId
    


    def _messageReceived(self, message):
        # The official Python callback, hard-coded in the MEL callback
        # when the commandPort was open!
        #
        # The actual callback is the functionObject stored in self._callback
        # And can be dynamically changed/enabled/disabled!
        
        if self._callback and self._callbackEnabled:
            self._callback(message) 
        


    def setCallback(self, callback):
        # Dynamic callback (chosen at runTime)
        self._callback = callback 
    


    def enable(self):
        # Enable the commandPort by enabling its only callback
        self._callbackEnabled = True



    def disable(self):
        # Disable the commandPort by disabling its only callback
        self._callbackEnabled = False
        


 

