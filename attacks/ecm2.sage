#!/bin/env sage

import sys
from sage.all import Integer

n = sys.argv[1]

def solve(n):
	n = Integer(n)
	primes = ecm.factor(n)
	return primes[0], primes[1]




