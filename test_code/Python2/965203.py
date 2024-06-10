def sieve(n):
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in xrange(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in xrange(i * i, n, i):
                primes[j] = False
    return [i for i in xrange(n) if primes[i]]

primes_a = sieve(25000)
primes_b = set(sieve(50000))
while 1:
    n = input()
    if n == 0:
        break
    ret = 0
    for prime in primes_a:
        if prime > n / 2:
            break
        if n - prime in primes_b:
            ret += 1
    print ret