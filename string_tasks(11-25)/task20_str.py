#!/usr/bin/env python3

#---------------------------------------------------------------------------------------------
#
# Write a Python function to reverse a string if its length is a multiple of 4.
#
#---------------------------------------------------------------------------------------------

mstr = input("Enter a string: ")

if len(mstr) % 4 == 0:
    mstr = mstr[::-1]

print(mstr)


