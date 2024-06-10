while 1:
	z3=m=input()**3
	if z3==0:break
	x=0
	while 1:
		x+=1
		x3=x**3
		y=int((z3-x3)**(1/3.))
		if y<x:break
		n=z3-x3-y**3
		if n<m:m=n
	print m