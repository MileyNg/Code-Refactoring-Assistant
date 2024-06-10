while 1:
    try:
        d = input()
        print sum(d * (i ** 2) for i in range(0, 600, d))
    except:
        break