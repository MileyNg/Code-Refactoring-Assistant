def gcd(a,b):
	return a if b==0 else gcd(b,a%b)

n=input()
if n==2:
	a,b=map(int,raw_input().split())
	g=gcd(a,b)
else:
	a,b,c=map(int,raw_input().split())
	g=gcd(gcd(a,b),c)
for i in range(1,g+1):
		if gcd(i,g)==i:print i