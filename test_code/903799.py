def gcd(a,b):
	return a if b==0 else gcd(b,a%b)

while 1:
	n=input()
	if n==0:break
	s=[map(int,raw_input().split()) for i in range(n)]
	c=1
	for i in s:
		c=c*i[1]/gcd(c,i[1])
	for i in range(n):
		s[i]=c*s[i][0]/s[i][1]
	c=1
	for i in s:
		c=c*i/gcd(c,i)
	for i in s:
		print c/i