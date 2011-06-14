#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import codecs

start = time.time()

# Problem 28

# Starting with the number 1 and moving to the right in a clockwise vec a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

VERBOSE = 0

def print_spiral(s):
    for l in s:
        print l

def generate_spiral(size):
    size = size
    MAX = size*size
    spiral = []
    for i in range(0,size):
        spiral.append([0]*size)
    center = (size-1)/2
    spiral[center][center] = 1

    number = 2
    leng = 1
    vec = 1
    xdir = center
    ydir = center
    while True:
        # Horizontal arm
        for i in range(1, leng + 1):
            if number > MAX: #Ugh
                break
            spiral[ydir][xdir + i*vec] = number
            number += 1
        xdir += leng*vec
        if number > MAX:
            break
        if xdir == size:
            break
        # Vertical arm
        for j in range(1, leng + 1):
            spiral[ydir + j*vec][xdir] = number
            number += 1
        ydir += leng*vec
        leng += 1
        vec = -vec

    if VERBOSE: print_spiral(spiral)

    return spiral

def sum_diag(spiral, size):
    sum = -1
    for i in xrange(0, size):
        sum += spiral[i][i]
        sum += spiral[i][size - 1 - i]
    return sum

size = 1001

spiral = generate_spiral(size)

print sum_diag(spiral, size)

end = time.time() - start
print "Time Taken: " + str(end) + "ms"
