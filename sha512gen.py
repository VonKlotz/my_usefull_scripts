#!/bin/env python3
import crypt

password = input("Enter password to hash => ")
print(crypt.crypt(str(password), crypt.mksalt(crypt.METHOD_SHA512)))




'''
old overcomplicated version version with args
import crypt
import argparse

parser = argparse.ArgumentParser(description='A SHA512 password hasher.')
parser.add_argument("-p", "--password", help="Prints the supplied argument.", nargs='*')
arguments = parser.parse_args()
pstr = arguments.password 

print(str(pstr))

print(crypt.crypt(str(pstr), crypt.mksalt(crypt.METHOD_SHA512)))



'''