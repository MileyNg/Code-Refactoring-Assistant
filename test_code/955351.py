ref = "SCHD"
first = 0
while 1:
	try:
		n = input()
		if first: print
		first = 1
	except:
		break
	P = [map(int,raw_input().split()) for i in range(4)]
	H = map(int,raw_input().split())
	for _ in range(n):
		hand = raw_input().replace("A","1").replace("T","10").replace("J","11").replace("Q","12").replace("K","13").split()
		num  = [int(i[:-1]) for i in hand]
		suit = [ref.index(i[-1]) for i in hand]
		ans  = sum(P[suit[i]][num[i]-1] for i in range(5))
		snum = sorted([i - min(num) for i in num])
		same = max(num.count(i) for i in set(num))
		if len(set(suit)) == 1:
			if snum == [0,9,10,11,12]:
				ans *= H[8]
			elif snum == [0,1,2,3,4]:
				ans *= H[7]
			else:
				ans *= H[4]
		elif snum == [0,1,2,3,4] or snum == [0,9,10,11,12]:
			ans *= H[3]
		elif same == 4:
			ans *= H[6]
		elif same == 3:
			if len(set(num)) == 2:
				ans *= H[5]
			else:
				ans *= H[2]
		elif same == 2:
			if len(set(num)) == 3:
				ans *= H[1]
			else:
				ans *= H[0]
		else:
			ans = 0
		print ans