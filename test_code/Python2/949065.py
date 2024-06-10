while 1:
	N,M = map(int,raw_input().split())
	if N == 0: break
	T = [[0]*1261 for i in range(N)]
	r = input()
	tnms = sorted([map(int,raw_input().split()) for i in range(r)], key = lambda x:x[1])
	for i in range(0,r,2):
		t1,n,m,s = tnms[i]
		t2,n,m,s = tnms[i+1]
		T[n-1][t1:t2] = [m for j in range(t1,t2)]
	for i in range(input()):
		ts,te,m = map(int,raw_input().split())
		print sum(1 if any(T[n][t] == m for n in range(N)) else 0 for t in range(ts,te))
	