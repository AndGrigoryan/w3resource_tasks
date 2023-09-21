#!/usr/bin/env python3

#------------------------------------------------------------------------
#
#   Write a Python program to find the second largest number in a list.
#
#------------------------------------------------------------------------

ls = [int(i) for i in input("Input a items of list: ").split()]

ls.sort()
print(ls[-2])

