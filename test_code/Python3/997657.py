def digits(n):
    if n < 10: return 1
    c = 0
    while n > 0:
        c += 1
        n = n // 10

    return c

n = int(input())
for i in range(n):
    u = int(input())
    v = int(input())
    s = u + v
    if (digits(u) > 80 or digits(v) > 80 or digits(s) > 80):
        print("overflow")
    else:
        print(s)