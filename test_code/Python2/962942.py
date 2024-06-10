for t in xrange(input()):
    n = input()
    h = map(int, raw_input().split())
    print max(0, max(h[i+1]-h[i] for i in xrange(n-1))), max(0, max(h[i]-h[i+1] for i in xrange(n-1)))