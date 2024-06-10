while True:
	try:
		d = input()
		area = 0
		for i in range(0,600,d):
			area += d * (i**2)
		print area
	except:
		break