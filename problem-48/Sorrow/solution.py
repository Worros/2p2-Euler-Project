#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem 48

# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
#
# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.


import time
start = time.time()

import decimal

VERBOSE = 0

tot = 0
context = decimal.Context
for i in range(1,1001):
    tot += i**i

print tot%10000000000

end = time.time() - start
print "Time Taken: " + str(end) + "ms"
