while True:
	m,f,r = map(int,raw_input().split())
	if m==f==r==-1:
		break
	if m == -1 or f == -1 or m+f < 30:
		print 'F'
	elif m+f >= 80:
		print 'A'
	elif 80 > m+f >= 65:
		print 'B'
	elif 65 > m+f >= 50:
		print 'C'
	elif 50 > m+f >= 30:
		if r < 50:
			print 'D'
		else:
			print 'C'