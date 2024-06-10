while 1:
    try:
        a, b, c, d, e, f = map(float, raw_input().split())
        matrix = [[a, b, c], [d, e, f]]
        for i in range(2):
            tmp = matrix[i][i]
            for j in range(3):
                matrix[i][j] = matrix[i][j] / tmp
            for j in range(2):
                if i == j:
                    continue
                else:
                    a = matrix[j][i]
                    for k in range(i, 3):
                        matrix[j][k] = matrix[j][k] - a * matrix[i][k]
        print "%.3f %.3f" % (matrix[0][2], matrix[1][2])
    except:
        break