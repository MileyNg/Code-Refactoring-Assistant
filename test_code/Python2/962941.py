for t in xrange(input()):
    up = 0; down = 0;
    n = input()
    h = map(int, raw_input().split())
    print max([0]+[h[i+1]-h[i] for i in xrange(n-1)]), max([0]+[h[i]-h[i+1] for i in xrange(n-1)])