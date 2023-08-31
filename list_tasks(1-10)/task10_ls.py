#!/usr/bin/env python3

#---------------------------------------------------------------------------------
#
#   Write a Python program to find the list of words that are longer than n from a given list of words
#
#---------------------------------------------------------------------------------

ls = input("Enter items of list: ").split()
n = int(input("n: "))
newls = []

for i in ls:
    if len(i) > n:
        newls.append(i)

print(newls)

