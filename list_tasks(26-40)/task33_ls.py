#!/usr/bin/env python3

#------------------------------------------------------------------------
#
#   Write a Python program to generate all sublists of a list.
#
#------------------------------------------------------------------------


def sub_ls(ls):
    tmp = []
    for i in range(len(ls)):
        for j in range(i, len(ls)):
            tmp.append(ls[i:j + 1])

    return tmp


ls = [int(i) for i in input().split()]

print(sub_ls(ls))
    
