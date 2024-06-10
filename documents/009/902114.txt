while 1:
    n = input()
    if n == 0:
        break
    ret = 0
    while n:
        ret += n % 10
        n /= 10
    print ret