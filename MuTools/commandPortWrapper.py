import maya.cmds as MC
import maya.mel  as MM

import __main__ # To access the 'singletons' (it's the interpreter module/namespace)
import socket





"""
__main__
This module represents the (otherwise anonymous) scope in which the interpreter's
main program executes - commands read either from standard input, from a script 
file, or from an interactive prompt.
"""

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
    

    _singletonName = 'commandPortSingleton'


    def __new__(cls, internalPortId=1000, pythonCallback=None):        
        if hasattr(__main__, CommandPort._singletonName):
            print 'SINGLETON EXISTS!'
            return getattr(__main__, CommandPort._singletonName)

        else:
            # Create a new virgin CommandPort object with object.__new__()...
            commandPortInstance = super(CommandPort, cls).__new__(cls)
            print 'SINGLETON CREATED!'
            # ... and make it interprer-level global (__main__)
            setattr(__main__, CommandPort._singletonName, commandPortInstance)

            # Open physically a Maya port and customize the object
            commandPortInstance._openPort(internalPortId, pythonCallback)

            return commandPortInstance



    @staticmethod
    def deleteSingleton():
        if hasattr(__main__, CommandPort._singletonName):
            print 'SINGLETON DELETED!'
            commandPortObj = getattr(__main__, CommandPort._singletonName)
            MC.commandPort(name=':' + str(commandPortObj.ID), close=True)
            MC.refresh()

            delattr(__main__, CommandPort._singletonName)



    def __init__(self, internalPortId=1000, pythonCallback=None):
        print '__init__'
        self.ID = internalPortId
        self.pythonCallback = pythonCallback



    def __repr__(self):
        repres = "'ID:{0}'<CommandPort>".format(self.getId())
        return repres



    #------------------------------------------------------------------
    # DYNAMIC CALLBACKS
    # no need to close and reeopen the commandPort
    #------------------------------------------------------------------
    """

    def setCallback(self, pythonCallback):
        # It works:)
        self._pythonCallback = pythonCallback 
    
    def disableCallback(self):
        pass

    def enableCallback(self):
        pass    

    """
    #------------------------------------------------------------------
    #------------------------------------------------------------------


    def _openPort(self, internalPortId=1000, pythonCallback=None):
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
        

        # If the port is already present, close it and rebuild; otherwise the callback won't change!
        internalPortName = ':' + str(internalPortId)

        if MC.commandPort(internalPortName, query=True):
            MC.commandPort(name=internalPortName, close=True)
            print 'commandPort ' + str(internalPortName) + 'closed!'
            # 'commandPort' uses the eventLoop which is disabled during scripts: hence force a refresh!
            MC.refresh()
     
        MC.commandPort(name=internalPortName, 
                       prefix='_commandPort_melCallback',
                       echoOutput=False, 
                       noreturn=False,
                       returnNumCommands=True)
        print 'PORT OPEN!'
        self.internalPortId = internalPortId



    def getId(self):
        return self.internalPortId
    


    def _messageReceived(self, message):
        # Indirectly called when this commandPort receive a message
        # With this you can change, enable, disable in dynamically!
        if self.pythonCallback:
            self.pythonCallback(message)
        else:
            print 'NO CALLBACK SET'    
        
        #print '-->', message, '(Actual namespace: {})'.format(__name__)



    def sendMessage(self, externalPortId=2000, message=''):
        """
        This has nothing to do with the 'commandPort'; it's just here for convenience
        """
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            mySocket.connect(('127.0.0.1', externalPortId))
        except Exception as exc:
            raise LostConnection(exc)
        mySocket.send(message)
        mySocket.close()

