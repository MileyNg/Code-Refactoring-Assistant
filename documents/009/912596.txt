while 1:
	n=input()
	if n==0:break
	m=input()
	a=raw_input()
	P="I"+"OI"*n
	l=1+2*n
	c=0
	for i in range(m-l+1):
		if a[i:i+l]==P:c+=1
	print c
	