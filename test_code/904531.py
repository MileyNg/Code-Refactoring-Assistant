for i in range(int(raw_input())):
    a = str(int(raw_input()) + int(raw_input()))
    print 'overflow' if len(a) > 80 else a