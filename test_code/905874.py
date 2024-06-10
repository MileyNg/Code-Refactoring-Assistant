try:
    a = ['A', 'B', 'AB', 'O']
    b = {s: 0 for s in a}
    while True:
        b[raw_input().split(',')[1]] += 1
except EOFError:
    pass
for s in a:
    print b[s]