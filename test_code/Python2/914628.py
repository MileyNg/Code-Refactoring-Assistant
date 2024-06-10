from fractions import gcd
def lcm(a,b):
	return a*b/gcd(a,b)
	
while 1:
	inp=map(int,raw_input().split())
	if inp[0]==0:break
	am=zip(inp[::2],inp[1::2])
	count=[0]*3
	for i in range(3):
		a,m=am[i]
		w,c=a%m,1
		while w!=1:
			w=a*w%m
			c+=1
		count[i]=c
	print reduce(lcm,count)