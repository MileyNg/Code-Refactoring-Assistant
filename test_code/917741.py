while 1:
	n=input()
	if n==0:break
	hmax=7500
	block=[map(int,raw_input().split()) for i in range(n)]
	field=[[0]*5 for i in range(hmax)]
	top=[0]*5
	for d,p,q in block:
		if d==1:
			h=max(top[q-1:q-1+p])
			field[h][q-1:q-1+p]=[1]*p
			top[q-1:q-1+p]=[max(top)+1]*p
		else:
			h=top[q-1]
			for i in range(p):
				field[h+i][q-1]=1
			top[q-1]=h+p
		h=0
		while 1:
			if field[h]==[1]*5:
				del field[h]
				top=[x-1 for x in top]
			elif field[h]==[0]*5:
				break
			else:
				h+=1
		for w in range(5):
			for h in range(top[w]-1,-2,-1):
				if field[h][w]==1 or h==-1:
					top[w]=h+1
					break
	print sum([sum(field[h]) for h in range(max(top))])