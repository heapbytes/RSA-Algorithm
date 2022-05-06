#!/bin/env python3

# Python Libraries
from Crypto.Util.number import long_to_bytes, bytes_to_long, GCD
from pwn import *
from gmpy2 import get_context
from gmpy2 import sqrt, iroot

# Configurations
get_context().precision=2048

# Attack 1 library ( weakprimes )
from attacks import weakprimes

def solve(e,n,p,q,c):
	assert p * q == n
	phi = (p-1) * (q-1)
	d = pow(e,-1,phi)
	intmsg = pow(c,d,n)
	msg = long_to_bytes(intmsg)
	return msg.decode()

class RSAScan:

	def weakprimes(n,c,e):
		primes = weakprimes.weakprimes(n)
		p,q = int(primes[0]), int(primes[1])
		print(solve(e,n,p,q,c))

		
		
	
	
	
