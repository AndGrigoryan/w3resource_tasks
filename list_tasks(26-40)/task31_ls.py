#!/usr/bin/env python3

#------------------------------------------------------------------------------------------------
#
#   Write a Python program to count the number of elements in a list within a specified range.
#
#------------------------------------------------------------------------------------------------

ls = input("Input a items of list: ").split()
start, end = int(input("start: ")), int(input("end: "))
md = {}

for i in range(start, end):
    md[ls[i]] = md.get(ls[i], 0) + 1

print(md)

