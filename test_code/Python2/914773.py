def L(cake1,cake2):
	return ((cake1+cake2)**2-abs(cake1-cake2)**2)**0.5
 
while 1:
	try:
		Cakes=map(int,raw_input().split())
		size_max=Cakes.pop(0)
		size_min=999
		for j in range(len(Cakes)):
			cakes=Cakes[:]
			size=cake1=cakes.pop(j)
			while cakes:
				cos,idx=min([(L(cake1,cakes[i])/(cake1+cakes[i]),i) for i in range(len(cakes))])
				cake2=cakes.pop(idx)
				size+=L(cake1,cake2)
				cake1=cake2
			size+=cake1
			size_min=min(size,size_min)
		print "OK" if size_min<=size_max else "NA"
	except:
		break