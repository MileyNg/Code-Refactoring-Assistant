W = raw_input().lower()
ret = 0
while 1:
    text = raw_input().split()
    if text[0] == "END_OF_TEXT":
        break
    for t in text:
        if W == t.lower():
            ret += 1
print ret