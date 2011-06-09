#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

start = time.time()

# Problem 23

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# 
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# 
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# 
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
# 

from math import sqrt

VERBOSE = 0


def divisors(n):
    factors = []
    for i in xrange(1,int(sqrt(n)+1)):
        if n%i == 0:
            if i != 1:
                factors.append(n/i)
            if n/i != i:
                factors.append(i)

    return factors

def is_abundant(n):
    abundant = False
    if sum(divisors(n)) > n:
        abundant = True
    return abundant

i = 1

abundant = []

while i <= 28123:
    if is_abundant(i): abundant.append(i)
    i += 1

# Must be a better way to sieve this, switching verbose on shows a massive number of duplicates
sieve = {}

for x in abundant:
    for y in abundant:
        if x+y <= 28123:
            if x+y not in sieve:
                sieve[x+y] = True
            else:
                if VERBOSE: print "(%s,%s): %s duplicate" % (x,y,x+y)
        else:
            break

tot = 0
for i in range(1, 28124):
    if i not in sieve: tot += i

print "Solution: %s" % tot

end = time.time() - start
print "Time Taken: " + str(end) + "ms"
