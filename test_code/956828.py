def prim(n):
    min_cost = [1 << 31] * n
    used = [False] * n
    min_cost[0] = 0
    ret = 0
    while 1:
        v = -1
        for u in range(n):
            if not used[u] and (v == -1 or min_cost[u] < min_cost[v]):
                v = u
        if v == -1:
            break
        used[v] = True
        ret += min_cost[v] - 100

        for u in range(n):
            min_cost[u] = min(min_cost[u], edges[v][u])
    return ret

if __name__ == '__main__':
    while 1:
        n = input()
        if n == 0:
            break
        m = input()

        edges = [[1 << 30] * n for _ in xrange(n)]
        for i in xrange(m):
            a, b, cost = map(int, raw_input().split(','))
            edges[a][b] = cost
            edges[b][a] = cost
        print (prim(n) + 100) / 100