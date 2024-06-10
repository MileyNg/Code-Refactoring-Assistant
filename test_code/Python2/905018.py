dx, dy, s = [1, 0, -1, 0], [0, 1, 0, -1], 'RDLU'


def f(x, y, d):
    x -= int(d == 2)
    y = y * 2 + dy[d]
    if not(0 <= y < len(a) and 0 <= x < len(a[y])):
        return False
    return a[y][x] == '1'

a = [raw_input() for i in range(9)]
x = y = d = 0
t = ''
while True:
    x += dx[d]
    y += dy[d]
    t += s[d]
    if x == 0 and y == 0:
        break
    for i in [(d + j + 3) % 4 for j in range(3)]:
        if f(x, y, i):
            d = i
            break
    else:
        d = (d + 2) % 4
print t