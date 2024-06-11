n = int(input())
p1 = p2 = 0
for i in range(n):
    s1, s2 = input().strip().split()
    if s1 > s2:
        p1 += 3
    elif s1 < s2:
        p2 += 3
    else:
        p1 += 1
        p2 += 1
print(p1, p2)