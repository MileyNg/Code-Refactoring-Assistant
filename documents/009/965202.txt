import math

n = input()
for i in xrange(n):
    xa, ya, ra, xb, yb, rb = map(float, raw_input().split())
    l = math.hypot(xa - xb, ya - yb)
    if l + rb < ra:
        print 2
    elif l + ra < rb:
        print -2
    elif l <= ra + rb:
        print 1
    else:
        print 0