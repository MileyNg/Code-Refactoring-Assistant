R = 101
while 1:
	n,S = map(int,raw_input().split())
	if n == 0: break
	r = [0]*R
	for i in range(n):
		r[int(raw_input())] += 1
	ans = 0
	for i in range(R):
		if 2*i > S:
			ans += r[i]*(r[i]-1)/2
		ans += r[i]*sum([r[j] for j in range(i+1,R) if i+j > S])
	print ans