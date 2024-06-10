small_x = [-1, 0, 0, 1]
small_y = [0, -1, 1, 0]
middle_x = [-1, -1, -1, 0, 0, 1, 1, 1]
middle_y = [-1, 0, 1, -1, 1, -1, 0, 1]
big_x = [-2, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 2]
big_y = [0, -1, 0, 1, -2, -1, 1, 2, -1, 0, 1, 0]
dx = [[], small_x, middle_x, big_x]
dy = [[], small_y, middle_y, big_y]

field = [[0] * 10 for _ in range(10)]
while 1:
    try:
        x1, y1, size = map(int, raw_input().split(','))
        field[y1][x1] += 1
        for k in range(len(dx[size])):
            ny = y1 + dy[size][k]
            nx = x1 + dx[size][k]
            if nx < 0 or ny < 0 or nx >= 10 or ny >= 10:
                continue
            field[ny][nx] += 1
    except:
        break
ret, mx = 0, 0
for i in range(10):
    for j in range(10):
        if field[i][j] == 0:
            ret += 1
        mx = max(mx, field[i][j])
print ret
print mx