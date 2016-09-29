import __main__

 
def singleton(cls):
    """
    Each class marked with the 'singleton' decorator will generate ONLY one 
    instance, located in __main__, named '_@@@Singleton' and hence visible
    to every module possible, no matter where!

    -> The original idea I found on internet used a 'closure' (here) to save the
       instance without using the interpreter module __main__. 
       But I had some problems with recursive reload on developing; the decorator
       was called multiple times and destroyed the singleton (it would have worked
       in production). 
       By using a __main__ level object you can recursively reload safely:)
       (In the end, I just replaced the closure holding the physical singleton with a
       	closure holding simply the name of the singleton in __main__... nothing more!)

    -> Caveat: when 'recursively reloading', check in __main__ for 'singleton' objects 
       and 'del' them: otherwise the singleton won't be updated!

    """
    
    # Ex: from class 'Fucker' to singleton name "_FuckerSingleton"
    # 'closure' for the class name, needed to recover the global object name:
    singletonName =  '_{}Singleton'.format(cls.__name__)
    
    # ??? A singleton should have a constructor with arguments? If called a second time as 
    # singleton with argument it should recreate it? Or simply a bare constructor and 
    # another '.initialize(*args, **kwargs)?'
    def _getInstance(*args, **kwargs):
        if not hasattr(__main__, singletonName):
            print 'Singleton of {0} named "{1}" created in __main__!'.format(cls, singletonName)
            setattr(__main__, singletonName, cls(*args, **kwargs))
        return getattr(__main__, singletonName)
    
    #getInstance.__name__ = cls.__name__
    
    # After applying the decorator, your class 'Fucker = singleton(Fucker)' become a function, 
    # '_getInstance(...)'; when you call 'Fucker(...)' in reality it calls '_getInstance(...)'
    # which in turn calls (if it's the first time) the constructor of the original 'Fucker'
    return _getInstance


@singleton
class Foo(object):
    def __init__(self, data=None):
    	print 'x'
        self.data = data
