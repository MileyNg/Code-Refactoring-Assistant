while 1:
	inp = raw_input()
	if inp == "0": break
	q1,b,c1,c2,q2 = map(int,inp.split())
	buy1 = min(b/c1,q2)
	buy2 = (b - buy1 * c1) / c2
	while buy1 > 0  and (buy1 * c1 + buy2 * c2 > b or buy1 + buy2 < q1):
		buy1 -= 1
		buy2 = (b - buy1 * c1) / c2
	if buy1 > 0:
		print buy1, buy2
	else:
		print "NA"