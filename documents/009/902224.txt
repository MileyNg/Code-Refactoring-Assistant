from bisect import bisect


def sieve(n):
    prime = [True] * n
    prime[0] = prime[1] = False
    for i in xrange(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, n, i):
                prime[j] = False
    return [i for i in xrange(2, n) if prime[i]]

primes = sieve(999999)
while 1:
    try:
        print bisect(primes, input())
    except:
        break