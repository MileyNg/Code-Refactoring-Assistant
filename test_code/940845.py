def gcd(a,b,i):
	return (a,i) if b == 0 else gcd(b,a%b,i+1)
while 1:
	n,m = sorted(map(int,raw_input().split()),reverse = True)
	if n == m == 0: break
	g,i = gcd(n,m,0)
	print g,i