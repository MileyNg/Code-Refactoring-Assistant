n = int(input())
sa = sb = 0
for i in range(n):
    a, b = input().strip().split()
    if a > b:
        sa += 3
    elif a < b:
        sb += 3
    else:
        sa += 1
        sb += 1
print(sa, sb)