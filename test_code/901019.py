def f(n):
	c=0
	while n>1:
		if n%2:n=3*n+1
		else:n /= 2
		c += 1
	print c
	
while 1:
	n=input()
	if n==0:break
	f(n)