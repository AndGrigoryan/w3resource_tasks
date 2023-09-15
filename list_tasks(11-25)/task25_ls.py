#!/usr/bin/env python3

#---------------------------------------------------------------------------------
#
#   Write a Python program to select an item randomly from a list.
#
#---------------------------------------------------------------------------------
from random import randrange

ls = input("Enter items of list: ").split()

print(ls[randrange(len(ls))])

