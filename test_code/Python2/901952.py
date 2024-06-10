for i in range(input()):
	x,y,b,p=map(int,raw_input().split())
	print min(x*b+y*p,(x*max(b,5)+y*max(p,2))*8/10)