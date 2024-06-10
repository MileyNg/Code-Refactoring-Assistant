while 1:
	n=input()
	if n==0:break
	s=[map(int,raw_input().split()) for i in range(n)]
	for i in range(n):
		s[i].append(4*s[i][1]+9*s[i][2]+4*s[i][3])
	r=map(int,raw_input().split())
	flag=0
	for i in s:
		if i[1]<=r[0] and i[2]<=r[1] and i[3]<=r[2] and i[4]<=r[3]:
			print i[0]
			flag=1
	if flag==0:print "NA"