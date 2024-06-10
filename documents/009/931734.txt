while 1:
	n = input()
	if n == 0: break
	rslt = sorted(sorted([raw_input().replace("2","") for i in range(n)], key = lambda x:x.count("1")), key = lambda x:x.count("0"), reverse = 1)
	for i in range(n): print rslt[i][0]