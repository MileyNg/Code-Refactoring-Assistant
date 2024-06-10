from bisect import *

def sieve(n):
    a = range(n)
    a[:2] = None, None
    for i in range(2, n):
        if i ** 2 >= n: break
        if not a[i]: continue
        for i in range(i ** 2, n, i):
            a[i] = None
    return [v for v in a if v]

try:
    a = sieve(90000)
    while True:
        n = int(raw_input())
        i = bisect_right(a, n)
        print a[i - (2 if a[i - 1] == n else 1)], a[i]
except EOFError:
    pass