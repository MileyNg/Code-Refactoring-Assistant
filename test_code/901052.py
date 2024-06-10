def buble(a):
    c = 0
    for i in range(n):
        for j in range(n-1,i,-1):
            if int(a[j]) < int(a[j-1]):
                a[j],a[j-1] = a[j-1],a[j]
                c += 1
    return c
    
while True:
	n = int(raw_input())
	if n == 0: break
	a = [int(raw_input()) for i in range(n)]
	print buble(a)