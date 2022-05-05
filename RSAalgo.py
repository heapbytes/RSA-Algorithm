#!/bin/env python3

# Python Libraries
from Crypto.Util.number import long_to_bytes, bytes_to_long, GCD
from pwn import *
from gmpy2 import get_context
from gmpy2 import sqrt, iroot

# Configurations
get_context().precision=2048

def solve(e,n,p,q,c):
    assert p * q == n
    phi = (p-1) * (q-1)
    d = pow(e,-1,phi)
    intmsg = pow(c,d,n)
    msg = long_to_bytes(intmsg)
    return msg.decode()

''' attack demo
n = 1004995496566346075873930707800493321236968239524622949507762127653
c = 391954716711415946350985916860618751332906967581871181532410342734
e = 65537
'''

# Attack - 1 : weakprimes
from attacks import weakprimes
primes = weakprimes.weakprimes(n)
p,q = int(primes[0]), int(primes[1])
print(solve(e,n,p,q,c))

