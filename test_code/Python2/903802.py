def g(a,b):
	return a if b==0 else g(b,a%b)

while 1:
	n=input()
	if n==0:break
	s=[map(int,raw_input().split()) for i in [1]*n]
	t=c=1
	for i in s:t*=i[1]/g(t,i[1])
	for i in range(n):
		s[i]=t*s[i][0]/s[i][1]
		c*=s[i]/g(c,s[i])
	for i in s:print c/i