def stuck(array):
	order=[]
	while array:
		r = len(array)
		w = sum([array[i][1] for i in range(r)])
		mx = 0
		for i in range(r):
			if array[i][2] >= w-array[i][1] and array[i][1] > mx:
				mx = array[i][1]
				id = i
		order.append(array.pop(id)[0])
	return order

def change(a):
	return a[0],int(a[1]),int(a[2])
	
while 1:
	n = input()
	if n == 0:break
	lunch = [change(raw_input().split()) for i in range(n)]
	ans = stuck(lunch)
	for i in range(n):
		print ans[i]