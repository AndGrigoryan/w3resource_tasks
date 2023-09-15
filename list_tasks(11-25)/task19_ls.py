#!/usr/bin/env python3

#---------------------------------------------------------------------------------
#
#   Write a Python program to calculate the difference between the two lists.
#
#---------------------------------------------------------------------------------

ls1 = list(int(i) for i in input("Enter items of list: ").split())
ls2 = list(int(i) for i in input("Enter items of list: ").split())

newls = [i for i in ls1 if i not in ls2]
newls.extend(i for i in ls2 if i not in ls1)

print(newls)

