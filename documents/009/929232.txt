while True:
	H,W = map(int,raw_input().split())
	if H==W==0:
		break
	for i in xrange(H):
		if i==0 or i==H-1:
			print '#'*W
		else:
			print '#' + '.'*(W-2) + '#'
	print