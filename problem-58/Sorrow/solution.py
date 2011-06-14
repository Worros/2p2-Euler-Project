#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import codecs

start = time.time()

# Problem 58

VERBOSE = 1

import itertools
import math
import gmpy

sieve = {2:True}
primes = [2]

def is_prime(n):
    return gmpy.is_prime(n)

def generate_spiral():
    MIN = 10000000
    number = 2
    leng = 1
    vec = 1
    while True:
        for i in range(1, leng + 1):
            number += 1
        yield (number -1)
        for j in range(1, leng + 1):
            number += 1
        yield (number -1)
        leng += 1

def get_prime_ratio(lst):
    den = len(lst)
    num = []
    for x in lst[:-4]:
        if is_prime(x):
            num.append(x)
    #print "%s/%s: %s" %(len(num), den, float(len(num))/float(den))
    #print num
    return float(len(num))/float(den)

ratio = 1

size = 1

diags = []

count = 0
for x in generate_spiral():
    diags.append(x)
    count = count % 4
    if count == 0:
        if len(diags) > 10000:
            ratio = get_prime_ratio(diags)
            if (size % 50) - 1 == 0:
                print "(%s): %s" %(size, ratio)
        size += 2
        if ratio < 0.1 and len(diags) > 1:
            print "(%s): %s" %(size, ratio)
            break
    count += 1

end = time.time() - start
print "Time Taken: " + str(end) + "ms"
