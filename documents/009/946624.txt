
N = int(raw_input())
    
for c in range(N):
    
    B = [0]
    C = [0]
    
    def dfs(depth):
        if depth == 10:
            return True
            
        res = False
        if B[-1] < A[depth]:
            B.append(A[depth])
            res |= dfs(depth+1)
            del B[-1]
        if C[-1] < A[depth]:
            C.append(A[depth])
            res |= dfs(depth+1)
            del C[-1]
        return res
    
    A = map(int, raw_input().split(" "))
    
    print "YES" if dfs(0) else "NO"
    