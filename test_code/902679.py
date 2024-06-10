l={}
for i in [1]*input():
	a,n=map(str,raw_input().split())
	try:l[a]+=int(n)
	except:l[a]=int(n)
for i in sorted(sorted(l.keys()),key=len):print i,l[i]