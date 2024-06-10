while 1:
    n, x = map(int, raw_input().split())
    if n == x == 0:
        break
    ret = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                if i + j + k == x:
                    ret += 1
    print ret