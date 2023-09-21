#!/usr/bin/env python3

#------------------------------------------------------------------------
#
#   Write a Python program to check whether two lists are circularly identical.
#
#------------------------------------------------------------------------


def circularly_identical(ls1, ls2):
    
    ls3 = ls1 * 2

    for x in range(0, len(ls1)):
        z = 0
        
        for y in range(x, x + len(ls1)):
            if ls2[z] == ls3[y]:
                z += 1
            else:
                break
        
        if z == len(ls1):
            return True

    return False


ls1 = [1, 1, 1, 0, 0]
ls2 = [0, 0, 1, 1, 1]

if (circularly_identical(ls1, ls2)):
    print("Yes!")
else:
    print("No!")

