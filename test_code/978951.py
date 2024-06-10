first = True
while True:
    a, b = map(int, input().split())
    if a == b == 0: break

    if not first: print()
    first = False

    count = 0
    for y in range(a, b + 1):
        if y % 400 == 0 or y % 4 == 0 and y % 100 != 0:
            count += 1
            print(y)
    if count == 0: print('NA')