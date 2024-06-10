try:
    a = 'A'
    while True:
        p, q = raw_input().split(',')
        if p == a:
            a = q
        elif q == a:
            a = p
except EOFError:
    pass
print a