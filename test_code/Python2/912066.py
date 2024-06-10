dic="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
code=raw_input()
ans=""
for w in code:
	ans+=dic[(dic.index(w)+23)%26]
print ans
		