#!/bin/env python3 

from Crypto.Util.number import long_to_bytes
from gmpy2 import iroot

def e1(c):
	return long_to_bytes(c).decode()
	
def e3(c):
	ct = int(iroot(c, 3)[0])
	return long_to_bytes(ct).decode()

"""
example of e1 attack : ('modulus' is not mandatory)

python3 main.py -modulus -e 1 -cipher 53124518356512721168420607301391628917329020305637080636254611014908535338355 --attack e1


example of e3(cube_root) attack : ( 'modulus' is not mandatory )

python3 main.py -modulus -e 3 -cipher 873155658033286165345893055075219953448439133304998599826332294122364399613515391492517530741997313686269671365469457117326837553092248386584401016236110628510070270063568461732767950347057143066788600143225698168693961311821925168117751654884111332051719013 --attack e3

"""

	
