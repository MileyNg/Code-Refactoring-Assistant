import sys

def readint():
    for line in sys.stdin:
        yield map(int,line.split())

def gcd(x,y):
    [x,y] = [max(x,y),min(x,y)]
    while 1:
        z = x % y
        if z == 0:
            break
        [x,y] = [y,z]
    return y

for [x,y] in readint():
    GCD = gcd(x,y)
    mx = x/GCD
    print GCD,mx*y