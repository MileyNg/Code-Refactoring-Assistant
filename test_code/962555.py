from math import sqrt
from collections import namedtuple

Point = namedtuple('Point', 'x y')

def rot60(p):
    return Point(C60 * p.x - S60 * p.y, S60 * p.x + C60 * p.y)

def koch(n, p1, p2):
    if n == 0: return
    s = Point((2*p1.x + p2.x)/3, (2*p1.y + p2.y)/3)
    t = Point((p1.x + 2*p2.x)/3, (p1.y + 2*p2.y)/3)
    q = rot60(Point((p2.x - p1.x)/3, (p2.y - p1.y)/3))
    u = Point(s.x + q.x, s.y + q.y)

    koch(n - 1, p1, s)
    print(f.format(s.x, s.y))

    koch(n - 1, s, u)
    print(f.format(u.x, u.y))

    koch(n - 1, u, t)
    print(f.format(t.x, t.y))

    koch(n - 1, t, p2)


C60 = 1 / 2
S60 = sqrt(3) / 2
f = '{:8f} {:8f}'

n = int(input())
print(f.format(0, 0))
koch(n, Point(0, 0), Point(100, 0))
print(f.format(100, 0))