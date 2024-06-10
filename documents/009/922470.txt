while 1:
	x = map(int, raw_input().split())
	if sum(x)==0:
		break;
	for i in sorted(x): print i,
	print