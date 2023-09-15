#!/usr/bin/env python3

#---------------------------------------------------------------------------------------------
#
#   Write a Python function to create an HTML string with tags around the word(s).
#   
#   Sample function and result :
#   add_tags('i', 'Python') -> '<i>Python</i>'
#   add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
#
#
#---------------------------------------------------------------------------------------------

mstr, tag = input("Enter a string: "), input("Enter a HTML tag: ")

mstr = '<' + tag + '>' + mstr[:] + '</' + tag + '>'

print(mstr)

