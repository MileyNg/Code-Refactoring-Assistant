for i in range(input()):
    L = map(int, raw_input().split())
    L1, L2 = [], []
    for x in L:
        if not L1 or L1[-1] < x:
            L1.append(x)
        elif not L2 or L2[-1] < x:
            L2.append(x)
        else:
            print "NO"
            break
    else:
        print "YES"