import maya.OpenMaya as OM
def shit(myArg1, myArg2, myKwarg1='default1', myKwarg2='default2'):
    # The autoDoc script will check for exact coherente between 
    # *args and **kwargs and what's written in ARGUMENTS...
    # To parse arguments of ARGUMENTS you could use the indentation, 
    # without the need to add weird symbols.
    # 
    # TAGS
    #   <>        class
    #   *... *    bold
    #   **... **  superBold
    #   ???       hyperLink
    #   ???       italic
    #   ???       itemize

    """
    DESCRIPTION
      Description of what the method/function does...
      The spaces befote this ain't *relevants*!
        1: Magica lista che non so che
           cazzo significhi... fuck you;
        2: Ancora un altro item xxx;
        3: Non ne ho davvero idea
          
      Choose a symbol to mark args, kwargs end return (e.g. @)
    
    ARGUMENTS
      myArg1 <type1, type2, type3>
        Convenient way to write what needs
        to be written in the arguent
        
      myArg2 <type>
        Again you can put here all the shit you want
        without any limit
        
      myKwarg1='default1' <type>
        Porco dio e' sempre piu complicato
        
      myKwarg2='default2' <type>
        Ma alla fine ci riuscirai
        Abbi fiducia in te stesso, e' solo una
        transizione e stai costruendoti il tuo futuro
        
    RETURN
      <type>
      Scrivi qua tutto cio che ti pare tanto non fa nessuna
      differenrza. se lo trovi difficile e perche stai 
      creando qualcosa che ti garantira un lavoro futuro.
      E' inevitabile che sia difficile. ma stai andando bene 
    """
    
    print 12
    
    
print type(shit)
doc = shit.__doc__ 
# Get the lines (which have some content) with trailing spaces removed
doc = [y for y in [x.lstrip().rstrip() for x in doc.split('\n')] if y != '']
for x in doc:
    print x 
#-------------------------------------------------------------------------
""" even this is possible
l = List('guido', 'sei', 'grandissimo')
print l.upper()
-------------------------------------------------------------"""
class List(list):
    def __init__(self, *args):
        if len(args) == 1:
            super(List, self).__init__(args[0])
        else:    
            super(List, self).__init__(args)
    
    def __getattr__(self, attrName):
        print '__getattr__', attrName
        result = None
        try:
            result = [getattr(x, attrName) for x in self]
        except:
            print "fuck you"
        return List(result)        
        
    def __call__(self, *args, **kwargs):
            return List([x(*args, **kwargs) for x in self])
        




class CustomContext(object):
    def __init__(self, *args, **kwargs):
        # The only way a context can receive arguments
        pass
        
    def __enter__(self):
        # No accepted arguments here; hence if 'as' must return 
        # a specific object, the info passed to the initializer 
        # will have to be stored in self 
        pass
        
        # If necessary, return an object X to be exposed:
        # - with MyContext(... ) as X: ... 
        # You can return whatever you want, even nothing (i.e. None)!
        return self
        
    def __exit__(self, *args):
        # args holds the eventual exception data
        pass
        
        # At this point, no exception has been yet thrown:
        # - return True  --> the exception is swallowed
        # - return False --> reraised 
        """
        if args and args[0] is <someExceptiontype>:
            print 'shitty division'
            return True # Swallow it!
        """ 


""" [???] In PyMel usa una closure nel callback... percke??? """
def _nodeAddedCallback(mObj, clientData):
    # C++ callback signature:
    # - callbackName(MObject &node, void* clientData)
    
    ptr = OM.MFnDependencyNode(mObj)
    print ptr.name()

    
ID = OM.MDGMessage.addNodeAddedCallback(_nodeAddedCallback, 'dependNode')

"""    
OM.MMessage.removeCallback(ID)
"""

with NodeTracker() as nodeTracker:
    ...
    nodeTracker.createdNodes()
    nodeTracker.flush()
    
    
# Apparently, modules and classes are really singletons;
# except when you 'reload': this forces the recompiling
# of the code and the singletons are reinitialized.
#
# Except this minor detail, they're really singletons!
# (check their ids)
#
# When you reload, reload from the outer to the inner:
# ex:
"""
reload(MuTools.MuUtils)
reload(MuTools.MuCore)
reload(MuTools.MuScene)
reload(MuTools.MuUI)
reload(MuTools.MuMessaging)
# ...
reload(YourFuckingModule)
# etc...
"""

"""
Probably it's not a good idea making the CommandPort
as a singleton 'cause there could be interferences
between different scripts...
Just create for each script an instance (that will
be a singleton but ONLY for the script, as in a 
namespace system)
""" 