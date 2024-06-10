while 1:
	a=16*float(raw_input())
	if a<0:break
	b=int(a)
	print "NA" if a!=b or a>4095 else "{:08b}.{:04b}".format(b/16,b%16)