#!/usr/bin/env python3

#------------------------------------------------------------------------
#
#   Write a Python program to get the frequency of elements in a list.
#
#------------------------------------------------------------------------

ls = input("Please input items of list: ").split()

md = {}

for i in ls:
    md[i] = md.get(i, 0) + 1

print(md)

