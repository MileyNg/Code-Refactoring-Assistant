while 1:
	n=input()
	if n==0:break
	ap=bp=0
	for i in range(n):
		a,b=map(int,raw_input().split())
		if a>b:ap+=a+b
		elif a<b:bp+=a+b
		else:ap+=a;bp+=b
	print ap,bp