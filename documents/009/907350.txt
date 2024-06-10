try:
    while True:
        a = map(int, raw_input().split())
        if len([i for i in range(1, 11) if i not in a and sum(a[:2]) + i <= 20]) > 3:
            print 'YES'
        else:
            print 'NO'
except EOFError:
    pass