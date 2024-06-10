while 1:
    try:
        n = bin(input())[:1:-1]
        print ' '.join(str(1 << i) for i in range(len(n)) if n[i] == '1')
    except:
        break