#!/bin/env python3

# Python Libraries
from Crypto.Util.number import long_to_bytes	

#####################################
#			Attack Libraries     	#
#####################################
from attacks.weakprimes import factorize # weakprimes Library
from attacks.e1e3 import e1 #e1 attack Library
from attacks.e1e3 import e3
from attacks.commonFactor import commonfactor #common factor Library
from attacks.commonmodulus import common_modulus
from attacks.wiener import wiener


def solve(e,n,p,q,c):
	assert p * q == n
	phi = (p-1) * (q-1)
	d = pow(e,-1,phi)
	intmsg = pow(c,d,n)
	msg = long_to_bytes(intmsg)
	return msg.decode()


class RSAScan:
	def weakprimes(n,c,e):
		primes = factorize(n)
		p,q = int(primes[0]), int(primes[1])
		return solve(e,n,p,q,c)

	def e1(c):
		msg = e1(c)
		return msg

	def e3(c):
		msg = e3(c)
		return msg

	def commonfactor(n1,n2,c1,c2,e):
		msg = commonfactor(n1,n2,c1,c2,e)
		return msg

	def commonmodulus(e1,e2,n,c1,c2):
		msg = common_modulus(e1,e2,n,c1,c2)
		return msg.decode()

	def wiener(e,n,c):
		d = wiener(e, n)
		msg = long_to_bytes(pow(c, d, n))
		return msg.decode()



