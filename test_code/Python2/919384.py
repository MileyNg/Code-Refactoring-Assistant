def bowling(game):
	game=map(int,game.split())
	score,thrw=0,1
	for flame in range(10):
		if game[thrw]==10:
			score+=sum(game[thrw:thrw+3])
			thrw+=1
		elif game[thrw]+game[thrw+1]==10:
			score+=10+game[thrw+2]
			thrw+=2
		else:
			score+=sum(game[thrw:thrw+2])
			thrw+=2
	return game[0],score
	
while 1:
	n=input()
	if n==0:break
	ls=[bowling(raw_input()) for i in range(n)]
	for k,s in sorted(sorted(ls),key=lambda x:x[1],reverse=1):
		print k,s