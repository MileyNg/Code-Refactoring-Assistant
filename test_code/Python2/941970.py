c = 1
while 1:
	n = input()
	if n == 0: break
	xy = [map(int,raw_input().split()) for i in range(n)]
	xy.append(xy[0])
	print c,abs(sum(xy[i][0]*xy[i+1][1] - xy[i+1][0]*xy[i][1] for i in range(n)))/2.0
	c += 1
	raw_input()