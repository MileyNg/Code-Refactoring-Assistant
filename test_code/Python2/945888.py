n = input()
m = input()
ans = m
for i in range(n):
	a,b = map(int,raw_input().split())
	m = m + a - b
	if m < 0:
		ans = 0
		break
	ans = max(ans,m)
print ans