
def tr(a,b,c):
	l = a*a
	m = b*b
	n = c*c
	if(l+m==n or m+n==l or l+n==m):
		print "YES"
	else:
		print "NO"
for i in range(int(raw_input())):
	(l,m,n) = map(int,raw_input().split())
	tr(l,m,n)