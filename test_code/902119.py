c = [0] * 200
while 1:
    try:
        for x in raw_input().lower():
            c[ord(x)] += 1
    except EOFError:
        for i in range(ord('a'), ord('z') + 1):
            print "%s : %d" % (chr(i), c[i])
        break