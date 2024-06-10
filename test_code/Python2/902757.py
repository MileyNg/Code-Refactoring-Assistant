from math import cos, sin, radians

x, y, d = 0, 0, 90
while 1:
    a, b = map(int, raw_input().split(','))
    if a == b == 0:
        break
    x += a * cos(radians(d))
    y += a * sin(radians(d))
    d = (d - b) % 360
print int(x)
print int(y)