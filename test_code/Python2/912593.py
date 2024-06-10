while 1:
	try:
		a=raw_input()
		c=0
		for i in range(len(a)-2):
			if a[i:i+3]=="IOI":c+=1
		print a.count("JOI")
		print c
	except:
		break		