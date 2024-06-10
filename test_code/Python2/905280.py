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
		l=int("".join(map(str,sorted(n)[::-1])))
		s=int("".join(map(str,sorted(n)[n.count("0"):])))
		n=list(str(l-s))
		n=["0"]*(4-len(n))+n
		count+=1