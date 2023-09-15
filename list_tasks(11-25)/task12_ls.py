#!/usr/bin/env python3

#---------------------------------------------------------------------------------
#   Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
#   Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#   Expected Output : ['Green', 'White', 'Black']
#
#
#---------------------------------------------------------------------------------

ls = input("Enter items of list: ").split()
ls = [ls[i] for i in range(len(ls)) if i not in [0, 4, 5]]

print(ls)

