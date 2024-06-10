while True:
	s = raw_input()
	if s == '-':
		break
	n = int(raw_input())
	for i in xrange(n):
		m = int(raw_input())
		s = s[m:] + s[:m]
	print s