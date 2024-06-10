while 1:
    try:
        a, b, n = map(int, raw_input().split())
    except EOFError:
        break
    a %= b
    ret = 0
    for i in xrange(n):
        a *= 10
        ret += a / b
        a %= b
    print ret