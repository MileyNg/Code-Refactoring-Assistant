try:
    while True:
        a, b, n = map(int, raw_input().split())
        print sum(map(int, str(a * 10 ** n / b)[-n:]))
except EOFError:
    pass