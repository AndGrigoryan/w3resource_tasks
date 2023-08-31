#!/usr/bin/env python3

#---------------------------------------------------------------------------------
#
#   Write a Python program to clone or copy a list
#
#---------------------------------------------------------------------------------

ls = [int(i) for i in input("Input items of list: ").split()]
newls = ls.copy()

print(ls)
print(newls)


