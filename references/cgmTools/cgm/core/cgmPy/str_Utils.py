"""
str_Utils
Josh Burton (under the supervision of David Bokser:)
www.cgmonks.com
1/12/2011

Key:
1) Class - Limb
    Creates our rig objects
2)  


"""
# From Python =============================================================
import copy
import re

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

# From Maya =============================================================
import maya.cmds as mc
from maya import OpenMaya

# From Red9 =============================================================
from Red9.core import Red9_Meta as r9Meta

# From cgm ==============================================================
from cgm.core import cgm_General as cgmGeneral
from cgm.core.cgmPy import validateArgs as cgmValid
reload(cgmValid)

#>>> Utilities
#===================================================================
d_functionStringSwaps = {'.':'_attr_', ' ':'',',':'_',
                         '+':'_add_','-':'_minus_','><':'_avg_',#pma                                                 
                         '==':'_isEqualTo_','!=':'_isNotEqualTo_','>':'_isGreaterThan_','>=':'_isGreaterOrEqualTo_','<':'_isLessThan_','<=':'_isLessThanOrEqualTo_',#condition
                         '*':'_multBy_','/':'_divBy_','^':'_pow_',}#md

def stripInvalidChars(arg = None,invalidChars = """`~!@#$%^&*()-+=[]\\{}|;':"/?><., """,
                      functionSwap = True, replaceChar = '', cleanDoubles = True, stripTailing=True):
	"""
	Modified from Hamish MacKenzie's zoo one


	returns l_pos
	"""
	_str_funcName = 'stripInvalidChars'
	try:
		str_Clean = cgmValid.stringArg(arg,False,_str_funcName)
		
		for char in invalidChars:
			if functionSwap and char in d_functionStringSwaps.keys():
				str_Clean = str_Clean.replace( char, d_functionStringSwaps.get(char) )
			else:
				str_Clean = str_Clean.replace( char, replaceChar )
			
		for n in range(10):		
			while str_Clean.startswith( str(n) ):
				log.debug("Cleaning : %s"%str(n))
				str_Clean = str_Clean[ 1: ]	
				
		if cleanDoubles and replaceChar:
			doubleChar = replaceChar + replaceChar
			while doubleChar in cleanStr:
				str_Clean = str_Clean.replace( doubleChar, replaceChar )
				
		if stripTailing:
			while str_Clean.endswith( '_' ):
				str_Clean = str_Clean[ :-1 ]
		return str_Clean		
	except StandardError,error:
		raise StandardError,"%s >>> error : %s"%(_str_funcName,error)	
	
"""
				l_buffer = []
				for k in d_functionStringSwaps.keys():
					if k in buffer:
					for i,n in enumerate(buffer.split(' ')):
						for k in d_functionStringSwaps.keys():
						if n == k:n = d_functionStringSwaps[k]
						if '.' in n:
						n = '_'.join(n.split('.'))
						if ',' in n:
						n = '_'.join(n.split(','))
						if '-' in n:
						b = list(n)
						for p,k in enumerate(b):
							if k == '-':
							b[p]='_inv'				    
						n = ''.join(b)
						l_buffer.append(n)
					break	
"""