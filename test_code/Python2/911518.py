while 1:
	n=input()
	if n==0:break
	dic={}
	for i in range(n):
		k,v=raw_input().split()
		dic[k]=v
	n=input()
	ans=""
	for i in range(n):
		a=raw_input()[0]
		try:ans+=dic[a]
		except:ans+=a
	print ans
			
	