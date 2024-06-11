import sys

d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

for s in sys.stdin:
    s = [d[c] for c in s.strip()] + [0]
    n = 0
    for i, x in enumerate(s[:-1]):
        if x >= s[i + 1]:
            n += x
        else:
            n -= x
    print(n)