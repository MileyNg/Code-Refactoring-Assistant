while 1:
	n=input()
	if n==0:break
	h=[0]*10
	for i in range(n):
		h[input()]+=1
	for i in range(10):
		print "*"*h[i] if h[i] else "-"
	