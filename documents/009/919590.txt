for i in range(input()):
    base = 0
    result = 0
    out = 0
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
        elif cmd == "OUT":
            out += 1
    print result