
try:
    a = []
    while True:
        p = int(raw_input())
        if p == 0:
            print a.pop()
        else:
            a.append(p)
except:
    pass