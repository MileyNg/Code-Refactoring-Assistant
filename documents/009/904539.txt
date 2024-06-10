import math
x, y, a = 0, 0, math.radians(90)
while True:
    p, q = map(int, raw_input().split(','))
    if p == 0 and q == 0:
        break
    x += math.cos(a) * p
    y += math.sin(a) * p
    a -= math.radians(q)
print int(x)
print int(y)