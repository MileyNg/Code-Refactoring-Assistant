while 1:
    try:
        n=input()
        if n==0:break
        l=m=0
        for i in [1]*n:
            p,d1,d2=map(int,raw_input().split())
            d=d1+d2
            if d>m:l,m=p,d
        print l,m
    except SyntaxError:
        pass