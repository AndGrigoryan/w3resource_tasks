#!/usr/bin/env python3

#----------------------------------------------------------------------------------------------
#
#   Write a Python program to find the highest 3 values of corresponding keys in a dictionary.
#
#----------------------------------------------------------------------------------------------


def get_max_value_key(md):
    k_mx = list(md.keys())[0]
    mx = md[k_mx]

    for k, v in md.items():
        if v > mx:
            mx = v
            k_mx = k
    return k_mx


md = {'a': 3, 'b': 12, 'c': 9, 'd': 7328, 'e': 9928}
keys = []

for i in range(3):
    k = get_max_value_key(md)
    md.pop(k)
    keys.append(k)

print(*keys)



