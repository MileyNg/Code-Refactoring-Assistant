while 1:
    m, f, r = map(int, raw_input().split())
    if m == f == r == -1:
        break
    if m == -1 or f == -1:
        print "F"
    elif m + f >= 80:
        print "A"
    elif 65 <= m + f < 80:
        print "B"
    elif 50 <= m + f < 65:
        print "C"
    elif 30 <= m + f < 50:
        print "C" if r >= 50 else "D" 
    else:
        print "F"