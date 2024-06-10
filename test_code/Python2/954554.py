import re
while 1:
	n,m = map(int,raw_input().split())
	if n ==0: break
	prize = []
	for i in range(n):
		num,money = raw_input().replace("*","[0-9]").split()
		prize.append([re.compile(num),int(money)])
	ans = 0
	for i in range(m):
		lot = raw_input()
		for num,money in prize:
			if num.search(lot):
				ans += money
				break
	print ans