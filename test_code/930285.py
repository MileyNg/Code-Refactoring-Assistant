s = raw_input()
l =[]
while True:
	x = raw_input()
	if x == 'END_OF_TEXT':
		break
	l += x.lower().split()
print l.count(s)