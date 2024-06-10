a = map(str,sorted(input() for i in range(input()))[:4])
ans = []
for i in range(3):
	for j in range(i+1,4):
		ans.append(int(a[i]+a[j]))
		ans.append(int(a[j]+a[i]))
print sorted(ans)[2]