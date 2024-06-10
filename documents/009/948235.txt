while True:
	try:
		ans = 0
		n = int(raw_input())
		for i in xrange(10):
			for j in xrange(10):
				for k in xrange(10):
					for l in xrange(10):
						if i+j+k+l == n:
							ans += 1
		print ans
	except EOFError:
		break