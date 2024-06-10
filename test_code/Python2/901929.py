while 1:
	t=int(raw_input())
	if t==0:break
	n=int(raw_input())
	for i in range(n):
		s,f=map(int, raw_input().split())
		t -= f-s
	print t if t > 0 else "OK"