while 1:
	n = input()
	if n == 0: break
	N = [input() for i in range(n)]
	s = input()
	l,r= 0,n-1
	c = 0
	while l <= r:
		i = (l + r)/2
		c += 1
		if N[i] == s:
			break
		elif N[i] < s:
			l = i + 1
		else:
			r = i - 1
	print c