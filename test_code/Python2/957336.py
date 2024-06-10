import math

while 1:
    n = input()
    if n == -1:
        break
    x, y = 0.0, 0.0
    radian = math.radians(-90)
    for i in xrange(n):
        radian = (radian + math.pi / 2)
        x += math.cos(radian)
        y += math.sin(radian)
        radian = math.atan2(y, x)
    print "%.2f" % x
    print "%.2f" % y