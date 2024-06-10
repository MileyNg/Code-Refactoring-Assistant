while 1:
	H,W = map(int,raw_input().split())
	if H == 0: break
	M = [raw_input() for i in range(H)]
	A = [[0]*W for i in range(H)]
	B = [[0]*W for i in range(H)]
	ans = 0
	for h in range(H):
		L = 0
		for w in range(W):
			if M[h][w] == ".":
				L += 1
			else:
				L = 0
			A[h][w] = L
			try: B[h][w] = B[h-1][w] + 1 if L > 0 else 0
			except: B[h][w] = 1 if L > 0 else 0
			if L*B[h][w] > ans:
				a = L
				for hi in range(B[h][w]):
					a = min(a,A[h-hi][w])
					if a*B[h][w] <= ans:
						break
					ans = max(ans,a*(hi+1))
	print ans