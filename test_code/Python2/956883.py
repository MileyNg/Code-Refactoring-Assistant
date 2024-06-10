while 1:
    try:
        line = raw_input()
    except EOFError:
        break
    i = 0
    ret = ''
    while i < len(line):
        if line[i] == '@':
            ret += line[i + 2] * int(line[i + 1])
            i += 3
        else:
            ret += line[i]
            i += 1
    print ret