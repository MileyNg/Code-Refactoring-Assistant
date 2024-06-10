# coding:utf-8
from __future__ import division, print_function
try:
    input = raw_input
    range = xrange
except NameError:
    pass

p, q = 10 ** 9 + 7, 0xffffffff
pow_p = [1]
for i in range(4010):
    pow_p.append(pow_p[-1] * p & q)


def exists(a, b, k):
    n, m = len(a), len(b)

    s = [a[k + i] - a[i] * pow_p[k] & q for i in range(n - k)]
    t = [b[k + i] - b[i] * pow_p[k] & q for i in range(m - k)]
    return len(set(s).intersection(set(t))) > 0


def hash(s):
    t = 0
    yield t
    for c in s:
        t = t * p + ord(c) & q
        yield t
    return


def solve(s, t):
    n, m = len(s), len(t)
    a, b = list(hash(s)), list(hash(t))

    l, r = 0, min(n, m) + 1
    while l + 1 < r:
        m = (l + r) // 2
        if exists(a, b, m):
            l = m
        else:
            r = m
    return l


while True:
    try:
        s = input().strip()
        t = input().strip()
    except EOFError:
        break

    print(solve(s, t))