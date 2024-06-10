while True:
	try:
		a,b,c = map(str, raw_input().replace("+","=").split("="))
		i = 1 if a!=a[0]=="X" or b!=b[0]=="X" or c!=c[0]=="X" else 0
		for x in range(i,10):
			if eval((a+"+"+b).replace("X",str(x))) == int(c.replace("X",str(x))):
				print x
				break
		else:
			print "NA"
	except:
		break