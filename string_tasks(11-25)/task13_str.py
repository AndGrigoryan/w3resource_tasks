#!/usr/bin/env python3

#---------------------------------------------------------------------------------------------
#
# Write a Python script that takes input from the user and displays that input back in upper and lower cases.
#
#
#---------------------------------------------------------------------------------------------

mstr = input("Enter a string: ")

for i in range(len(mstr)):
    if mstr[i].islower():
        mstr = mstr[:i] + mstr[i].upper() + mstr[i+1:] 
    else:
        mstr = mstr[:i] + mstr[i].lower() + mstr[i+1:] 

print(mstr)

#print(mstr.swapcase())

