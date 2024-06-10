from bisect import *
while 1:
	N,M = map(int,raw_input().split())
	if N == 0: break
	P = [int(raw_input()) for i in range(N)] + [0]
	P = sorted(set(i+j for i in P for j in P))
	s = bisect(P,M) - 1
	print max(i + P[bisect(P,M-i) - 1] for i in P[:s])