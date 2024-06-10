while 1:
	inp = raw_input()
	if inp == "0": break
	q1,b,c1,c2,q2 = map(int,inp.split())
	a1 = min(b/c1, q2)
	a2 = (b - a1*c1)/c2
	while a1 > 0  and (a1*c1 + a2*c2 > b or a1 + a2 < q1):
		a1 -= 1
		a2 = (b - a1*c1)/c2
	print "%d %d"%(a1,a2) if a1 > 0 else "NA"