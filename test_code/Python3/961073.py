def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

x, y = map(int, input().strip().split())
print(gcd(x, y))