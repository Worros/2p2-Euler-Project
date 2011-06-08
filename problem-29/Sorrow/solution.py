#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
start = time.time()
import math

# Problem 29

m = []
sol = []

vals = {}
a, b = 2, 2
abmax = 100

while a <= abmax:
    b = 2
    while b <= abmax:
        tmp = int(math.pow(a,b))
        vals[tmp] = True
        b += 1
    a += 1

print "Solution: %s" % len(vals.keys())

end = time.time() - start
print "Time Taken: " + str(end) + "ms"
