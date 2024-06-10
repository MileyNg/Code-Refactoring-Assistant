import sys
def readint():
    for line in sys.stdin:
        yield int(line)

def getprimes(maxn):
    sieve = [0 for i in range(0,maxn+1)]
    ps = set()
    for p in range(2,maxn+1):
        if sieve[p]:
            continue
        else:
            ps.add(p)
            for k in range(p,maxn+1,p):
                sieve[k] = 1
    return ps

ns = [x for x in readint()]
primes = getprimes(max(ns))
for n in ns:
    print len(filter(lambda x:n>=x, primes))