while 1:
    n = input()
    if n == 0:
        break
    ret = 0
    i = 1
    while 1:
        tmp = n / 5 ** i
        if tmp == 0:
            break
        ret += tmp
        i += 1
    print ret