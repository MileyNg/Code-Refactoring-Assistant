import sys

a = []
for line in sys.stdin:
    a.append(int(line))

d = [a.count(i) for i in range(1, 101)]
m = max(d)
for i in range(100):
    if d[i] == m: print(i + 1)