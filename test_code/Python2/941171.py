while 1:
	n = input()
	if n == 0: break
	item = {}
	for i in range(n):
		name,cost = raw_input().split()
		item[name] = int(cost)
	for i in range(input()):
		recipe = raw_input().split()
		cost = sum(item[name] if name in item else 0 for name in recipe[2:])
		item[recipe[0]] = min(cost, item[recipe[0]])
	print item[raw_input()]