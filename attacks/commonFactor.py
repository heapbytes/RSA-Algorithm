#!/bin/env python3

from Crypto.Util.number import long_to_bytes, GCD

def commonfactor(n1,n2,c1,c2,e):
	p = GCD(n1,n2)
	q = n1 // p
	r = n2 // p
	phi = (p-1) * (q-1)
	phi2 = (p-1) * (r-1)
	d1 = pow(e,-1,phi)
	d2 = pow(e,-1,phi2)
	
	msg1 = long_to_bytes( pow(c1,d1,n1) ).decode()
	msg2 = long_to_bytes( pow(c2,d2,n2) ).decode()
	msg = msg1 + msg2
	return msg 
