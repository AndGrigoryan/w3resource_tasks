#!/usr/bin/env python3

#---------------------------------------------------------------------------------------------
#
#    Write a Python program to get a string from a given string where all occurrences of its
#   first char have been changed to '$', except the first char itself.
#   
#   Sample String : 'restart'
#   Expected Result : 'resta$t'
#
#
#---------------------------------------------------------------------------------------------

mstr = input("Please enter a string: ")

first_symbol = mstr[0]

for i in range(1, len(mstr)):
    if mstr[i] == first_symbol:
        mstr = mstr[:i] + "$" + mstr[i+1:]
print(mstr)

