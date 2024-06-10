while 1:
    try:
        a, b, c = map(int, raw_input().split())
    except EOFError:
        break
    cards = set(xrange(1, 11))
    cards -= {a, b, c}
    ret = 0.0
    rest = 20 - a - b
    for card in cards:
        if rest >= card:
            ret += 1
    if ret / 7.0 >= 0.5:
        print "YES"
    else:
        print "NO"