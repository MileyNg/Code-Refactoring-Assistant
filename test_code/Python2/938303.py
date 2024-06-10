while 1:
	n = input()
	if n == 0: break
	a = sorted(map(int,raw_input().split()))[::-1]
	s = sum(a)
	L = [0]
	for i in a:
		L += [i+j for j in L if j < s/2]
	print min(abs(s-2*i) for i in L)