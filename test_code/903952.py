n=input()
while 1:
	p={}
	for i in range(n):
		t=raw_input().split()
		p[t[0]] = [3*int(t[1])+1*int(t[3]),-i]
	for k,v in sorted(p.items(),key=lambda x:x[1])[::-1]:
		print "%s,%d"%(k,v[0])
	n=input()
	if n==0:break
	print