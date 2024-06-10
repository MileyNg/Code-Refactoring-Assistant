import sys
import math

def readnums():
    for line in sys.stdin:
        yield map(int,line.split(','))

[x,y] = [0.0,0.0]
degree = 90
for [steps,delta_d] in readnums():
    if steps == 0 and degree == 0:
        break
    phi = math.radians(degree)
    x += steps*math.cos(phi)
    y += steps*math.sin(phi)
    degree -= delta_d
print int(x)
print int(y)