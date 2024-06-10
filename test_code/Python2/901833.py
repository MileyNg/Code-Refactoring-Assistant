while True:
	w = int(raw_input())
	if w == -1: break
	print 3130-125*max(0,min(10,(w-10)))-140*max(0,min(10,(w-20)))-160*max(0,w-30)