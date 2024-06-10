p=[[list(raw_input()) for i in range(8)],[],[],[]]
for r in range(3):
	print 90*(r+1)
	for j in range(8):
		p[r+1].append([p[r][-i-1][j] for i in range(8)])
		print "".join(p[r+1][j])