while 1:
	n=input()
	if n==0:break
	a,b,c=[0]*n,0,raw_input()
	for i in range(100):
		if c[i]=="M":
			a[i%n]+=1
		elif c[i]=="S":
			b+=1+a[i%n]
			a[i%n]=0
		else:
			a[i%n]+=1+b
			b=0
	print " ".join(map(str,sorted(a))),b