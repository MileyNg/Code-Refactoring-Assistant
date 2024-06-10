while True:
	m, f, r = map(int, raw_input().split())
	if m + f + r == -3: break

	if m == -1 or f == -1:
		grade = 'F' 
	elif m + f >= 80:
		grade = 'A'
	elif m + f >= 65:
		grade = 'B'
	elif m + f >= 50:
		grade = 'C'
	elif m + f >= 30:
		grade = 'C' if r >= 50 else 'D' 
	elif m + f < 30:
		grade = 'F'
	print grade