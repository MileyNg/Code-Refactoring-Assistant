bus = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in xrange(input()):
    s, t = map(int, raw_input().split())
    if s>5:
        print " ".join(map(str, bus[s:bus.index(t, s)+1]))
    else:
        if s<t:
            print " ".join(map(str, xrange(s, t+1)))
        else:
            print " ".join(map(str, xrange(s, t-1, -1)))
            