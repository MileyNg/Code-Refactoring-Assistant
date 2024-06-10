d=[list(raw_input()) for i in range(8)]
p=[d,[],[],[]]
for r in range(3):
	print 90*(r+1)
	for j in range(8):
		p[r+1].append([p[r][i][j] for i in range(7,-1,-1)])
		print "".join(p[r+1][j])