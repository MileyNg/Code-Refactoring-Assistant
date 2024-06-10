while 1:
    edges = [0] * 101
    try:
        a, b = map(int, raw_input().split())
        edges[a] += 1
        edges[b] += 1
    except EOFError:
        break
    while 1:
        a, b = map(int, raw_input().split())
        if a == b == 0:
            break
        edges[a] += 1
        edges[b] += 1
    if edges[1] % 2 and edges[2] % 2 and all(map(lambda a: a % 2 == 0, edges[3:])):
        print "OK"
    else:
        print "NG"