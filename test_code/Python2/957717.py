while 1:
    try:
        x1, y1, x2, y2, x3, y3, xp, yp = map(float, raw_input().split())
    except EOFError:
        break
    Points = [(x1, y1), (x2, y2), (x3, y3)]
    for i in xrange(3):
        A = Points[i]
        B = Points[(i + 1) % 3]
        C = Points[(i + 2) % 3]
        if A[0] - B[0] == 0:
            mark1 = C[0] - A[0]
            mark2 = xp - A[0]
        else:
            a = (A[1] - B[1]) / (A[0] - B[0])
            b = A[1] - a * A[0]
            mark1 = C[1] - (a * C[0] + b)
            mark2 = yp - (a * xp + b)
        if not ((mark1 >= 0 and mark2 >= 0) or (mark1 <= 0 and mark2 <= 0)):
            print "NO"
            break
    else:
        print "YES"