while 1:
    try:
        L = map(float, raw_input().split(','))
        sm = sum(L[:10])
        t = sm / (L[10] + L[11])
        l = t * L[10]
        i = 0
        while l > 0:
            l -= L[i]
            i += 1
        print i
    except:
        break