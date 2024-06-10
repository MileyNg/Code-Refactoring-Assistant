while 1:
	e = input()
	if e == 0: break
	ans = 3*e
	for z in range(e+1):
		z3 = z**3
		if z3 > e: break
		y = int((e-z3)**0.5)
		x = e - y**2 - z3
		ans = min(ans,x+y+z)
	print ans