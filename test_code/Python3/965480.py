def check(a):
    b = [a[0]]
    c = [0]
    for i in range(1, len(a)):
        x = a[i]
        if x < b[-1] and x < c[-1]:
            return False
        elif b[-1] < x < c[-1]:
            b.append(x)
        elif c[-1] < x < b[-1]:
            c.append(x)
        elif b[-1] > c[-1]:
            b.append(x)
        else:
            c.append(x)
    return True

n = int(input())
for i in range(n):
    a = list(map(int, input().split()))
    print('YES' if check(a) else 'NO')