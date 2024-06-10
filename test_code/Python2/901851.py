while 1:
	n=input()
	if n==0:break
	h=[0]*10
	for i in range(n):
		h[int(raw_input())]+=1
	for i in h:
		print "*"*i if i else "-"