N = int(raw_input())

def dfs(depth, l, r):
    if depth == 10:
        return True
    res = False
    if l < A[depth]:
        res |= dfs(depth+1, A[depth], r)
    if r < A[depth]:
        res |= dfs(depth+1, l, A[depth])
    return res

for c in range(N):
    A = map(int, raw_input().split(" "))
    print "YES" if dfs(0, 0, 0) else "NO"
    