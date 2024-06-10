def SumOfDiv(n):
	i = 2
	ans = 1
	while i*i <= n:
		c = 0
		while n%i==0:
			n /= i
			c += 1
		if c > 0:
			ans *= (i**(c+1)-1)/(i-1)
		i += 1
	if n > 1:
		ans *= (1+n)
	return ans
	
while 1:
	n = input()
	if n == 0: break
	d = SumOfDiv(n) - n
	if d == n:
		print "perfect number"
	elif d < n:
		print "deficient number"
	else:
		print "abundant number"