d = {
        ((0, 0), (1, 0), (0, 1), (1, 1))  : 'A',
        ((0, 0), (0, 1), (0, 2), (0, 3))  : 'B',
        ((0, 0), (1, 0), (2, 0), (3, 0))  : 'C',
        ((0, 0), (-1, 1), (0, 1), (-1, 2)): 'D',
        ((0, 0), (1, 0), (1, 1), (2, 1))  : 'E',
        ((0, 0), (0, 1), (1, 1), (1, 2))  : 'F',
        ((0, 0), (1, 0), (-1, 1), (0, 1)) : 'G'
    }


n = 9
while True:
    if n == 9:
        n = 0
        a = []
    try:
        line = input()
    except:
        break
    a.append(line)
    n += 1
    if n != 8: continue

    piece = [(x, y) for y in range(8) for x in range(8) if a[y][x] == '1']
    x0, y0 = piece[0]
    piece = tuple([(x - x0, y - y0) for x, y in piece])
    print(d[piece])