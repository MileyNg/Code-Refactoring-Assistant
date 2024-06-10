while 1:
	n = input()
	if n == 0: break
	ans = 0
	for i in range(96):
		t = i*(i+1)*(i+2)/6
		if t > n: break
		ans = max(ans,int((n-t)**(1.0/3)+1e-8)**3 + t)
		if ans == n: break
	print ans