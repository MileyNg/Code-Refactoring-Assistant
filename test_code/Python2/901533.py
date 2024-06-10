def div(p,q):
	deci,rest = "",[p]
	while True:
		p *= 10
		deci += str(p//q)
		p -= q*(p//q)
		rest.append(p)
		if rest[-1] == 0: return deci,rest
		if rest[-1] in rest[:-1]: return deci,rest
		
while True:
	try:
		p,q = map(int, raw_input().split())
		deci,rest = div(p,q)
		if rest[-1] == 0:
			print deci
		else:
			print deci
			print " "*rest.index(rest[-1])+"^"*(len(rest)-rest.index(rest[-1])-1)
	except:
		break