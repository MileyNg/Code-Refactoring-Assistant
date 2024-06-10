text = raw_input()
ans = ""
for s in text:
	if s.isalpha(): 
		ans += s.upper() if s.islower() else s.lower()
	else:
		ans += s
print ans