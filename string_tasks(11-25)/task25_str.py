#!/usr/bin/env python3

#---------------------------------------------------------------------------------------------
#
# Write a Python program to create a Caesar encryption.
#
#---------------------------------------------------------------------------------------------

upercases = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
lowercases = [chr(i) for i in range(ord("a"), ord("z") + 1)]

mstr = list(input("Enter a string: "))
shift = input("Enter shift amount: ")
if shift.isdigit():
    shift = int(shift)
else:
    print("ERROR")
    exit()


for i in range(len(mstr)):
    if mstr[i].isalpha():
        if mstr[i].isupper():
            mstr[i] = upercases[(upercases.index(mstr[i]) + shift) % len(upercases)]
        else:
            mstr[i] = lowercases[(lowercases.index(mstr[i]) + shift) % len(upercases)]


mstr = "".join(mstr)
print(mstr)

