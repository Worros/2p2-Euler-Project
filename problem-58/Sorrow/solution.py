#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import codecs

start = time.time()

# Problem 58

VERBOSE = 1

import gmpy

sieve = {2:True}
primes = [2]

def is_prime(n):
    if gmpy.is_prime(n) > 0:
        return True
    return False

def generate_diags(n):
    """n^2-n+1     n^2
       n^2-2n+2    n^2-3n+3
       Solution from problem 28 comments"""
    return [n*n-n+1, n*n, n*n-(2*n)+2, n*n-(3*n)+3]

primes = 0
x = 3

while True:
    tmp = generate_diags(x)
    for i in tmp:
        if is_prime(i):
            primes += 1
    den = 2*x-1
    if float(primes)/float(den) < 0.10:
        print "Solution: %s" % x
        break
    x += 2


end = time.time() - start
print "Time Taken: " + str(end) + "ms"
