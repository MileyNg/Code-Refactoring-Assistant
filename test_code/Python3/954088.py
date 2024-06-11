n = int(input())
a = input().split(" ")
a.reverse()

for i in range(0,n):
	if i==n-1:
		print(a[i])
	else :
		print(a[i],end=' ')