import re

def readline():
    return raw_input()

def split8by10(str):
    str = str.rjust(80,'0')
    ss = []
    for s in range(0,len(str),8):
        ss.append(int(str[s:s+8]))
    return ss

def add8by10(a,b):
    c = [0 for i in range(0,10)]
    p = 10**8
    for i in reversed(range(0,10)):
        c[i] += a[i] + b[i]
        if c[i] >= p:
            if i > 0:
                c[i-1] += c[i] // p
            else:
                return None
        c[i] = c[i] % p
    return c

n = int(readline())
for i in range(0,n):
    a = readline()
    b = readline()
    if len(a) > 80 or len(b) > 80:
        print "overflow"
        continue
    a = split8by10(a)
    b = split8by10(b)
    c = add8by10(a,b)
    if c is None:
        print "overflow"
    else:
        print re.sub('^0{,79}',"","".join(map(lambda x:str(x).rjust(8,'0'),c)))