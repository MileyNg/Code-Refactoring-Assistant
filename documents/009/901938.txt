while 1:
	n=input()
	if n==0:break
	y=input()
	mx=0
	for i in range(n):
		b,r,t=map(int,raw_input().split())
		m=(1+y*float(r)/100) if t==1 else (1+float(r)/100)**y
		if m>mx:mx,a=m,b
	print a