l={}
for i in [1]*input():
	a,n=raw_input().split()
	n=int(n)
	try:l[a]+=n
	except:l[a]=n
for i in sorted(sorted(l.keys()),key=len):print i,l[i]