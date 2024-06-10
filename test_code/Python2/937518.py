H,W = map(int,raw_input().split())
M = [map(int,list(raw_input())) for i in range(H)]
for h in range(H):
	for w in range(W):
		if 0 < w  and 0 < h:
			M[h][w] += min(M[h-1][w],M[h][w-1])
		elif w == 0 and 0 < h:
			M[h][w] += M[h-1][w]
		elif 0 < w and h == 0:
			M[h][w] += M[h][w-1]
print M[H-1][W-1]