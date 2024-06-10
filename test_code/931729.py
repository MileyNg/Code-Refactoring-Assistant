while 1:
	n = input()
	if n == 0: break
	rslt = [raw_input().replace("2","").split() for i in range(n)]
	rslt = sorted(sorted(rslt, key = lambda x:x.count("1")), key = lambda x:x.count("0"), reverse = True)
	for i in range(n):
		print rslt[i][0]