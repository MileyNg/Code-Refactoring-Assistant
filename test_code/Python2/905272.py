while 1:
	n=list(raw_input())
	if n==["0"]*4: break
	elif n[0]==n[1]==n[2]==n[3]:
		print "NA"
		continue
	count=0
	while 1:
		if n==["6","1","7","4"]:
			print count
			break
		l=sorted(n)[::-1]
		s=sorted(n)[n.count("0"):]
		n=list(str(int("".join(map(str,l)))-int("".join(map(str,s)))))
		for i in range(4-len(n)):
			n.insert(0,"0")
		count+=1