while 1:
	exps=raw_input().split("|")
	if exps[0]=="#":break
	for exp in exps:
		v=1
		lit=exp[1:-1].split("&")
		for i in range(2):
			for j in range(i+1,3):
				if (lit[i]=="~"+lit[j]) or ("~"+lit[i]==lit[j]):
					v=0
		if v:
			print "yes"
			break
	else:
		print "no"
		