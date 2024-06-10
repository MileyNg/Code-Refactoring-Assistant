import sys
while 1:
	for i in range(3):
		g=raw_input()
		if g=="0":sys.exit()
		g=g[1:]+g[-1]
		print g.count("A"),g.count("B")