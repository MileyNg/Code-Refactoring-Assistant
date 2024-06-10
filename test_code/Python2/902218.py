def sieve(n):
    prime = [True] * n
    prime[0] = prime[1] = False
    for i in xrange(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, n, i):
                prime[j] = False
    return [i for i in xrange(2, n) if prime[i]]

while 1:
    try:
        print len(sieve(input() + 1))
    except:
        break