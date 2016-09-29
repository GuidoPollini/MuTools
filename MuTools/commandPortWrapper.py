import maya.cmds as MC
import maya.mel  as MM

import __main__ # To access the 'singletons' (it's the interpreter module/namespace)
import socket





"""
__main__

This module represents the (otherwise anonymous) scope in which the interpreter's
main program executes - commands read either from standard input, from a script 
file, or from an interactive prompt. It is this environment in which the idiomatic 
'conditional script' stanza causes a script to run:
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

    def __new__(cls, internalPortId=1000):        
        if hasattr(__main__, CommandPort._singletonName):
            # print 'Singleton already existing'
            return getattr(__main__, CommandPort._singletonName)

        else:
            # Create a new object...
            commandPortInstance = super(CommandPort, cls).__new__(cls)
            # ... and make it interprer-level global (__main__)
            setattr(__main__, CommandPort._singletonName, commandPortInstance)

            # Open physically Maya port
            commandPortInstance._openPort(internalPortId)

            return commandPortInstance



    def __init__(self, internalPortId=1000):
        pass



    def __repr__(self):
        repres = "'Port:{0}'<CommandPort>".format(self.getId())
        return repres



    def _openPort(self, internalPortId=1000):
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
            # 'commandPort' uses the eventLoop which is disabled during scripts: hence force a refresh!
            MC.refresh()
     
        MC.commandPort(name=internalPortName, echoOutput=False, noreturn=False,
                       prefix='_commandPort_melCallback', returnNumCommands=True)

        self.internalPortId = internalPortId



    def getId(self):
        return self.internalPortId
    


    def _messageReceived(self, message):
        # Indirectly called when this commandPort receive a message
        print '-->', message, '(Actual namespace: {})'.format(__name__)



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

