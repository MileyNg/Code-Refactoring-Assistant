n1 = n2 = input()
while 1:
	if n1 > -1 and n1 == int(str(n1)[::-1]):
		print n1
		break
	elif n2 == int(str(n2)[::-1]):
		print n2
		break
	n1 -= 1
	n2 += 1