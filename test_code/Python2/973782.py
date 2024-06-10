o=[]
for c in raw_input():
    o.append(chr((ord(c)+10)%26+65))
print ''.join(o)