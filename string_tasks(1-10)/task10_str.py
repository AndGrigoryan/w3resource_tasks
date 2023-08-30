#!/usr/bin/env python3

#---------------------------------------------------------------------------------------------
#
#    Write a Python program to change a given string to a newly string
#    where the first and last chars have been exchanged.
#
#---------------------------------------------------------------------------------------------

mstr = input("Enter a string: ")

mstr = mstr[-1] + mstr[1:-1] + mstr[0]
print(mstr)

