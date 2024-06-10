ref=["abcde","fghij","klmno","pqrst","uvwxy","z.?! "]
while 1:
	try:
		inp=raw_input()
		if len(inp)%2==1:
			print "NA"
			continue
		msg=""
		for i in range(0,len(inp),2):
			r,c=map(int,inp[i:i+2])
			if 1<=r<=6 and 1<=c<=5:
				msg+=ref[r-1][c-1]
			else:
				msg="NA"
				break
		print msg
	except:
		break