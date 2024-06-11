def triangle(a, b, c):
    return a * a + b * b == c * c

t = int(input())
for i in range(t):
    sides = input().split(' ')
    for i in range(3):
        sides[i] = int(sides[i])
    sides.sort()
    r = triangle(sides[0], sides[1], sides[2])
    if (r): print("YES")
    else: print("NO")