#!/usr/bin/env python3

#---------------------------------------------------------------------------------
#
#   Write a Python program to check if a list is empty or not.
#
#---------------------------------------------------------------------------------

ls = [int(i) for i in input("Input items of list: ").split()]

if len(ls) == 0:
    print("List is empty.")
else:
    print("List isn't empty.")

