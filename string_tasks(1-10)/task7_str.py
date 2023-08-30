#!/usr/bin/env python3

#---------------------------------------------------------------------------------------------
#
#   Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string.
#   If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
#   
#   Sample String : 'The lyrics is not that poor!'
#   Expected Result : 'The lyrics is good!'
#
#---------------------------------------------------------------------------------------------

mstr = input("Enter a string: ")


ind_not = mstr.find('not')
ind_poor = mstr.find('poor')
if ind_not != -1 and ind_not < ind_poor:
    mstr = mstr.replace(mstr[ind_not:ind_poor+4], 'good')

print(mstr)

