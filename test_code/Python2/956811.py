from math import hypot

while 1:
    x, h = input(), input()
    if x == h == 0:
        break
    print hypot(x / 2.0, h) * x * 2 + x ** 2