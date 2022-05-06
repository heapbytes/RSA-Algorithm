#!/bin/env python3 

from Crypto.Util.number import long_to_bytes
from gmpy2 import iroot

def e1(c):
	return long_to_bytes(c).decode()
	
def e3(c):
	ct = iroot(c,3)
	return long_to_bytes(ct[0]).decode()


	
