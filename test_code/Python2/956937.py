n = input()
for _ in xrange(n):
    a, b = input(), input()
    ret = a + b
    overflow = 10 ** 80
    if a + b >= overflow:
        print 'overflow'
    else:
        print ret