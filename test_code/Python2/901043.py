while True:
	n = int(raw_input())
	if n == 0: break
	a = []
	for i in range(n):
		d = map(int, raw_input().split())
		t = 60*(d[1]+d[3]+d[5]+d[7])+d[2]+d[4]+d[6]+d[8]
		a.append([d[0],t])
	a = sorted(a,key=lambda x:x[1])
	print "{}\n{}\n{}".format(a[0][0],a[1][0],a[-2][0])