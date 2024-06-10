text = ""
ans = [0 for i in range(26)]
while True:
	try:
		text += raw_input().lower()
	except:
		for s in text:
			if s.isalpha():
				ans[ord(s)-97] += 1
		for j in range(len(ans)):
			print "{} : {}".format(chr(j+97),ans[j])
		break