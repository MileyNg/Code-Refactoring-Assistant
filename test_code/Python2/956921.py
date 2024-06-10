while 1:
    try:
        n = input()
    except EOFError:
        break
    ret = n
    for i in xrange(9):
        if i % 2:
            n /= 3
        else:
            n *= 2
        ret += n
    print ret