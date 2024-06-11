a = [True for i in range(1000000)]
i = 3
while i * i < 1000000:
    for j in range(3 * i, 1000000, 2 * i): a[j] = False
    i += 2

while True:
    try:
        n = int(input())
    except:
        break

    count = int(n >= 2) + sum(a[i] for i in range(3, n + 1, 2))
    print(count)