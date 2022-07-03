#!/bin/env python3
import crypt

password = input("Enter password to hash => ")
print(crypt.crypt(str(password), crypt.mksalt(crypt.METHOD_SHA512)))
