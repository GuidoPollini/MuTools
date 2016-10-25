#import sys
#sys.__stdout__.write('\n?\n? WEIRD: MuTools\' __init__ is called indirectly by an inner import like "import MuTools.MuUtils"...\nand the imported objects live in the "MuTools" namespace...?\n?')



"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
  _                           _              
 | |                         (_)             
 | |     ___  __ _ _ __ _ __  _ _ __   __ _  
 | |    / _ \/ _` | '__| '_ \| | '_ \ / _` | 
 | |___|  __/ (_| | |  | | | | | | | | (_| | 
 |______\___|\__,_|_|  |_| |_|_|_| |_|\__, | 
                                       __/ | 
                                      |___/  

* BINDING BETWEEN NAMES AND OBJECTS (not assignment/mutation)
* PASSING BY OBJECT SHARING 
* MUTATION is related to what you can see of the object (ex 'immutable' objects which have a cache...)
  and it depends on which methods it gives you to detect alteration!
  Of course there's no way to check for the MUTABILITY of an object in Python!!!
---------------------------------------------------------------------------------------------------------------




---------------------------------------------------------------------------------------------------------------
STATIC CLASS OBJECTS
---------------------------------------------------------------------------------------------------------------


THIS ONE WILL FAIL
------------------

  class Log(object):
    STANDARD   = 0
    def __init__(self, globalLogId=None, verbosity=Log.STANDARD):
      self.verbosity = verbosity

The default agrument is evaluated during the building of the class object, which doesn't exist yet. 
Log doesnt' exist there      



THIS ONE IS PROPER
------------------

  class Log(object):
    STANDARD   = 0
    def __init__(self, globalLogId=None, verbosity=None):
      self.verbosity = verbosity or Log.STANDARD

When __init__ is called, Log exists and you have access to its 'members'

















PYTHON PASSES ARGUMENT 'BY OBJECT SHARING', ALWAYS!

--> all object arguments are passed by 'object sharing' (no exception)
    (There ain't two 'differents ways', one for mutables one for immutables)
    IT'S EXACTLY THE SAME!

--> the statement '='' is BINDING, never mutation! 

--> an object is IMMUTABLE when its methods can't alter self (in any noticeable way)
    and hence returns a NEW object... BUT IT'S NOT MUTATION!!!

--> KEY EXAMPLE:
      myStr = myStr.upper()
    - '.upper()' can't mutate 'myStr'; it doesn't modify 'self' and returns
      a new object of the required form;
    - 'myStr = ...' rebinds the NAME myStr to the new object returned by '.upper()'
    - the original object pointed by the old myStr is still alive and accessible
    - myStr now points TO A COMPLETE DIFFERENT OBJECT   

    ASSIGNMENT IS NOT MUTATION

>>>>>> In fact, forget about ASSIGNMENT: in Python it's BINDING <<<<<<

---------------------------------------------------------------------------------------------------------------
Strings are 'immutable'; it means that 'myString.upper()' won't mutate the data of the object myString, instead
will create a new object returned by the method

def myFunc(STR, LIST, OBJECT):
  STR = STR.upper()      --> NO MUTATION: rebinding to a new object
  LIST.append('shit')    --> MUTATION
  OBJECT.killYourself()  --> probably MUTATION


>>> Note that STR, LIST and OBJECT are passed exactly the same way: by object reference! <<<
What does the difference it's the MUTATION and REBINDING
 - string/numbers methods CANT MUTATE; they dont alter their selfs and return A NEW OBJECT
 - name = ...  is a BINDING, NOT AN ASSIGNMENT OR MUTATION














---------------------------------------------------------------------------------------------------------------
FUNCTION ARGUMENTS
---------------------------------------------------------------------------------------------------------------

                  POSITIONAL                KEYWORDED              EXTRA_POSITIONAL      EXTRA KEYWORDED
def FUNCTION(  a0, a1, ..., am,      k0=d0, k1=d1, ..., kn=dn,          *args,               **kwargs     ):...

When called with FUNCTION(PASSED_POSITIONAL, PASSED_KEYWORDED):
 - POSITIONAL is filled with the first items in PASSED_POSITIONAL, and what's left is put in EXTRA_POSITIONAL
 - each item of PASSED_KEYWORDED which is not in KEYWORDED is put in EXTRA_KEYWORDED

Put it simply: POSITIONAL and KEYWORDED rule; what's left goes into *args (list) or **kwargs (dict).
Note that the order here IS fundamental: *args and **kwargs must be the latter ones!


















---------------------------------------------------------------------------------------------------------------
Version 'MAJOR.MINOR.PATCH'
---------------------------------------------------------------------------------------------------------------

- 'PATCH' must be incremented if only backwards compatible bug fixes are 
  introduced. A bug fix is defined as an internal change that fixes incorrect 
  behavior.

- 'MINOR' must be incremented if new, backwards compatible functionality is 
  introduced to the public API. It MUST be incremented if any public API 
  functionality is marked as deprecated. It may be incremented if substantial
  new functionality or improvements are introduced within the private code. 
  It MAY include patch level changes. Patch version MUST be reset to 0 when 
  minor version is incremented.

- 'MAJOR' must be incremented if any backwards incompatible changes are 
  introduced to the public API. It MAY include minor and patch level changes.
  Patch and minor version MUST be reset to 0 when major version is 
  incremented.

-------------------------------------------------------------------------------

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""