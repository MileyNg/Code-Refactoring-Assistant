a='abcdefghijklmnopqrstuvwxyz'
l=[0]*26
while True:
    try:
        text=raw_input()
    except EOFError:
        break
    for i in text:
        ascNum=ord(i.lower())-97
        if ascNum < 0 or 25 < ascNum:
            continue
        l[ascNum]+=1
for i in xrange(26):
    print a[i] + ' : '+str(l[i])