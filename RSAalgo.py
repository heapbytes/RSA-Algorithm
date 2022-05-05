#!/bin/env python3

# Python Libraries
from Crypto.Util.number import long_to_bytes, bytes_to_long, GCD
from pwn import *
from gmpy2 import get_context
from gmpy2 import sqrt, iroot
from os import system

# Configurations
get_context().precision=2048

# Sage solve by os library
#n = 1004995496566346075873930707800493321236968239524622949507762127653
n = 1211

print(system(f'./attacks/ecm2.sage {n}'))