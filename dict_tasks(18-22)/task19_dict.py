#!/usr/bin/env python3

#----------------------------------------------------------------------------------------
#
#   Write a Python program to combine two dictionary by adding values for common keys.
#   d1 = {'a': 100, 'b': 200, 'c':300}
#   d2 = {'a': 300, 'b': 200, 'd':400}
#   Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
#
#----------------------------------------------------------------------------------------

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = {}

if len(d1) > len(d2):
    mx, mn = d1, d2
else:
    mx, mn = d2, d1

d3.update(mn)

for k, v in mx.items():
    d3[k] = d3.get(k, 0) + v

print(d3)

