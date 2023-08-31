#!/usr/bin/env python3

#---------------------------------------------------------------------------------
#
#   Write a Python program to get the largest number from a list.
#
#---------------------------------------------------------------------------------

ls = [int(i) for i in input("Input items of list: ").split()]

mx = ls[0]
for i in ls:
    if i > mx:
        mx = i
print(mx)

