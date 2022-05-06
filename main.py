#!/bin/env python3

# Python Libraries
import argparse
import os

attack_list = ['weakprimes', 'e1', 'e3', 'commonfactor']

# Arguments 
parser = argparse.ArgumentParser()

parser.add_argument('-modulus', metavar='', nargs='?',  const=1, type=int, 
      help='Enter the modulus (p * q), (default = 1)')

parser.add_argument('-n1', metavar='', type=int,  
      help='Enter the n1, for attack : commonfactor')

parser.add_argument('-n2', metavar='', type=int,  
      help='Enter the n2, for attack : commonfactor')

parser.add_argument('-e', metavar='', nargs='?', const=65537, type=int, 
      help='Enter the public exponent (default = 65537)')

parser.add_argument('-cipher', metavar='', nargs='?', const=1, type=int,  
      help='Enter the ciphertext (default = 0)')

parser.add_argument('-c1', metavar='', type=int,  
      help='Enter the c1, for attack : commonfactor')

parser.add_argument('-c2', metavar='', nargs='?', const=1, type=int,  
      help='Enter the c2, for attack : commonfactor')

parser.add_argument('--attack', metavar='',default='all',  
      help=f'Enter the attack name {set([i for i in attack_list])}')


args = parser.parse_args()
argv = vars(args)

# Attacks library
from RSAScan import RSAScan

# Attack 1 : weakprimes
if argv['attack'] == 'weakprimes':
	print('Trying for weakprimes attack.....!!')
	print('Results of weakprime attack : ', RSAScan.weakprimes(n,c,e))

# Attack 2 : small exponent	
if argv['attack'] == 'e1':
	print('Trying for e1 attack......!!')
	print('Results : ', RSAScan.e1(c))

# Attack 3 : cube root
if argv['attack'] == 'e3':
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

