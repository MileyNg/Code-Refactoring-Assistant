while 1:
	N,M = map(int,raw_input().split())
	if N == 0: break
	T = [[0]*1261 for i in range(N)]
	for i in range(input()):
		t,n,m,s = map(int,raw_input().split())
		for ti in range(t,1261):
			T[n-1][ti] = s*m
	for i in range(input()):
		ts,te,m = map(int,raw_input().split())
		print sum(1 if any(T[n][t] == m for n in range(N)) else 0 for t in range(ts,te))
	