#!/usr/bin/env python3

#---------------------------------------------------------------------------------------------
#
#   Write a Python program to sort a string lexicographically.
#
#---------------------------------------------------------------------------------------------

mstr = input("Enter a string: ")

start = 0
mstr = list(mstr)
while start != len(mstr) - 1:
    mn = mstr[start]
    mn_pos = start

    for i in range(start, len(mstr)):
            if mstr[i] < mn:
                mn = mstr[i]
                mn_pos = i

                if mn_pos != start:
                    mstr[start], mstr[mn_pos] = mstr[mn_pos], mstr[start]
    start += 1
mstr = ''.join(mstr)
print(mstr)

