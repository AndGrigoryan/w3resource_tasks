#!/usr/bin/env python3

#------------------------------------------------------------------------
#
#   Write a Python program to check whether a list contains a sublist.
#
#------------------------------------------------------------------------


def is_sublist(ls, s):
    sub_set = False

    if s == [] or s == ls:
        sub_set = True
    elif len(s) > len(ls):
        sub_set = False
    else:
        for i in range(len(ls)):
            if ls[i] == s[0]:
                n = 1
                while (n < len(s)) and (ls[i+n] == s[n]):
                    n += 1

                if n == len(s):
                    sub_set = True
    
    return sub_set


ls1 = [int(i) for i in input("Input items of list1: ").split()]
ls2 = [int(i) for i in input("Input items of list2: ").split()]

print(is_sublist(ls1, ls2))

