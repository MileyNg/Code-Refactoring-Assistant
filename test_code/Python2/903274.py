while 1:
	try:
		h=[input() for i in [1]*5]
		if 1 in h and 2 in h:w=1
		elif 1 in h:w=3
		else:w=2
		for i in h:
			if len(set(h))!=2:print 3
			else:print 1 if i==w else 2
	except:break