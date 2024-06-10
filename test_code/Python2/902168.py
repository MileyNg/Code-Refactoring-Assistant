for i in range(input()):
    L = map(int, raw_input().split())
    L.sort()
    if L[0] ** 2 + L[1] ** 2 == L[2] ** 2:
        print "YES"
    else:
        print "NO"