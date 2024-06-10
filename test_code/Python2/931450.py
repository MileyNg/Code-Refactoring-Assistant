root = [[1,2],[-1,3],[1,-1],[4,5],[5,2],[2,1]]
while 1:
	n = raw_input()
	if n == "#": break
	cur = 0
	for i in n:
		cur = root[cur][int(i)]
		if cur == -1: break
	print "Yes" if cur == 5 else "No"