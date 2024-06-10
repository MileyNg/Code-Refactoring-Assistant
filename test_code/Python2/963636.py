def sieve(n):
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in xrange(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in xrange(i * i, n, i):
                primes[j] = False
    return [i for i in xrange(n) if primes[i]]

while 1:
    try:
        n = input()
    except EOFError:
        break
    primes = sieve(n * 2)
    small, big = -1, -1
    for prime in primes:
        if prime < n:
            small = prime
        if prime > n:
            big = prime
            break
    print small, big