from fractions import gcd
while 1:
    try:
        a, b = map(int, raw_input().split())
        print gcd(a, b), a * b / gcd(a, b)
    except:
        break