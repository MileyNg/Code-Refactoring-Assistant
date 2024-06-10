while 1:
	a,b = map(int,raw_input().split())
	if a == 0: break
	block = [map(int,raw_input().split()) for i in range(input())]
	road = [[0]*(a+1) for i in range(b+1)]
	road[1][1] = 1
	for bi in range(1,b+1):
		for ai in range(1,a+1):
			if [ai,bi] not in block:
				road[bi][ai] += road[bi-1][ai] + road[bi][ai-1]
	print road[b][a]