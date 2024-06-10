while 1:
    x = raw_input()
    if x == '0': break;
    print sum(int(s) for s in x)