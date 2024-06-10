def collatz(n):
	c = 0
	while n > 1:
		if n%2:	n = 3*n+1
		else: n /= 2
		c += 1
	return c
	
while True:
	n = int(raw_input())
	if n == 0: break
	print collatz(n)