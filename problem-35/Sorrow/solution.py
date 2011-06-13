#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem 35

#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#
#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
#How many circular primes are there below one million?

import time
start = time.time()

MAX = 1000000
n = 6
sieve = {2:True}
primes = [2]

def rotate(n):
    yield n
    nstr = str(n)
    i = 0
    while i < len(nstr):
        nstr = "%s%s" %(nstr[1:], nstr[0])
        yield int(nstr)
        i += 1

def circular(n):
    for i in rotate(n):
        #print "%s %s %s" %(n, i, sieve[i])
        if i % 2 == 0:
            return False
        if sieve[i] == True:
            pass
        else:
            return False
    return True

for i in range(3,MAX):
    if i%2 == 0:
        pass
    else:
        if i not in sieve:
            primes.append(i)
            sieve[i] = True
            j = i + i
            while j < MAX:
                sieve[j] = False # setdefault?
                j +=i

soln = 1

for i in primes:
    if circular(i):
        soln += 1

print soln

end = time.time() - start
print "Time Taken: " + str(end) + "ms"
