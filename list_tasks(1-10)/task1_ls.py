#!/usr/bin/env python3

#---------------------------------------------------------------------------------
#
#   Write a Python program to sum all the items in a list.
#
#---------------------------------------------------------------------------------

ls = list(int(i) for i in input("Enter items of list: ").split())
total = 0

for i in ls:
    total += i

print("Sum:", total)

