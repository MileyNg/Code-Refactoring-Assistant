while True:
	n = int(raw_input())
	if n == 0: break
	data = {}
	order = []
	for i in range(n):
		id,price,quant = map(int, raw_input().split())
		if id in data:
			data[id] += price*quant
		else:
			data[id] = price*quant
			order.append(id)
	if max(data.values()) < 1000000:
		print "NA"
	else:
		for k in order:
			if data[k] >= 1000000: print k
	