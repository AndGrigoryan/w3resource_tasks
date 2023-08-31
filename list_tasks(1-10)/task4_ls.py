#!/usr/bin/env python3

#---------------------------------------------------------------------------------
#
#   Write a Python program to get the smallest number from a list.
#
#---------------------------------------------------------------------------------

ls = [int(i) for i in input("Please input items of list: ").split()]

mn = ls[0]

for i in ls:
    if i < mn:
        print(i)
        mn = i

print("The smallest number is: ", mn)
