try:
    while True:
        a = map(int, raw_input().split())
        b = map(int, raw_input().split())
        p = q = 0
        for i in range(len(b)):
            if a[i] == b[i]:
                p += 1
            elif a.count(b[i]) != 0:
                q += 1
        print p, q
except:
    pass