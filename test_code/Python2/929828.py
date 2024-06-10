n = input()
i = 0
while 1:
	if n>=i and n-i == int(str(n-i)[::-1]):
		print n-i
		break
	elif n+i == int(str(n+i)[::-1]):
		print n+i
		break
	i += 1