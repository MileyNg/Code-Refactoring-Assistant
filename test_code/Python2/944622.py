while 1:
    n = raw_input()
    if n == '0': break;
    print reduce(lambda x,y: x+int(y), n, 0)