# -*- coding: utf-8 -*-

count = 0
def dfs(i, j, island):
    global count
    #print i, j
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    if i < 0 or i >= len(island) or j < 0 or j >= len(island[0]):
        return

    if island[i][j] == '#' or island[i][j] == 'x':
        return

    island[i][j] = 'x'
    count += 1
    
    for d in dxy:
        dfs(i+d[0], j+d[1], island)

def solve(w, h, island):
    s_i = 0
    s_j = 0
    for i, row in enumerate(island):
        for j, s in enumerate(row):
            if s == '@':
                s_i = i
                s_j = j
                break

    dfs(s_i, s_j, island)
    print count

def func():
    '''

    '''
    while True:
        global count
        wh = map(int, raw_input().split())
        w = wh[0]
        h = wh[1]
        if w == 0 and h == 0:
            break
        island = []
        count = 0
        for i in range(h):
            row = []
            line = raw_input()
            for j in line:
                row.append(j)
            island.append(row)
        
        # for row in island:
        #     for j in row:
        #         print j
        #     print ''

        solve(w, h, island)


func()
    