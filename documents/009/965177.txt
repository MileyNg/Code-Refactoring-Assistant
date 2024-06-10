while True:
    try:
        d = int(input())
    except:
        break

    area = d * sum(x * x for x in range(0, 600, d))
    print(area)