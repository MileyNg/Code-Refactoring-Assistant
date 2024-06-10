from math import ceil
import sys

for s in sys.stdin:
    v = float(s)
    y = 4.9*(v / 9.8)**2
    n = ceil((y + 5) / 5)
    print(n)