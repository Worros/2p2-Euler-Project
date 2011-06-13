#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem 4
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

import time
start = time.time()

VERBOSE = 0

def is_pallindrome(n):
    return n == n[::-1]

maximum = 999
i, j = maximum, maximum


imin = 0
jmin = 0

found = False
max_pallindrome = 0
val = 0
total_iterations = 0
record = [0,0,0]
all_pallindromes = []

while i > imin:
    while j > jmin:
        val = i * j
        if VERBOSE: print "%d * %d = %d" %(i, j, val)
        if is_pallindrome(str(val)):
            if VERBOSE: print "Found: %d * %d = %d" % (i, j, val)
            found = True
            break
        total_iterations += 1
        j -= 1
    if found:
        if val > max_pallindrome:
            max_pallindrome = val
            if VERBOSE: print "New max %d * %d = %d" % (i, j, max_pallindrome)
            record = [max_pallindrome, i, j]
            imin, jmin = j, j
        all_pallindromes.append([val, i, j])
        found = False
    j = maximum
    i -= 1

if VERBOSE: print "All palindromes found: %s" % all_pallindromes
if VERBOSE: print "Total interations: %s" % total_iterations
print "Solution: %s" % record 

end = time.time() - start
print "Time Taken: " + str(end) + "ms"

