#!/bin/env python3

# Python Libraries
import argparse
import os

attack_list = ['weakprimes', 'e1', 'e3', 'commonfactor']

# Arguments 
parser = argparse.ArgumentParser()

parser.add_argument('-n', metavar='', nargs='?',  const=1, type=int, 
      help='Enter the modulus (p * q), (default = 1)')

parser.add_argument('-e', metavar='', nargs='?', const=65537, type=int, 
      help='Enter the public exponent (default = 65537)')

parser.add_argument('-c', metavar='', nargs='?', const=1, type=int,  
      help='Enter the ciphertext (default = 0)')

parser.add_argument('--attack', metavar='',default='all',  
      help=f'Enter the attack name {set([i for i in attack_list])}')


args = parser.parse_args()
argv = vars(args)

if not argv['n']:
	print('Enter the modulus with -n <number>')
	parser.parse_args(['--help'])
else:
	n = argv['n']

if not argv['e']:
	print('Enter the exponent with -e <number>')
	parser.parse_args(['--help'])
else:
  	e = argv['e']

if not argv['c']:
	print('Enter the ciphertext with -c <number>')
	parser.parse_args(['--help'])
else:
	c = argv['c']

# Attacks library
from RSAScan import RSAScan

# Attack - 1 : weakprimes
if argv['attack'] == 'weakprimes':
	print('Trying for weakprimes attack.....!!')
	print('Results of weakprime attack : ', RSAScan.weakprimes(n,c,e))
	
if argv['attack'] == 'e1':
	print('Trying for e1 attack......!!')
	print('Results : ', RSAScan.e1(c))

if argv['attack'] == 'e3':
	print('Trying for cube root attack......!!')
	print('Results : ', RSAScan.e3(c))


