while 1:
	card=map(lambda x: min(int(x),10),raw_input().split())
	if card==[0]:break
	s=sum(card)
	for i in range(card.count(1)):
		if s+10>21:
			break
		s+=10
	print s if s<22 else 0