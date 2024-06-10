def gauss(matrix):
    dimension = len(matrix)
    for i in range(dimension):
        tmp = matrix[i][i]
        for j in range(dimension + 1):
            matrix[i][j] /= tmp
        for j in range(dimension):
            if i == j:
                continue
            else:
                tmp2 = matrix[j][i]
                for k in range(i, dimension + 1):
                    matrix[j][k] -= tmp2 * matrix[i][k]
    return zip(*matrix)[-1]

while 1:
    try:
        a, b, c, d, e, f = map(float, raw_input().split())
        matrix = [[a, b, c], [d, e, f]]
        print "%.3f %.3f" % gauss(matrix)
    except:
        break