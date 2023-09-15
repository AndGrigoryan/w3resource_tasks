#!/usr/bin/env python3

#---------------------------------------------------------------------------------------------
#
#   Write a Python function to get a string made of 4 copies of the last two characters of a
#   specified string (length must be at least 2).
#   Sample function and result :
#   insert_end('Python') -> onononon
#   insert_end('Exercises') -> eseseses
#
#---------------------------------------------------------------------------------------------

mstr = input("Enter a string: ")

if len(mstr) >= 2:
    print((mstr[-2] + mstr[-1]) * 4)
else:
    print("ERROR! String length must be 2 and more")

