for i in range(input()):
	n = list(raw_input())
	n.sort()
	mini = int("".join(sorted(n)))
	mixi = int("".join(sorted(n)[::-1]))
	print mixi - mini