while 1:
    H,W = map(int,raw_input().split())
    if H == 0: break
    A = [raw_input() for i in range(H)]
    S = [[[0,0] for j in range(W)] for i in range(H)]
    ans = 0
    for h in range(H):
    	L = 0
        for w in range(W):
            if A[h][w] == ".":
                L += 1
            else:
                L = 0
            S[h][w][0] = L
            try: S[h][w][1] = S[h-1][w][1] + 1 if L > 0 else 0
            except: S[h][w][1] = 1 if L > 0 else 0
            if L*S[h][w][1] > ans:
                a = L
                for hi in range(1,S[h][w][1]):
                    a = min(a,S[h-hi][w][0])
                    ans = max(ans,a*(hi+1))
                    if a*S[h][w][1] < ans:
                    	break
    print ans