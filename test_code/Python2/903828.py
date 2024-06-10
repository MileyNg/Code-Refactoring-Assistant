while 1:
	try:
		n=input()
		p=sorted(map(int,raw_input().split()))
		print sum([sum(p[:i+1]) for i in range(n)])
	except:
		break