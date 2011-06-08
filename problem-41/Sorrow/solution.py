#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem 41

#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#
#What is the largest n-digit pandigital prime that exists?

import itertools

VERBOSE = 1

def is_pandigital(n):
    pandigital = True
    tmp = {}
    for c in n:
        if c in tmp:
            pandigital = False
            break
        else:
            tmp[c] = True
    return pandigital        

MAX = 50000000
n = 6
sieve = {}
primes = [2]
val = 0

for i in itertools.count(start=3):
    if i > MAX:
        break
    if i%2 == 0:
        pass
    else:
        if i not in sieve:
            if is_pandigital(str(i)):
                val = i
                print val
            j = i
            while j < MAX:
                sieve[j] = True # setdefault?
                j +=i

print val

