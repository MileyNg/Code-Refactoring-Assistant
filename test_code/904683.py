import sys
for s in sys.stdin:
    while 1:
        p = s.find("@")
        if p==-1: break
        s = s.replace(s[p:p+3], s[p+2] * int(s[p+1]))
    print s[:-1]