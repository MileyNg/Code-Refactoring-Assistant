
while 1:
	a, o, b = raw_input().split()
	a = int(a)
	b = int(b)
	if o == "+":
		print a + b
	elif o == "-":
		print a - b
	elif o == "*":
		print a * b
	elif o == "/":
		print a / b
	else:
		break