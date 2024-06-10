dic = {}
while True:
	try:
		word, page = raw_input().split()
		if word in dic.keys():
			dic[word].append(int(page))
			dic[word].sort()
		else:
			dic[word] = [int(page)]
	except:
		dic = sorted(dic.items(), key=lambda x: x[0])
		for d in dic:
			print d[0]
			print " ".join(map(str, d[1]))
		break