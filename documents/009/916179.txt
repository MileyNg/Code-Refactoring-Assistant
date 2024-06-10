import sys,math
for v in sys.stdin:
	m=int(v)
	for i in range(10):
		if m&(2**i):
			print 2**i,
	print