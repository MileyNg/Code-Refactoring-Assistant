p=[list(raw_input()) for i in range(8)]
plist=[p,[],[],[]]
for r in range(3):
	for j in range(8):
		plist[r+1].append([plist[r][i][j] for i in range(7,-1,-1)])
	print 90*(r+1)
	for i in range(8):
		print "".join(plist[r+1][i])