def go(n,x,dx,l):
	return min(n,max(1,x+l*dx))

while 1:
	m,n = map(int,raw_input().split())
	if m == 0: break
	x = y = 1
	dx,dy = 0,1
	while 1:
		com = raw_input().split()
		s = com[0][0]
		if   s == "S": break
		elif s == "F":
			l = int(com[1])
			x,y = go(m,x,dx,l), go(n,y,dy,l)
		elif s == "B":
			l = int(com[1])
			x,y = go(m,x,-dx,l),go(n,y,-dy,l)
		elif s == "R":
			dx,dy = dy,-dx
		elif s == "L":
			dx,dy = -dy,dx
	print x,y