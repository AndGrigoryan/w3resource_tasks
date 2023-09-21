#!/usr/bin/env python3

#------------------------------------------------------------------------
#
#   Write a Python program that uses the Sieve of Eratosthenes method to compute prime numbers
#   up to a specified number.
#
#------------------------------------------------------------------------

def prime_num(n):
    prime_ls = []
    for i in range(2, n + 1):
        if i not in prime_ls:
            print(i, end=" ")
            for j in range(i * i, n + 1, i):
                prime_ls.append(j)


prime_num(100)

