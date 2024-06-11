while True:
    m, f, r = map(int, input().strip().split())
    if m == f == r == -1: break
    g = 'F'
    if m == -1 or f == -1: g = 'F'
    elif m + f >= 80: g = 'A'
    elif m + f >= 65: g = 'B'
    elif m + f >= 50: g = 'C'
    elif m + f >= 30: g = 'C' if r >= 50 else 'D'
    print(g)