while True:
	try:
		n, m = (int(x.strip()) for x in raw_input().split())
		if n == 0 and m == 0: break
		p = [int(x.strip()) for x in raw_input().split()]
		s = sum(p)
		p.sort(reverse=True)
		for x in p[m - 1::m]:
			s -= x
		print s
	except:
		pass