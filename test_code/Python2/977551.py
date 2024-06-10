import sys
import math

def readdata():
    for line in sys.stdin:
        yield map(int,line.split())

def rounder(decimal):
    rounded = round(decimal*1000)/1000
    if rounded == -0.0:
        rounded = +0.0
    return rounded

for data in readdata():
    [a,b,c,d,e,f] = map(float,data)
    det = a*e-b*d
    x = (c*e-b*f)/det
    y = (a*f-c*d)/det
    [x,y] = map(rounder,[x,y])
    print "%1.3f %1.3f" % (x,y)