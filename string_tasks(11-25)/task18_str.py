#!/usr/bin/env python3

#---------------------------------------------------------------------------------------------
#
#   Write a Python function to get a string made of the first three characters of a specified string. 
#   If the length of the string is less than 3, return the original string.
#   Sample function and result :
#   first_three('ipy') -> ipy
#   first_three('python') -> pyt
#
#
#---------------------------------------------------------------------------------------------

mstr = input("Enter a string: ")

if len(mstr) > 3:
    print(mstr[:3])
else:
    print(mstr)

