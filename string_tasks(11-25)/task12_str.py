#!/usr/bin/env python3

#---------------------------------------------------------------------------------------------
#
#   Write a Python program to count the occurrences of each word in a given sentence.
#
#
#---------------------------------------------------------------------------------------------

mstr = input("Enter a string: ").split()
md = {}

for el in mstr:
    el = el.lower()
    if el in md:
        md[el] += 1
    else:
        md[el] = 1


print(md)

