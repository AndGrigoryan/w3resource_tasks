#!/usr/bin/env python3

#---------------------------------------------------------------------------------
#
#    Write a Python program to access the index of a list.
#
#---------------------------------------------------------------------------------

ls = list(int(i) for i in input("Enter items of list: ").split())

for i in range(len(ls)):
    print(i, ls[i])

