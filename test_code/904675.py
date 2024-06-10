import sys
for s in sys.stdin:
    n=s.count("@")
    m=0
    x=""
    for c in s[:-1]:
        if m==0:
            if c=="@":m=1
            else:x+=c
        elif m==1:
            a="0123456789".index(c)
            m=2
        elif m==2:
            x+=c*a
            m=0
    print x