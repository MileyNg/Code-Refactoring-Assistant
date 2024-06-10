def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def lcm(a, b):
    return a / gcd(a, b) * b

try:
    while True:
        a, b = map(int, raw_input().split())
        print gcd(a, b), lcm(a, b)
except:
    pass