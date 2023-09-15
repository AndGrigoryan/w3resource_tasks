#!/usr/bin/env python3

#---------------------------------------------------------------------------------
#
#   Write a Python program to shuffle and print a specified list.
#
#---------------------------------------------------------------------------------

from random import shuffle

ls = input("Enter items of list: ").split()

shuffle(ls)

print(*ls)

