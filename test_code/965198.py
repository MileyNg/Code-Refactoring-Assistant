import sys
a = 'abcdefghijklmnopqrstuvwxyz'

for s in sys.stdin:
    for n in range(1, 27):
        t = s[:-1].translate(str.maketrans(a, a[n:] + a[:n]))
        if 'the' in t or 'this' in t or 'that' in t: break
    print(t)