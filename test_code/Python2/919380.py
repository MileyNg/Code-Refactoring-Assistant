while True:
    try:
        num = float(raw_input())
        s = num
        tmp = num
        for i in xrange(9):
            tmp = tmp * 2 if i % 2 == 0 else tmp / 3
            s += tmp
        print s
    except:
        break