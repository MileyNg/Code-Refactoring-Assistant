import sys
def sieve(m):
    N=range(1,m+2,2)
    r=int(m**.5)
    h=len(N)
    N[0]=0
    for i in range(h):
        x=N[i]
        if x>r: break
        if x and i+x<h: N[i+x:h:x]=[0]*((h-1-i-x)/x+1)
    return N
def f0056(n):
    x=0
    if n<4:x=0
    elif n==4:x=1
    elif n%2==1:
        if S[(n-2)/2]: x=1
    else:
        a=n/2
        for e in PRIMES:
            if e>a: break
            if S[(n-e)/2]: x+=1
    return x
 
S=sieve(50000)
PRIMES=filter(None,S)
for n in sys.stdin:
    n=int(n)
    if n==0: break
    print f0056(n)