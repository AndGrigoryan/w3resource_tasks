#!/usr/bin/env python3

#------------------------------------------------------------------------
#
#   Write a Python program to get unique values from a list.
#
#------------------------------------------------------------------------

ls = [int(i) for i in input("Input a items of list: ").split()]

ls = list(set(ls))
print(ls)

