while 1:
	g=raw_input()
	if g=="0":break
	g=g[1:]+g[-1]
	print g.count("A"),g.count("B")