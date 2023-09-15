#!/usr/bin/env python3

#---------------------------------------------------------------------------------------------
#
#   Write a Python program to remove a key from a dictionary.
#
#---------------------------------------------------------------------------------------------

md = {'a': 1, 'b': 2, 'c': 3}
k = input("Enter a key for remove: ")

if md.get(k, 0):
    md.pop(k)
else:
    print("Invalid key")

print(md)

