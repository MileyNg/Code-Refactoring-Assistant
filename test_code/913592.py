while True:
    n, m = map(int, raw_input().split())
    if n==0 and m==0:
        break
    b = [input() for i in xrange(n)]
    d = [input() for i in xrange(m)]
    p = 0; ans = 0;
    for i in xrange(m):
        p += d[i]
        if p>=n-1 or p+b[p]>=n-1:
            ans = i+1
            break
        p += b[p]
    print ans