H, W = 12, 12
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(i, j):
    field[i][j] = 0
    for k in xrange(4):
        ny = i + dy[k]
        nx = j + dx[k]
        if nx < 0 or ny < 0 or nx >= W or ny >= H:
            continue
        if field[ny][nx] == 1:
            dfs(ny, nx)

while 1:
    field = []
    for i in xrange(H):
        field.append(map(int, raw_input()))

    ret = 0
    for i in xrange(H):
        for j in xrange(W):
            if field[i][j] == 1:
                dfs(i, j)
                ret += 1
    print ret
    try:
        raw_input()
    except EOFError:
        break