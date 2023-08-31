#!/usr/bin/env python3

#-------------------------------------------------------------------------------
#
#   Write a Python program to remove duplicates from a list.
#
#-------------------------------------------------------------------------------

ls = [int(i) for i in input("Please input items of list: ").split()]
tmp = []

for i in ls:
    if i not in tmp:
        tmp.append(i)
ls = tmp.copy()
print(ls)

