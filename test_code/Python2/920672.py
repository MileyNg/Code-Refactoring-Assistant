def bmi(a):
	return int(a[0]), abs(22-int(a[2])/((int(a[1])/100.0)**2))
	
while 1:
	n=input()
	if n==0:break
	data=[bmi(raw_input().split()) for i in range(n)]
	print sorted(sorted(data),key=lambda x:x[1])[0][0]