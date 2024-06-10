a = [['the'], ['this'], ['that']]
for i in range(25):
    for b in a:
        s = ''
        for c in b[-1]:
            s += chr((ord(c) - ord('a') + 1) % 26 + ord('a'))
        b.append(s)


def f(s):
    for b in a:
        for i in range(26):
            if s.find(b[i]) != -1:
                t = ''
                for c in s:
                    if c.isalpha():
                        t += chr((ord(c) - ord('a') - i + 26) % 26 + ord('a'))
                    else:
                        t += c
                return t
    return None

try:
    while True:
        print f(raw_input())
except:
    pass