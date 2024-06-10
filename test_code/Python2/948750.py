while True:
	size = map(int, raw_input().split())
	if sum(size) == 0: break
	size.remove(max(size))
	m = (size[0]**2 + size[1]**2) ** 0.5
	for i in range(input()):
		n = input()
		print "OK" if m < n * 2 else "NA"