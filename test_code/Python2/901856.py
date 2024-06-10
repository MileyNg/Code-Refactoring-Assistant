while 1:
	n=input()
	if n==0:break
	for i in range(n):
		m,e,j=map(int, raw_input().split())
		if 100 in [m,e,j] or m+e>=180 or m+e+j>=240:print "A"
		elif m+e+j>=210 or (m+e+j>=150 and max(m,e)>=80):print "B"
		else:print"C"