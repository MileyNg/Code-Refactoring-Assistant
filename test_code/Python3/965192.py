a = 'abcdefghijklmnopqrstuvwxyz'

while True:
    try:
        s = input()
    except:
        break
    for n in range(1, 27):
        t = s.translate(str.maketrans(a, a[n:] + a[:n]))
        if 'the' in t or 'this' in t or 'that' in t: break
    print(t)