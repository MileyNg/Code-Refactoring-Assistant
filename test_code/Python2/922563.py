char = raw_input().split()
ans = []
for c in char:
	if ',' in c:
		c = c.replace(',','')
	elif '.' in c:
		c = c.replace('.','')
	if 3 <= len(c) <= 6:
		ans.append(c)
print " ".join(ans)