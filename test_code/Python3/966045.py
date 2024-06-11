while True:
    try:
        a = list(map(int, input().split(',')))
    except EOFError:
        break
    v1, v2 = a[10], a[11]
    d = [0]
    for i in range(10): d.append(a[i] + d[-1])
    x = d[10] * v1 / (v1 + v2)
    for i in range(10):
        if d[i] < x <= d[i + 1]:
            print(i + 1)
            break