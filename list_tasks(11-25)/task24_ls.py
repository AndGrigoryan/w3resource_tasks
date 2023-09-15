#!/usr/bin/env python3

#---------------------------------------------------------------------------------
#
#   Write a Python program to append a list to the second list.
#
#---------------------------------------------------------------------------------

ls1 = input("Enter items of list: ").split()
ls2 = input("Enter items of list: ").split()

ls1.extend(ls2)

print(ls1)

