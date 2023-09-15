#!/usr/bin/env python3

#---------------------------------------------------------------------------------------------
#
#   Write a Python function to insert a string in the middle of a string.
#   
#   Sample function and result :
#   insert_sting_middle('[[]]', 'Python') -> [[Python]]
#   insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
#
#---------------------------------------------------------------------------------------------

mstr, symbols = input("Enter a string: "), input("Enter a symbols: ")

mstr = symbols[:len(symbols) // 2] + mstr + symbols[len(symbols)// 2:]

print(mstr)

