encode = {
' ':'101', 
"'":'000000', 
',':'000011', 
'-':'10010001', 
'.':'010001', 
'?':'000001', 
'A':'100101', 
'B':'10011010', 
'C':'0101', 
'D':'0001', 
'E':'110', 
'F':'01001', 
'G':'10011011', 
'H':'010000', 
'I':'0111', 
'J':'10011000', 
'K':'0110', 
'L':'00100', 
'M':'10011001', 
'N':'10011110', 
'O':'00101', 
'P':'111', 
'Q':'10011111', 
'R':'1000', 
'S':'00110', 
'T':'00111', 
'U':'10011100', 
'V':'10011101', 
'W':'000010', 
'X':'10010010', 
'Y':'10010011', 
'Z':'10010000'}

decode = {
"00000":"A",
"00001":"B",
"00010":"C",
"00011":"D",
"00100":"E",
"00101":"F",
"00110":"G",
"00111":"H",
"01000":"I",
"01001":"J",
"01010":"K",
"01011":"L",
"01100":"M",
"01101":"N",
"01110":"O",
"01111":"P",
"10000":"Q",
"10001":"R",
"10010":"S",
"10011":"T",
"10100":"U",
"10101":"V",
"10110":"W",
"10111":"X",
"11000":"Y",
"11001":"Z",
"11010":" ",
"11011":".",
"11100":",",
"11101":"-",
"11110":"'",
"11111":"?"}

while True:
	try:
		string = raw_input()
	except EOFError:
		break		

	e, ans = "", ""
	for s in string:
		e += encode[s]
	tmp = []
	while len(e) > 4:
		tmp.append(e[0:5])
		e = e[5:]
	if len(e) != 0:
		e += '0' * (5 - len(e))
		tmp.append(e)

	for s in tmp:
		ans += decode[s]
	print ans