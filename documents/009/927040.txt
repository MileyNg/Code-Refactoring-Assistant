while 1:
	n = input()
	if n == 0: break
	q = sorted([int(raw_input()) for i in range(n)])
	t = [0]*n
	for i in range(n-1):
		t[i + 1] = t[i] + q[i]
	print sum(t)