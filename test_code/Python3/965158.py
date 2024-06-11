while True:
    try:
        n = int(input())
    except:
        break

    a = [0 for i in range(n + 1)]

    # sieve
    i = 3
    while i * i <= n:
        for j in range(3 * i, n + 1, 2 * i): a[j] = 1
        i += 2

    count = int(n >= 2)
    count += sum(a[i] == 0 for i in range(3, n + 1, 2))
    print(count)