from math import hypot

T = input()
for t in xrange(1, T + 1):
    x1, y1, x2, y2, x3, y3 = map(float, raw_input().split())
    x4 = (((y1 - y3) * (y1 ** 2 - y2 ** 2 + x1 ** 2 - x2 ** 2) - (y1 - y2) * (y1 ** 2 - y3 ** 2 + x1 ** 2 - x3 ** 2)) /
          (2 * (y1 - y3) * (x1 - x2) - 2 * (y1 - y2) * (x1 - x3)))
    y4 = (((x1 - x3) * (x1 ** 2 - x2 ** 2 + y1 ** 2 - y2 ** 2) - (x1 - x2) * (x1 ** 2 - x3 ** 2 + y1 ** 2 - y3 ** 2)) /
          (2 * (x1 - x3) * (y1 - y2) - 2 * (x1 - x2) * (y1 - y3)))
    print "%.3f %.3f %.3f" % (x4, y4, hypot(x1 - x4, y1 - y4))