import sys
for d in map(int, sys.stdin):
    print sum(d * (i ** 2) for i in range(0, 600, d))