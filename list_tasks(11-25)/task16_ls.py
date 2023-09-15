#!/usr/bin/env python3

#---------------------------------------------------------------------------------
#
#   Write a Python program to generate and print a list of the first and last 5 
#   elements where the values are square numbers between 1 and 30 (both included).
#
#---------------------------------------------------------------------------------

ls = list(i ** 2 for i in range(1, 21))


print(ls[:5])
print(ls[-5:])

