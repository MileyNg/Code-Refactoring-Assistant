import sys,math
for v in sys.stdin:
	v=float(v[:-1])
	print int(math.ceil(v**2/2/9.8/5))+1