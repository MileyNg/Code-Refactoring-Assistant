a = raw_input()
ans = 0
for i in range(input()):
	r = raw_input()
	if a in r + r[:len(a)]:
		ans += 1
print ans