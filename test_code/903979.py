while 1:
	n3=mn=input()**3
	if n3==0:break
	i=0
	while 1:
		i+=1
		i3=i**3
		j3=int((n3-i3)**(1/3.0))**3
		if j3<i3:break
		m=n3-i3-j3
		if m<mn:mn=m
	print mn