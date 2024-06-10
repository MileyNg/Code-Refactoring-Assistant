while 1:
	n,k = map(int,raw_input().split())
	if n == 0: break
	s = [0]*(n+1)
	c = sorted([int(raw_input()) for i in range(k)])
	p = 1 if c[0] == 0 else 0
	pre = 0
	for i in c[p:]:
		s[i] = s[i-1] + 1
		if p and s[i-1] == 0:
			if s[i-2] > 0:
				s[i] += s[i-2] + 1 - pre
				pre = s[i-2] + 1
			if s[i-2] == 0:
				pre = 0
	print max(s)