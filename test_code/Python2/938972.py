R = 101
while 1:
	n,S = map(int,raw_input().split())
	if n == 0: break
	d = [int(raw_input()) for i in range(n)]
	r = [0]*R
	for i in set(d): r[i] = d.count(i)
	ans = 0
	for i in range(R):
		if 2*i > S:
			ans += r[i]*(r[i]-1)/2
		ans += r[i]*sum([r[j] for j in range(max(i+1,S-i+1),R)])
	print ans