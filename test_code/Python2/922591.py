while 1:
	N,K = map(int,raw_input().split())
	if N == 0: break
	S = map(int,raw_input().split())
	B = [map(int,raw_input().split()) for i in range(N)]
	for breed in B:
		for i in range(K):
			S[i] -= breed[i]
	print "Yes" if min(S) >= 0 else "No"