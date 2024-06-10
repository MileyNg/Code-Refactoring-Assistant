def sieve(n):
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in xrange(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in xrange(i * i, n, i):
                primes[j] = False
    return [i for i in xrange(n) if primes[i]]

prime_list = sieve(200000)
while 1:
    a = input()
    if a == 0:
        break
    print sum(prime_list[:a])