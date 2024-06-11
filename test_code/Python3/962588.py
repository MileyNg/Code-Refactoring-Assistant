while True:
    a, op, b = input().strip().split()
    a, b = int(a), int(b)
    if op == '+': print(a + b)
    if op == '-': print(a - b)
    if op == '*': print(a * b)
    if op == '/': print(a // b)
    if op == '?': break