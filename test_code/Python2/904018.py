while 1:
	n,m,p=map(int,raw_input().split())
	if n==0:break
	x=[input() for i in range(n)]
	if x[m-1]==0:
		print 0
		continue
	print int((100-p)*sum(x)/float(x[m-1]))