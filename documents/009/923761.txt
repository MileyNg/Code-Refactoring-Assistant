import sys
readline = sys.stdin.readline

D = {
	"N": (0, 1),
	"E": (1, 0),
	"S": (0, -1),
	"W": (-1, 0),
}

while True:
	n = int(readline())
	if n == 0: break
	gems = {tuple(int(x) for x in readline().split()) for i in xrange(n)}
	x = 10
	y = 10
	try:
		gems.remove((x, y))
	except KeyError:
		pass
	for i in xrange(int(readline())):
		c, cnt = readline().split()
		dx, dy = D[c]
		for j in xrange(int(cnt)):
			x += dx
			y += dy
			try:
				gems.remove((x, y))
			except KeyError:
				pass
	print "No" if gems else "Yes"