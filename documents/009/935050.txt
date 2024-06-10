import fractions
while True:
	try:
		x,y = map(int,raw_input().split())
		print '%d %d' % (fractions.gcd(x,y),x/fractions.gcd(x,y)*y)
	except EOFError:
		break