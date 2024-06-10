from math import hypot

n = int(input())
for i in range(n):
    x1, y1, x2, y2, x3, y3 = map(float, input().strip().split())

    d = lambda x, y: x*x + y*y
    t21 = [2*(x2-x1), 2*(y2-y1), d(x2,y2) - d(x1,y1)]
    t31 = [2*(x3-x1), 2*(y3-y1), d(x3,y3) - d(x1,y1)]

    det = lambda i, j: t21[i]*t31[j] - t21[j]*t31[i]
    a = det(2,1) / det(0,1)
    b = det(0,2) / det(0,1)
    r = hypot(x1-a, y1-b)

    print('{:.3f} {:.3f} {:.3f}'.format(a, b, r))