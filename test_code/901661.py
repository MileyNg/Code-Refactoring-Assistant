while 1:
	n=int(raw_input())
	if n==0:break
	h=[0 for i in range(7)]
	for i in range(n):
		h[min(6,int(raw_input())/10)] += 1
	for i in h:print i