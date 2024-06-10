while 1:
    a,b = map(int,raw_input().split())
    if a == 0 and b==0:
        break
    elif a > b:
        a,b = b,a
        print str(a) + " " + str(b)
    else:
        print str(a) + " " + str(b)