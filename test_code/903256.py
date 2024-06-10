while 1:
	try:
		h=[input() for i in [1]*5]
		l=set(h)
		if 1 in h and 2 in h:w=1
		if 1 in h and 3 in h:w=3
		if 2 in h and 3 in h:w=2
		if len(l)==3 or len(l)==1:
			for i in h:print 3
		else:
			for i in h:print 1 if i==w else 2
	except:
		break