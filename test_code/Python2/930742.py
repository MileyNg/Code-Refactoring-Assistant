n = int(raw_input())
x = map(int,raw_input().split())
x.sort()
for i in xrange(n):
	print x[i],