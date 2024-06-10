l={}
for i in [1]*input():
	a,n=map(str,raw_input().split())
	try:l[a]+=int(n)
	except:l[a]=int(n)
for k,v in sorted(sorted(l.items(),key=lambda x:x[0]),key=lambda x:len(x[0])):print k,v