def f(a,n):
	for j in range(n):
		aa = ""
		s = a[0]
		c = 1
		for i in range(1,len(a)):
			if a[i] == s:
				c += 1
			else:
				aa += str(c) + s
				s = a[i]
				c = 1
		a = aa + str(c) + s
	return a
	
while 1:
	n = input()
	if n == 0: break
	a = raw_input()
	print f(a,n)