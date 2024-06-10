from itertools import *

def sieve(n):
    a = range(n)
    a[:2] = None, None
    for i in range(2, n):
        if i ** 2 >= n: break
        if not a[i]: continue
        for i in range(i ** 2, n, i):
            a[i] = None
    return a

b = sieve(50000)
a = [v for v in b if v]
while True:
    n = int(raw_input())
    if n == 0: break
    ct = 0
    for v in a:
        if v > n / 2: break
        if b[n - v]:
            ct += 1
    print ct