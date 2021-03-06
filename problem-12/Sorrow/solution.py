#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem 12

#The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
#
#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

#Let us list the factors of the first seven triangle numbers:
#
#     1: 1
#     3: 1,3
#     6: 1,2,3,6
#    10: 1,2,5,10
#    15: 1,3,5,15
#    21: 1,3,7,21
#    28: 1,2,4,7,14,28
#
#We can see that 28 is the first triangle number to have over five divisors.
#
#What is the value of the first triangle number to have over five hundred divisors?

from math import sqrt

VERBOSE = 1


def divisors(n):
    factors = []
    for i in xrange(1,int(sqrt(n))):
        if n%i == 0:
            factors.append(i)
            factors.append(n/i)

    return factors

tri_level = 1
tri_total = 0

target_divisors = 500
l = []

while True:
    tri_total += tri_level

    l = divisors(tri_total)

    if len(l) >= target_divisors:
        break
    tri_level += 1

print "Solution: Triangle #: %s" % tri_total
