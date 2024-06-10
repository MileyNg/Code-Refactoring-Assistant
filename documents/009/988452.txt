from sys import stdin

count = int(stdin.readline())
ns = [int(n) for n in stdin.readline().split(' ')]
minimum = None
maximum = None
total = 0

for n in ns:
    if minimum == None or minimum > n:
        minimum = n
    if maximum == None or maximum < n:
        maximum = n

    total += n

print(minimum, maximum, total)