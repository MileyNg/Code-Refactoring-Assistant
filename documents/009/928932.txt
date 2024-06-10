while True:
	H,W = map(int,raw_input().split())
	if H==W==0:
		break 
	for i in xrange(H):
		print '#' * W
	print