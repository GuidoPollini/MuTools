import os
from cgm.core.lib.zoo.path import Path
""" From http://stackoverflow.com/questions/1057431/loading-all-modules-in-a-folder-in-python"""


def returnPyFilesFromFolder():
    import os
    thisFile = Path( __file__ )
    thisPath = thisFile.up()


    bufferList = find_files(thisPath, '*.py')
    returnList = []

    for file in bufferList:
	if '__' not in file:
	    splitBuffer = file.split('.')
	    returnList.append(splitBuffer[0])               
    if returnList:
	return returnList
    else:
	return False

def find_files(base, pattern):
    import fnmatch
    import os

    '''Return list of files matching pattern in base folder.'''
    """ http://stackoverflow.com/questions/4296138/use-wildcard-with-os-path-isfile"""
    return [n for n in fnmatch.filter(os.listdir(base), pattern) if
            os.path.isfile(os.path.join(base, n))]

def returnFilesFromFolder(searchTerms = ['*.ma','*.mb']):
    import os
    thisFile = Path( __file__ )
    thisPath = thisFile.up()
    returnList = []
    for term in searchTerms:
	returnList.extend(find_files(thisPath, term))

    if returnList:
	return returnList
    else:
	return False

def returnMayaFilesFromFolder():
    return returnFilesFromFolder(['*.ma','*.mb','*.obj'])

def returnThisPath():
    import os
    thisFile = Path( __file__ )
    thisPath = thisFile.up()
    return thisPath

__all__ = returnPyFilesFromFolder()
__pathHere__ = returnThisPath()