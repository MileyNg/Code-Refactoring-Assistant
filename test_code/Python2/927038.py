while 1:
	n = input()
	if n == 0: break
	q = sorted([int(raw_input()) for i in range(n)])
	t = [0]*n
	for i in range(1,n):
		t[i] = t[i-1] + q[i-1]
	print sum(t)