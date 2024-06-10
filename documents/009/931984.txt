s = []
for i in xrange(10):
	s.append(int(raw_input()))
s.sort()
s.reverse()
for i in xrange(3):
	print s[i]