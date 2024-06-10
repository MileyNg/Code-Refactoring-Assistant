dx = [[0, 1, 0, -1, 0], [1, 1, -1, -1], [2, 0, -2, 0]]
dy = [[0, 0, 1, 0, -1], [-1, 1, 1, -1], [0, 2, 0, -2]]
a = [[0 for i in range(14)] for j in range(14)]
try:
    while True:
        x, y, s = map(int, raw_input().split(','))
        x += 2
        y += 2
        for i in range(s):
            for j in range(len(dx[i])):
                a[x + dx[i][j]][y + dy[i][j]] += 1
except:
    pass
ct = mx = 0
for b in a[2:-2]:
    for p in b[2:-2]:
        mx = max(mx, p)
        if p == 0:
            ct += 1
print ct
print mx