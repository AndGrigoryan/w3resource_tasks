#!/usr/bin/env python3

#---------------------------------------------------------------------------------
#
#   Write a Python program to multiply all the items in a list. 
#
#---------------------------------------------------------------------------------ls

ls = [int(i) for i in input("Input items of list: ").split()]

p = 1
for i in ls:
    p *= i

print(p)


