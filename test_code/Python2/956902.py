def encode(string, a, b):
    ret = ''
    for x in string:
        tmp = ord(x) - ord('a')
        if 0 <= tmp <= 26:
            ret += chr((a * tmp + b) % 26 + ord('a'))
        else:
            ret += x
    return ret


n = input()
for t in xrange(n):
    line = raw_input()
    for i in xrange(1, 10000):
        f = False
        if not (26 % i and i % 26):
            continue
        for j in xrange(26):
            txt = encode(line, i, j)
            if 'that' in txt or 'this' in txt:
                print txt
                f = True
                break
        if f:
            break