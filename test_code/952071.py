def count_rectangle(cnt, x1, y1, x2, y2):
    return cnt[y2][x2] - cnt[y2][x1 - 1] - cnt[y1 - 1][x2] + cnt[y1 - 1][x1 - 1]


if __name__ == '__main__':
    N, M = map(int, raw_input().split())
    K = input()
    field = []
    for i in xrange(N):
        field.append(list(raw_input()))
    cnt = dict()
    ground = ('J', 'O', 'I')
    for k in ground:
        cnt[k] = [[0] * (M + 1) for _ in xrange(N + 1)]

    for i in xrange(N):
        for j in xrange(M):
            for k in cnt:
                tmp = 1 if field[i][j] == k else 0
                cnt[k][i + 1][j + 1] = cnt[k][i + 1][j] + tmp

    for j in xrange(1, M + 1):
        for i in xrange(N):
            for k in cnt:
                cnt[k][i + 1][j] += cnt[k][i][j]
                
    for i in xrange(K):
        y1, x1, y2, x2 = map(int, raw_input().split())
        ret = []
        for k in ground:
            ret.append(count_rectangle(cnt[k], x1, y1, x2, y2))
        print ' '.join(map(str, ret))