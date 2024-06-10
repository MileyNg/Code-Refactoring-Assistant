w = input()
L = range(1, w + 1)
for i in range(input()):
    a, b = map(int, raw_input().split(','))
    L[a - 1], L[b - 1] = L[b - 1], L[a - 1]
print '\n'.join(map(str, L))