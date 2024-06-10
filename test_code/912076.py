while 1:
	a,b,c=map(int,raw_input().split())
	if a==0:break
	t=[2]*(a+b+c)
	m=input()
	tests=sorted([map(int,raw_input().split()) for i in range(m)],key=lambda x:x[3])[::-1]
	for test in tests:
		na,nb,nc=test[0]-1,test[1]-1,test[2]-1
		if test[3]==1:
			t[na],t[nb],t[nc]=1,1,1
		else:
			ls=[t[na],t[nb],t[nc]]
			if ls.count(1)==2 and 2 in ls:
				if t[na]==2:t[na]=0
				if t[nb]==2:t[nb]=0
				if t[nc]==2:t[nc]=0
	for i in t:
		print i