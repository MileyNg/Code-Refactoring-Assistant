while True:
	try:
		a,b,c,d,e,f = map(float,raw_input().split())
		x = (e*c-b*f) / (e*a-b*d)
		y = (c*d-a*f) / (b*d-e*a)
		if x == -0.0:
			x = 0
		if y == -0.0:
			y = 0
		print '%.3f %.3f' % (x,y)
	except EOFError:
		break