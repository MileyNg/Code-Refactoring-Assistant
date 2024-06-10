while 1:
	n = input()
	if n == 0:break
	r = sorted(sorted([raw_input().replace("2","") for i in range(n)],key = lambda x:x.count("1")),key = lambda x:x.count("0"),reverse = 1)
	for i in r:print i[0]