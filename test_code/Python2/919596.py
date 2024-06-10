for i in xrange(input()):
    base, result, out = 0, 0, 0
    while out != 3:
        cmd = raw_input()
        if cmd == "HIT":
            if base == 3:
                result += 1
            else:
                base += 1
        elif cmd == "HOMERUN":
            result += base + 1
            base = 0
        else:
            out += 1
    print result