dx = [-3, -2, -1, 0, 0, 0, 0, 0, 0, 1, 2, 3]
dy = [0, 0, 0, -1, -2, -3, 1, 2, 3, 0, 0, 0]


def bomb(y, x):
    field[y][x] = 0
    for k in xrange(len(dx)):
        ny = y + dy[k]
        nx = x + dx[k]
        if nx < 0 or ny < 0 or nx >= 8 or ny >= 8:
            continue
        if field[ny][nx] == 1:
            bomb(ny, nx)


T = input()
for t in xrange(1, T + 1):
    field = []
    raw_input()
    for i in xrange(8):
        field.append(map(int, raw_input()))
    x, y = input() - 1, input() - 1
    bomb(y, x)
    print "Data %d:" % t
    for i in xrange(8):
        print ''.join(map(str, field[i]))