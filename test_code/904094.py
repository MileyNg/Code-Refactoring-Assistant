ref=[63,6,91,79,102,109,125,39,127,111]
while 1:
	try:
		n=input()
		if n==-1:break
		e=0
		for i in range(n):
			a=ref[input()]
			print "{:07b}".format(a^e)
			e=a
	except:
		pass