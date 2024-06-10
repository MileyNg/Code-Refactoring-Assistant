while 1:
	n = input()
	if n == 0: break
	que = sorted([int(raw_input()) for i in range(n)])
	print sum([sum(que[:i]) for i in range(1,n)])