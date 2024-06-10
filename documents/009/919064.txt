for r in range(input()):
	snake=raw_input()
	L=len(snake)
	if L>5 and snake == ">'" + "="*((L-4)/2) + "#" + "="*((L-4)/2) + "~":
		print "A"
	elif L>5 and snake == ">^" + "Q="*((L-4)/2) + "~~":
		print "B"
	else:
		print "NA"