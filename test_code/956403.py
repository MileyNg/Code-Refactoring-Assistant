ct = 0
try:
    while True:
        s = raw_input()
        if len(s) == 1 or s[:(len(s) + 1) / 2] == s[-1:len(s) / 2 - 1:-1]:
            ct += 1
except EOFError:
    pass
print ct