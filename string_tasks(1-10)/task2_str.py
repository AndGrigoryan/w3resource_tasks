#!/usr/bin/env python3

#---------------------------------------------------------------------------------------------
#
# Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
#
#---------------------------------------------------------------------------------------------

mstr = input("Enter a string: ")
d = {}

for i in mstr:
    d[i] = mstr.count(i)

print(d)

