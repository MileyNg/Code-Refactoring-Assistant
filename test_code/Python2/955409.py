while 1:
	n,a,b = map(int,raw_input().split())
	if n == 0: break
	S = [1]*(n+1)
	for i in range(a):
		s = b*i
		while s <= n:
			S[s] = 0
			s += a
	print sum(S)