#!/usr/bin/env python3

#---------------------------------------------------------------------------------------------
#
#   Write a Python program to get a single string from two given strings, separated by a space 
#   and swap the first two characters of each string.
#   Sample String : 'abc', 'xyz'
#   Expected Result : 'xyc abz'
#
#---------------------------------------------------------------------------------------------

mstr1, mstr2 = input("Enter first string: "), input("Enter second string: ")

res = mstr2[:2] + mstr1[2:] + ' ' + mstr1[:2] + mstr2[2:]
print(res)

