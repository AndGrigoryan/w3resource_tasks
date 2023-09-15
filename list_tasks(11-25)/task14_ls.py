#!/usr/bin/env python3

#--------------------------------------------------------------------------------------------------------
#
#   Write a Python program to print the numbers of a specified list after removing even numbers from it.
#
#--------------------------------------------------------------------------------------------------------

ls = list(int(i) for i in input("Enter items of list: ").split())

i = 0
while i < len(ls):
    if ls[i] % 2 == 0:
       ls.pop(i)
    else:
        i += 1

print(*ls)

