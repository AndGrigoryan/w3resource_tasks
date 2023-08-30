#!/usr/bin/env python3

#---------------------------------------------------------------------------------------------
#
#   Write a Python program to add 'ing' at the end of a given string (length should be at least 3). #   If the given string already ends with 'ing', add 'ly' instead.
#   If the string length of the given string is less than 3, leave it unchanged.
#   
#   Sample String : 'abc'
#   Expected Result : 'abcing'
#   Sample String : 'string'
#   Expected Result : 'stringly'
#
#
#---------------------------------------------------------------------------------------------

mstr = input("Inpur a string: ")

if len(mstr) >= 3:
    if not mstr.endswith('ing'):
        mstr += 'ing'
    else:
        mstr += 'ly'
print(mstr)

