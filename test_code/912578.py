while 1:
	try:
		a=raw_input()
		cjoi=cioi=0
		for i in range(len(a)-2):
			if   a[i]=="J" and a[i+1]=="O" and a[i+2]=="I":cjoi+=1
			elif a[i]=="I" and a[i+1]=="O" and a[i+2]=="I":cioi+=1
		print cjoi
		print cioi
	except:
		break		