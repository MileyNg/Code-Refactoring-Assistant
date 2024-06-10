import math

DELTA = 1e-10

def readnums():
    return raw_input().split()

def cross(v1,v2):
    return v1[0]*v2[1]-v1[1]*v2[0]

[n] = readnums()
for i in range(0,int(n)):
    [xa,ya,xb,yb,xc,yc,xd,yd] = map(float,readnums())
    vab = (xb-xa,yb-ya)
    vcd = (xd-xc,yd-yc)
    prod = cross(vab,vcd)
    if math.fabs(prod) < DELTA:
        print "YES"
    else:
        print "NO"