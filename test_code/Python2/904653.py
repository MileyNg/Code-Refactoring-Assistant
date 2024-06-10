try:
    while True:
        s = bin(int(raw_input()))[::-1]
        a = []
        for i in range(len(s)):
            if s[i] == '1':
                a.append(str(1 << i))
        print ' '.join(a)
except:
    pass