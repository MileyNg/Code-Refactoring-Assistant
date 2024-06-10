while 1:
	n=input()
	if n==0:break
	games=[map(int,raw_input().split()) for i in range(n)]
	ls=[]
	for game in games:
		score,thrw=0,1
		for flame in range(10):
			if game[thrw]==10:
				score+=sum(game[thrw:thrw+3])
				thrw+=1
			elif game[thrw]+game[thrw+1]==10:
				score+=10+game[thrw+2]
				thrw+=2
			else:
				score+=game[thrw]+game[thrw+1]
				thrw+=2
		else:
			ls.append([game[0],score])
	for k,s in sorted(sorted(ls),key=lambda x:x[1],reverse=True):
		print k,s