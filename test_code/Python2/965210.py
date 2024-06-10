def sieve(n):
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in xrange(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in xrange(i * i, n, i):
                primes[j] = False
    return [i for i in xrange(n) if primes[i]]

primes = sieve(50000)
ret = [0] * 50001
for i in xrange(len(primes)):
    for j in xrange(i, len(primes)):
        tmp = primes[i] + primes[j]
        if tmp > 50000:
            break
        ret[tmp] += 1
while 1:
    n = int(input())
    if n == 0:
        break
    print ret[n]