import bisect


def sieve(n):
    a = range(n)
    a[0], a[1] = None, None
    for i in range(2, n):
        if i ** 2 >= n:
            break
        if a[i] is None:
            continue
        for j in range(i ** 2, n, i):
            a[j] = None
    j = 0
    for i in range(n):
        if a[i] is not None:
            a[j] = a[i]
            j += 1
    return a[0:j]

a = sieve(1000000)

try:
    while True:
        print bisect.bisect_right(a, int(raw_input()))
except:
    pass