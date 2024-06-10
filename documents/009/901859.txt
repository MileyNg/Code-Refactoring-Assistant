while 1:
	n=input()
	if n==0:break
	for i in range(n):
		m,e,j=map(int, raw_input().split())
		a=m+e+j
		if 100 in [m,e,j] or m+e>179 or a>239:print"A"
		elif a>209 or (a>149 and max(m,e)>79):print"B"
		else:print"C"