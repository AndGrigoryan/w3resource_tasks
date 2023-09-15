#!/usr/bin/env python3

#---------------------------------------------------------------------------------------------
#
#   Write a Python function to convert a given string to all uppercase 
#   if it contains at least 2 uppercase characters in the first 4 characters.
#
#---------------------------------------------------------------------------------------------

mstr = input("Enter a string: ")

cnt = 0

for i in mstr[:4]:
    if i.isupper():
        cnt += 1

if cnt >= 2:
    mstr = mstr.upper()

print(mstr)

