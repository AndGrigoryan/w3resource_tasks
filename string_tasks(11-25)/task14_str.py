#!/usr/bin/env python3

#---------------------------------------------------------------------------------------------
#
#   Write a Python program that accepts a comma-separated sequence of words as input and 
#   prints the distinct words in sorted form (alphanumerically).
#   Sample Words : red, white, black, red, green, black
#   Expected Result : black, green, red, white
#
#---------------------------------------------------------------------------------------------

mstr = input("Write the words separated by commas: ")

mstr = ','.join(sorted(list(set(mstr.split(',')))))

print(mstr)


