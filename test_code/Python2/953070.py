import re
while 1:
	n,m = map(int,raw_input().split())
	if n == m == 0: break
	R = []
	for i in range(n):
		p,s,d = raw_input().replace("?","[0-9]").split()
		r = re.compile(s+d)
		R.append([r,(1 if p[0] == "p" else 0)])
	ans = []
	for i in range(m):
		s,d,name = raw_input().split()
		for r,p in R[::-1]:
			if r.search(s+d):
				if p:ans.append([s,d,name])
				break
	print len(ans)
	for s,d,name in ans:
		print s,d,name