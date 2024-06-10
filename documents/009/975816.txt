for i in xrange(input()):
    c, a, n = map(int, raw_input().split())
    can = min(c, a, n)
    c -= can; a -= can; n -= can;
    cca = min(c/2, a)
    c -= 2*cca; a -= cca;
    ccc = c/3
    c -= 3*ccc;
    print can+cca+ccc