#!/usr/bin/env python3

#---------------------------------------------------------------------------------
#
#   Write a Python program to check if each number is prime in a given list of numbers.
#   Return True if all numbers are prime otherwise False.
#   
#   Sample Data:
#   ([0, 3, 4, 7, 9]) -> False
#   ([3, 5, 7, 13]) -> True
#   ([1, 5, 3]) -> False
#
#---------------------------------------------------------------------------------

ls = list(int(i) for i in input("Enter items of list: ").split())

flag = True
i = 0
while flag and i < len(ls):
    for j in range(2, int(ls[i] ** 0.5) + 1):
        if ls[i] % j == 0:
            flag = False
            break
    i += 1

print(flag)

