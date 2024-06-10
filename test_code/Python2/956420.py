sm = 0
try:
    while True:
        a = ''
        for c in raw_input():
            a += c if c.isdigit() else ' '
        sm += sum(map(int, a.split()))
except EOFError:
    pass
print sm