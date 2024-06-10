while 1:
	n=input()
	if n==0:break
	games=[map(int,raw_input().split()) for i in range(n)]
	ls=[]
	for game in games:
		score,flame,thrw=0,1,1
		while thrw<len(game):
			if flame<10:
				if game[thrw]==10:
					score+=sum(game[thrw:thrw+3])
					thrw+=1
				elif game[thrw]+game[thrw+1]==10:
					score+=sum(game[thrw:thrw+3])
					thrw+=2
				else:
					score+=game[thrw]+game[thrw+1]
					thrw+=2
				flame+=1
			else:
				score+=game[thrw]
				thrw+=1
		ls.append([game[0],score])
	for k,s in sorted(sorted(ls),key=lambda x:x[1],reverse=True):
		print k,s