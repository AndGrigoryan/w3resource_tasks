#!/usr/bin/env python3

#------------------------------------------------------------------------
#
#   Write a Python program to create a list by concatenating a given list with a range from 1 to n.
#   Sample list : ['p', 'q']
#   n =5
#   Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
#
#------------------------------------------------------------------------

ls = ['p', 'q']
tmp = []
n = int(input("n: "))

for i in range(1, n + 1):
    ls_cp = ls.copy()
    for j in range(len(ls_cp)):
        ls_cp[j] += str(i)
    tmp.extend(ls_cp)
    
print(tmp)

