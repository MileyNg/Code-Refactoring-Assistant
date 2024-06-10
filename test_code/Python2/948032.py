while 1:
	X,Y = map(int,raw_input().split())
	if X == 0: break
	A = [[0]+map(int,raw_input().split())+[0] for i in range(Y)]
	S = [[0]*(X+2) for i in range(Y)]
	for x in range(1,X+1): S[0][x] = 1 if A[0][x] == 0 else 0
	for y in range(1,Y):
		for x in range(1,X+1):
			if A[y][x] == 0:
				for i in range(-1,2):
					S[y][x] += S[y-1][x-i] if A[y-1][x-i] == 0 else 0
			if A[y][x] == 2:
				S[y][x] += S[y-1][x] if A[y-1][x] == 0 else 0
				if y+2 < Y and A[y+2][x] != 1:
					S[y+2][x] = S[y][x]
	ans = 0
	for x in range(1,X+1):
		ans += S[Y-1][x] + (S[Y-2][x] if A[Y-2][x] == 2 else 0)
	print ans