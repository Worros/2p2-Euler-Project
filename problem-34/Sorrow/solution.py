#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem 34

#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
#Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
#Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import time
start = time.time()

VERBOSE = 0

MAX = 100000
i = 3
soln = []

f= [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

while i < MAX:
    tmp = 0
    for c in str(i):
        tmp += f[int(c)]
    if tmp == i:
        if VERBOSE: print "Found: %s" % i
        soln.append(i)
    i += 1

print "Solution: %s" % sum(soln)        
end = time.time() - start
print "Time Taken: " + str(end) + "ms"

