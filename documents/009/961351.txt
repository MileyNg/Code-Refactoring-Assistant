n = int(input())
a = input().strip().split()

# bubble sort
b = a[:]
for i in range(n):
    for j in range(n - 1, i, -1):
        if b[j][1] < b[j - 1][1]:
            b[j], b[j - 1] = b[j - 1], b[j]

print(' '.join(b))
print('Stable')

# selection sort
for i in range(n):
    mini = i
    for j in range(i, n):
        if a[j][1] < a[mini][1]:
            mini = j
    a[i], a[mini] = a[mini], a[i]
print(' '.join(a))
print('Stable' if a == b else 'Not stable')