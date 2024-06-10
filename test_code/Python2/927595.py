while True:
	a,op,b = map(str,raw_input().split())
	if op =='?':
		break
	a,b= int(a),int(b)
	if op == '+':
		print a+b
	elif op == '-':
		print a-b
	elif op == '*':
		print a*b
	else:
		print a/b