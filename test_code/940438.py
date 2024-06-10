while 1:
	n,k = map(int,raw_input().split())
	s = [0]*(n+1)
	ss = [0]*(n+1)
	if n == 0: break
	c = sorted([int(raw_input()) for i in range(k)])
	use0 = -1
	if c[0] == 0:
		use0 = 1
		c.pop(0)
	for i in c:
		s[i] = s[i-1]+1
		ss[i] = ss[i-1]+1
		if s[i-1] == 0 and s[i-2] > 0:
			ss[i] = s[i] + s[i-2] + 1
	print max(s) if use0 == -1 else max(ss)
	