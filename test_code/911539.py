while 1:
	n=input()
	if n==0:break
	a=raw_input()
	for r in range(n):
		aa=""
		s=a[0]
		count=1
		for i in range(len(a)-1):
			if a[i]==a[i+1]:
				count+=1
			else:
				aa+=str(count)+s
				count=1
				s=a[i+1]
		aa+=str(count)+s
		a=aa
	print a