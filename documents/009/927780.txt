#!/usr/bin/env python

import sys

def solve(n, s, j, a, c):
    if len(a) == n:
        if sum(a) == s:
            c += 1
    elif len(a) < n:
        for i in range(j, 10):
            c = solve(n, s, i+1, a + [i], c)
    return c

for line in sys.stdin:
    if line == "0 0\n":
        break
    else:
        nums = line.replace('\n', '').split(' ')
        n = int(nums[0])
        s = int(nums[1])
        c = solve(n, s, 0, [], 0)
        print c