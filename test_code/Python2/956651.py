blocks = {'A': [[0, 0, 1, 1],
                [0, 1, 0, 1]],
          'B': [[0, 0, 0, 0],
                [0, 1, 2, 3]],
          'C': [[0, 1, 2, 3],
                [0, 0, 0, 0]],
          'D': [[0, 0, -1, -1],
                [0, 1, 1, 2]],
          'E': [[0, 1, 1, 2],
                [0, 0, 1, 1]],
          'F': [[0, 0, 1, 1],
                [0, 1, 1, 2]],
          'G': [[-1, 0, 0, 1],
                [1, 0, 1, 0]], }

while 1:
    field = []
    for i in xrange(8):
        field.append(raw_input())
    for i in xrange(8):
        for j in xrange(8):
            if field[i][j] == '1':
                for block in blocks:
                    dx, dy = blocks[block]
                    for k in xrange(4):
                        ny = i + dy[k]
                        nx = j + dx[k]
                        if nx < 0 or ny < 0 or nx >= 8 or ny >= 8:
                            break
                        if field[ny][nx] != '1':
                            break
                    else:
                        print block
                        break
    try:
        raw_input()
    except EOFError:
        break