while 1:
	n = input()
	if n == 0: break
	a = map(int,raw_input().split())
	s = sum(a)
	ref = [0]
	for i in a:
		ref += [i+j for j in ref if j < s/2]
	print min(abs(s-2*i) for i in ref)