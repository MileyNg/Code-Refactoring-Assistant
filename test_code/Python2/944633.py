while 1:
    x = raw_input()
    if x == '0': break;
    print sum([int(d) for d in x])