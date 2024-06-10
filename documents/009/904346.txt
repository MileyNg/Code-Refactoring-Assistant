while True:
	text = raw_input()
	if text == "-": break
	for i in range(input()):
		h = input()
		text = text[h:] + text[:h]
	print text