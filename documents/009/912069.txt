a=""
for w in raw_input():
	a+=chr((ord(w)-42)%26+65)
print a