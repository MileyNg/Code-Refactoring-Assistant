def decode(string, num):
    a, z = ord('a'), ord('z')
    return ''.join([chr(((ord(s) - a) + num) % 26 + a) if a <= ord(s) <= z else s for s in string])


while 1:
    try:
        line = raw_input()
        for i in range(26):
            tmp = decode(line, i)
            for x in tmp.split():
                x = x.strip('.')
                if 'this' in x or 'the' in x or 'that' in x:
                    print tmp
                    break
    except:
        break