while 1:
	n = input()
	if n == 0: break
	A = sorted(map(int,raw_input().split()))
	c,l = A[0],1
	for i in range(1,n):
		if A[i] == c:
			l += 1
			if l > n/2:
				print c
				break
		else:
			c = A[i]
			l = 1
	else:
		print c if l > n/2 else "NO COLOR"