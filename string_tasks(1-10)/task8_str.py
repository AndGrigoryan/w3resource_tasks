#!/usr/bin/env python3

#---------------------------------------------------------------------------------------------
#
#  Write a Python function that takes a list of words and return the longest word and the length of the longest one.
#  Sample Output:
#  Longest word: Exercises
#  Length of the longest word: 9
#
#---------------------------------------------------------------------------------------------

ls = input("Enter a string: ").split()
mxstr = ls[0]

for i in ls:
    if len(mxstr) < len(i):
        mxstr = i

print("Longest word: ", mxstr)
print("Length of the longest word: ", len(mxstr))

