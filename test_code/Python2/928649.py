for i in range(input()):
	n = raw_input()
	c = 0
	while len(n) > 1:
		c += 1
		maxn = 0
		for i in range(1,len(n)):
			a = int(n[:i])
			b = int(n[i:])
			maxn = max(maxn,a*b)
		n = str(maxn)
	print c
	