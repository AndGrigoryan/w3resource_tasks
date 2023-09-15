#!/usr/bin/env python3

#---------------------------------------------------------------------------------
#
# Write a Python function that takes two lists and returns True if they have at least one common member.
#
#---------------------------------------------------------------------------------

ls1 = input("Enter items of list1: ").split()
ls2 = input("Enter items of list2: ").split()

if ls1 < ls2:
    mn_ls, mx_ls = ls1, ls2
else:
    mn_ls, mx_ls = ls2, ls1

flag = False

for i in mn_ls:
    if i in mx_ls:
        flag = True
        break

print(flag)

