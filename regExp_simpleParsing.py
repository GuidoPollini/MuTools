import re
import maya.cmds as MC

filterExamples = [
    # Default
    'all',
    ' all  ',
    
    # After
    '>123_A',
    '  >   099_A ',

    # Before
    '<012_B',
    '   <  999_A  ',
    
    # Between
    '123_B-001',
    ' 099 -  012_C',
    
    # List (spaces)
    '999_B',
    '  000_M     ',
    '123 232 999_B 111 001_T',
    '   345     012_B      999',
    
    # List (commas)
    '123,999,123_B,012,009',
    '  123  232 , 999_B  111,   001_T',    
]

for filter in filterExamples:
    # Decompose the regExes in tokens... A LOT EASIER, to read and debug
    spaces   = '[ ]*'
    shotCode = '[0-9]{3}(_[a-zA-Z])?'

    # Default?
    # regExp = spaces + 'all' + spaces
    if re.search(r'^[ ]*all[ ]*$', filter):        
        print '"{0}" default'.format(filter)
        continue

    # After?
    # regExp = spaces + '>' + spaces + shotCode + spaces
    #  spaces    >    spaces     ###      _@ (if any)   spaces
    #   [ ]*     >     [ ]*   [0-9]{3}   (_[a-zA-Z])?    [ ]*
    elif ">" in filter:
        if re.search(r'^[ ]*>[ ]*[0-9]{3}(_[a-zA-Z])?[ ]*$', filter):
            print '"{0}" after OK'.format(filter)
            continue
        else:
            MC.error("BAD")

        
    # Before?
    # regExp = spaces + '<' + spaces + shotCode + spaces
    #  spaces    <    spaces     ###      _@ (if any)   spaces
    #   [ ]*     <     [ ]*   [0-9]{3}   (_[a-zA-Z])?    [ ]*    
    elif "<" in filter:
        if re.search(r'^[ ]*<[ ]*[0-9]{3}(_[a-zA-Z])?[ ]*$', filter):
            print '"{0}" before OK'.format(filter)
            continue
        else:
            MC.error('BAD')

    # Between?
    # regExp = spaces + shotCode + spaces + '-' + spaces + shotcode + spaces
    # spaces        shotCode         space    -   spaces       shotCode          spaces
    #  [ ]*    [0-9]{3}(_[a-zA-Z])?   [ ]*    -    [ ]*    [0-9]{3}(_[a-zA-Z])?   [ ]*
    elif "-" in filter:
        if re.search(r'^[ ]*[0-9]{3}(_[a-zA-Z])?[ ]*-[ ]*[0-9]{3}(_[a-zA-Z])?[ ]*$', filter):
            print '"{0}" betweek OK'.format(filter)
            continue
        else:
            MC.error('BAD')    
    
    # List?
    else:
        if re.search(r'^(?:[ ,]*[0-9]{3}(?:_[a-zA-Z])?[ ,]*)+$', filter):
            print '"{0}" list OK'.format(filter)
            # (?:  ) means a "non capturing" group... I.e. a siple "grouping"
            matches = re.findall(r'[0-9]{3}(?:_[a-zA-Z])?', filter)
            for match in matches:
                print "-->", match
            continue
        else:
            MC.error('BAD')     
    