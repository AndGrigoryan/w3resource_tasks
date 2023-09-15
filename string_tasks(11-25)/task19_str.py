#!/usr/bin/env python3

#---------------------------------------------------------------------------------------------
#
#   Write a Python program to get the last part of a string before a specified character.
#   https://www.w3resource.com/python-exercises
#   https://www.w3resource.com/python
#
#---------------------------------------------------------------------------------------------

mstr, symbol = input("Enter a string: "), input("Enter symbol: ")

if symbol in mstr:
    mstr = mstr[:mstr.rfind(symbol)]

print(mstr)

