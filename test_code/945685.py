while 1:
	n = input()
	if n == 0: break
	ans = 0
	for i in range(96):
		tri = i*(i+1)*(i+2)/6
		if tri > n: break
		ans = max(ans,int((n-tri)**(1.0/3)+1e-8)**3 + tri)
	print ans