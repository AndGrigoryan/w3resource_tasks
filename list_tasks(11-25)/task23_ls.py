#!/usr/bin/env python3

#---------------------------------------------------------------------------------
#
#    Write a Python program to flatten a shallow list.
#
#---------------------------------------------------------------------------------

nums = [[2,4,3],[1,5,6], [9], [7,9,0]]
newls = []

for i in range(len(nums)):
    for j in range(len(nums[i])):
        newls.append(nums[i][j])

print(newls)

