while True:
    n = int(raw_input())
    if n==0:
        break
    lsum = sum(map(int, raw_input().split()))
    j = map(int, raw_input().split())
    lsum += sum(j)
    j.sort()
    ans = lsum
    for i in xrange(0,n-1):
        lsum -= j[i]
        ans = max(ans, lsum*(i+2))
    print ans