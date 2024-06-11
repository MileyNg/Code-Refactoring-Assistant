import sys

s = c = n = 0
for line in sys.stdin:
    x, y = map(int, line.split(','))
    s += x * y
    c += y
    n += 1
print(s)
print(int(c / n + 0.5))