def gcd(a, b):
    while b: a, b = b, a % b
    return a

while True:
    try:
        line = input()
    except:
        break
    a, b = map(int, line.strip().split())
    g = gcd(a, b)
    print(g, a * b // g)