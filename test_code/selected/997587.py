def sieve(n):
    p = [True for i in range(n + 1)]
    p[0] = p[1] = False
    end = int(n ** .5)
    for i in range(2, end + 1):
        if p[i]:
            for j in range(i * i, n + 1, i):
                p[j] = False

    return p

def primes_below(n):
    if n < 2: return 0
    c = 1
    for i in range(3, n + 1, 2):
        if p[i]: c += 1

    return c

p = sieve(1000000)
while 1:
    try:
        n = int(input())
    except EOFError:
        break
    else:
        print(primes_below(n))