from itertools import *

def mlist(n, *args, **keys):
    if args:
        return [mlist(*args, **keys) for i in range(n)]
    else:
        return [keys.get('default')] * n

for h in count(1):
    w = int(raw_input())
    if w == 0: break
    n = int(raw_input())
    a, b = zip(*[map(int, raw_input().split(',')) for i in range(n)])
    c = mlist(1010, 1010)
    c[0][0] = 0
    for i in range(n):
        for j in range(w + 1):
            if c[i][j] is None: continue
            c[i + 1][j] = max(c[i + 1][j], c[i][j])
            if j + b[i] <= w:
                c[i + 1][j + b[i]] = max(c[i + 1][j + b[i]], c[i][j] + a[i])
    mx = max(c[n])
    print 'Case {}:'.format(h)
    print mx
    print c[n].index(mx)