import math
a, b, C = map(float, raw_input().split())
S = math.sin(math.radians(C)) * a * b / 2
L = a + b + (a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(C))) ** 0.5
print "%.8f\n%.8f\n%.8f" % (S, L, S * 2 / a)