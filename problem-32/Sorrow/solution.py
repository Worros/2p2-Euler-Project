#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem 32

import time
start = time.time()

import itertools
import math

VERBOSE = 0

solns = {}

for i in [''.join(item) for item in itertools.permutations('123456789')]:
    for j in range(2,5):
        if int(i[0:j]) * int(i[j]) == int(i[j+1:]):
            if VERBOSE: print "%s x %s = %s" %(i[0:j], i[j], i[j+1:])
            solns[int(i[j+1:])] = int(i[j+1:])
        if int(i[0:j]) * int(i[j:j+2]) == int(i[j+2:]):
            if VERBOSE: print "%s x %s = %s" %(i[0:j], i[j:j+2], i[j+2:])
            solns[int(i[j+2:])] = int(i[j+2:])
        if int(i[0:j]) * int(i[j:j+3]) == int(i[j+3:]):
            if VERBOSE: print "%s x %s = %s" %(i[0:j], i[j:j+3], i[j+3:])
            solns[int(i[j+3:])] = int(i[j+3:])

print sum(solns)

end = time.time() - start
print "Time Taken: " + str(end) + "ms"
