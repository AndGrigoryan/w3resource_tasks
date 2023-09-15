#!/usr/bin/env python3

#---------------------------------------------------------------------------------------------
#
#   Write a Python script to add a key to a dictionary.
#
#   Sample Dictionary : {0: 10, 1: 20}
#   Expected Result : {0: 10, 1: 20, 2: 30}
#
#---------------------------------------------------------------------------------------------

md = {0: 10, 1: 20}

k, v = int(input("Enter a new key: ")), int(input("Enter a value for new key: "))

md[k] = v

print(md)

