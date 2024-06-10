while 1:
	n=input()
	if n==0:break
	print n-sum([int(raw_input()) for i in range(9)])
		