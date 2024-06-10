def div(p,q):
	d,r = "",[p]
	while True:
		p *= 10
		d += str(p//q)
		p -= q*(p//q)
		r.append(p)
		if r[-1] == 0 or r[-1] in r[:-1]: return d,r
		
while True:
	try:
		p,q = map(int, raw_input().split())
		d,r = div(p,q)
		s = r.index(r[-1])
		if s == len(r)-1:
			print d
		else:
			print "{}\n{}".format(d," "*s+"^"*(len(r)-s-1))
	except:
		break