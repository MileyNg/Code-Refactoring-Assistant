while True:
    n = int(input())
    if n == 0: break

    count = 0
    x = 5
    while x <= n:
        count += n // x
        x *= 5
    print(count)