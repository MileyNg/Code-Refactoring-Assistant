while 1:
	n=input()
	if n==0:break
	for i in range(n):
		a,b,c,d,x,y,z,w=map(int,raw_input().split())
		print a*x-b*y-c*z-d*w,a*y+b*x+c*w-d*z,a*z-b*w+c*x+d*y,a*w+b*z-c*y+d*x