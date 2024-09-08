#!/bin/env python3

# Python Libraries
import argparse
import os
import sys

attack_list = ['weakprimes', 'e1', 'e3', 'commonfactor', 'commonmodulus', 'wiener']

# Arguments 
parser = argparse.ArgumentParser()

parser.add_argument('-modulus', metavar='', nargs='?',  const=1, type=int, 
      help='Enter the modulus (p * q), (default = 1)')

parser.add_argument('-n1', metavar='', type=int,  
      help='Enter the n1, for attack : commonfactor and commonmodulus')

parser.add_argument('-n2', metavar='', type=int,  
      help='Enter the n2, for attack : commonfactor and commonmodulus')

parser.add_argument('-e', metavar='', nargs='?', const=65537, type=int, 
      help='Enter the public exponent (default = 65537)')

parser.add_argument('-cipher', metavar='', nargs='?', const=1, type=int,  
      help='Enter the ciphertext (default = 0)')

parser.add_argument('-c1', metavar='', type=int,  
      help='Enter the c1, for attack : commonfactor')

parser.add_argument('-c2', metavar='', type=int,  
      help='Enter the c2, for attack : commonfactor')

parser.add_argument('-e1', metavar='', type=int,  
      help='Enter the e1, for attack : commonmodulus')

parser.add_argument('-e2', metavar='',type=int,  
      help='Enter the e2, for attack : commonmodulus')

parser.add_argument('--attack', metavar='',default='all',  
      help=f'Enter the attack name {set([i for i in attack_list])}')


args = parser.parse_args()
argv = vars(args)

# Attacks library
from RSAScan import RSAScan
from banner import banner

if len(sys.argv) <= 1:
	b = banner()
	print(' Use -h for more information')
else:
	b = banner()

# Attack 1 : weakprimes
if argv['attack'] == 'weakprimes':
	c,n,e = argv['cipher'], argv['modulus'], argv['e']
	print('Trying for weakprimes attack.....!!')
	print('Results of weakprime attack : ', RSAScan.weakprimes(n,c,e))

# Attack 2 : small exponent	
if argv['attack'] == 'e1':
	c = argv['cipher']
	print('Trying for e1 attack......!!')
	print('Results : ', RSAScan.e1(c))

# Attack 3 : cube root
if argv['attack'] == 'e3':
	c = argv['cipher']
	print('Trying for cube root attack......!!')
	print('Results : ', RSAScan.e3(c))

# Attack 4 : commonfactor
if argv['attack'] == 'commonfactor':
	if argv['n1'] and argv['n2'] and argv['c1'] and argv['c2'] and argv['e']:
		n1, n2, c1, c2, e = argv['n1'], argv['n2'], argv['c1'], argv['c2'], argv['e']
		print('Trying for common factor attack......!!')
		print('Results : ', RSAScan.commonfactor(n1,n2,c1,c2,e))
	else:
		print('Parameters missing try using with all parameters n1,n2,c1,c2,e for common factor attack')

if argv['attack'] == 'commonmodulus':
    n, c1, c2, e1, e2 = argv['modulus'], argv['c1'], argv['c2'], argv['e1'], argv['e2']
    print('Trying for Common modulus attack..........!!')
    print('Results : ', RSAScan.commonmodulus(e1,e2,n,c1,c2))

if argv['attack'] == 'wiener':
	n, e, c = argv['modulus'], argv['e'], argv['cipher']
	print('Trying for wiener attack......!!')
	print('Results : ', RSAScan.wiener(e, n, c))


    
