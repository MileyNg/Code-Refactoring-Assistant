while 1:
    try:
        n = input()
    except EOFError:
        break
    ret = 1
    for i in xrange(1, n + 1):
        ret += i
    print ret