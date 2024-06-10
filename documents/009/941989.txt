while 1:
	m,n = map(int,raw_input().split())
	if m == 0: break
	x = y = 1
	dx,dy = 0,1
	while 1:
		com = raw_input().split()
		s = com[0][0]
		if   s == "S": break
		elif s == "R":
			dx,dy = dy,-dx
		elif s == "L":
			dx,dy = -dy,dx
		else:
			d = 1 if s == "F" else -1
			l = d*int(com[1])
			x,y = min(m,max(1,x+l*dx)),min(n,max(1,y+l*dy))
	print x,y