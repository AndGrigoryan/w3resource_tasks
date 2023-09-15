#!/usr/bin/env python3

#---------------------------------------------------------------------------------
#
#    Write a Python program to generate all permutations of a list in Python.
#
#---------------------------------------------------------------------------------
from itertools import permutations

ls = list(int(i) for i in input("Enter items of list: ").split())

ls = list(permutations(ls, len(ls)))

print("List: ", ls)

