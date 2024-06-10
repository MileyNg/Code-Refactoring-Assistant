str = raw_input()
out = []
for c in str:
    a = ord(c)
    if a < 68:
        a += 23
    else:
        a -= 3
    out.append(chr(a))
print(''.join(out))