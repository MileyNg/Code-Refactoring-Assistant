def sieve(n):
    a = range(n)
    a[:2] = None, None
    for i in range(2, n):
        if i ** 2 >= n: break
        if not a[i]: continue
        for i in range(i ** 2, n, i):
            a[i] = None
    return [v for v in a if v]

def partialsum(a):
    b = [0] + a
    for i in range(len(a)):
        b[i + 1] += b[i]
    return b

a = partialsum(sieve(200000))
while True:
    n = int(raw_input())
    if n == 0: break
    print a[n]