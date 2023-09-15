#!/usr/bin/env python3

#---------------------------------------------------------------------------------------------
#
#   Write a Python script to check whether a given key already exists in a dictionary.
#
#---------------------------------------------------------------------------------------------

d_len = int(input("Enter a length for dictionary: "))

md = {}
for _ in range(d_len):
    k, v = input("Enter a key for dictionary: "), input("Enter a value for dictionary key: ")
    md[k] = v

k = input("Enter the key to check whether it is in the dictionary or not: ")


print(md.get(k, "Key not found."))

