L = []
while 1:
    try:
        d = input()
        x = 600
        ret = 0
        for i in range(0, 600, d):
            ret += d * (i ** 2)
        print ret
    except:
        break