def isStorage(max_shelf):
	i,cur_shelf,num = 0,0,1
	while i < n:
		if num > m:
			return False
		if cur_shelf + book[i] > max_shelf:
			num += 1
			cur_shelf = 0
		else:
			cur_shelf += book[i]
			i += 1
	else:
		return True
			
while 1:
	m,n = map(int,raw_input().split())
	if m==0: break
	book = [int(raw_input()) for i in range(n)]
	max_shelf = len = sum(book)
	while len:
		len /= 2
		max_shelf -= len if isStorage(max_shelf) else -len
	max_shelf += 6
	while isStorage(max_shelf-1):
		max_shelf -= 1
	print max_shelf