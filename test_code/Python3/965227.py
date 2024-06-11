from math import hypot

n = int(input())
for i in range(n):
    xa, ya, ra, xb, yb, rb = map(float, input().split())
    d = hypot(xb - xa, yb - ya)
    if ra + rb < d:
        print(0)
    elif abs(ra - rb) <= d:
        print(1)
    elif rb < ra:
        print(2)
    else:
        print(-2)