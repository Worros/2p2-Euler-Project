#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem 36

import time
start = time.time()

VERBOSE = 0

def is_pallindrome(n):
    return n == n[::-1]

MAX = 1000000
tot = 0
for i in range(1,MAX+1):
    if is_pallindrome(str(i)) and is_pallindrome(str(bin(i)[2:])):
        if VERBOSE: print "Found: %s: %s" % (i, bin(i)[2:])
        tot += i
        
print "Solution: %s" % tot
end = time.time() - start
print "Time Taken: " + str(end) + "ms"

