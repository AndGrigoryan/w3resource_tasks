#!/usr/bin/env python3

#---------------------------------------------------------------------------------------------
#
#    Write a Python program to remove the nth index character from a nonempty string.
#
#
#---------------------------------------------------------------------------------------------

mstr = input("Enter a string: ")
index = int(input("Write the index you want to delete: "))

mstr = mstr[:index] + mstr[index+1:]
print(mstr)


