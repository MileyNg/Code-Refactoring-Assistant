while True:
    n, m = map(int, raw_input().split())
    if n==0 and m==0:
        break
    p = range(1,n+1); idx = n-1;
    while len(p)>1:
        idx = (idx + m)%len(p)
        p.pop(idx)
        idx = (idx + len(p) - 1)%len(p)
    print p[0]