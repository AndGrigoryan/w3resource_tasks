#!/usr/bin/env python3

#---------------------------------------------------------------------------------
#
#   Write a Python program to get a list, sorted in increasing order by the last element 
#   in each tuple from a given list of non-empty tuples.
#   Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#   Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
#
#---------------------------------------------------------------------------------

ls = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
start = 0

while start != len(ls) -1:
    mn = ls[start][-1]
    mn_pos = start

    for i in range(start + 1, len(ls)):
        if ls[i][-1] < mn:
            mn = ls[i][-1]
            mn_pos = i
    if mn_pos != start:
        ls[start], ls[mn_pos] = ls[mn_pos], ls[start]
    
    start +=1

print(ls)

