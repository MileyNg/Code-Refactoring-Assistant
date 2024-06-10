def f(n):
    return 1 if n == 1 else f(n - 1) * n
print f(int(raw_input()))