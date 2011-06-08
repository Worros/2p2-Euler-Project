#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem 41

#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#
#What is the largest n-digit pandigital prime that exists?

import time
start = time.time()

import itertools
import math

VERBOSE = 1

sieve_exists = False
sieve_size = int(math.sqrt(9999999))
sieve = {}
primes = [2]

def create_sieve():
    print "Building sieve size: %s" % sieve_size
    for i in itertools.count(start=3):
        if i > sieve_size:
            break
        if i%2 == 0:
            pass
        else:
            if i not in sieve:
                primes.append(i)
                j = i
                while j < sieve_size:
                    sieve[j] = True # setdefault?
                    j +=i
    print "Sieve completed"

def is_prime(n):
    global sieve_exists
    if not sieve_exists:
        create_sieve()
        sieve_exists = True
    # Test precalculated primes up to 10M
    for i in primes:
        if n % i == 0:
            return False

    return True

for i in itertools.permutations("7654321", 7):
    n = int("%s%s%s%s%s%s%s" % (i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
    if is_prime(n):
        print n
        exit()

end = time.time() - start
print "Time Taken: " + str(end) + "ms"
