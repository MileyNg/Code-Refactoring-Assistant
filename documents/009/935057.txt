while 1:
	n = input()
	if n == 0: break
	s = [sum(map(int,raw_input().split())) for i in range(n)]
	print max(s),min(s)
	