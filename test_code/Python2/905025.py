try:
    while True:
        a = sorted(map(int, raw_input().split(',')))
        if a.count(a[2]) == 4:
            print 'four card'
        elif a.count(a[1]) + a.count(a[-2]) == 5:
            print 'full house'
        elif a == range(a[0], a[0] + 5) or a == [1, 10, 11, 12, 13]:
            print 'straight'
        elif a.count(a[2]) == 3:
            print 'three card'
        elif a.count(a[1]) == 2 and a.count(a[-2]) == 2:
            print 'two pair'
        elif len(set(a)) == 4:
            print 'one pair'
        else:
            print 'null'
except EOFError:
    pass