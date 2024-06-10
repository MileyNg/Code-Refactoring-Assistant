L = []
while 1:
    try:
        n = input()
        if n == 0:
            print L.pop()
        else:
            L.append(n)
    except:
        break