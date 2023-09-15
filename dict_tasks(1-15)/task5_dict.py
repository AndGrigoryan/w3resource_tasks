#!/usr/bin/env python3

#---------------------------------------------------------------------------------------------
#
#   Write a Python program to iterate over dictionaries using for loops.
#
#---------------------------------------------------------------------------------------------

md_len = int(input("Enter a length for dictionary: "))
md = {}

for _ in range(md_len):
    k, v = input("Enter a key: "), input("Enter a value: ")
    md[k] = v

for k, v in md.items():
    print("%s: %s"%(k, v))

