def L(cake1,cake2):
	return ((cake1+cake2)**2-abs(cake1-cake2)**2)**0.5

while 1:
	try:
		Raw_cakes=map(int,raw_input().split())
		box=Raw_cakes.pop(0)
		Raw_cakes=sorted(Raw_cakes)[::-1]
		size_min=999
		for j in range(len(Raw_cakes)):
			size=0
			raw_cakes=Raw_cakes[:]
			cakes=[raw_cakes.pop(j)]
			while raw_cakes:
				cos=[L(cakes[-1],i)/(cakes[-1]+i) for i in raw_cakes]
				cakes.append(raw_cakes.pop(cos.index(min(cos))))
			size=cakes[0]+cakes[-1]
			for i in range(len(cakes)-1):
				size+=L(cakes[i],cakes[i+1])
			size_min=min(size,size_min)
		print "OK" if size_min<=box else "NA"
	except:
		break