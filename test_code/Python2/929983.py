from math import ceil

n = int(raw_input())

debt = 100000

for i in range(n):
    debt = ceil(debt * 1.05 / 1000) * 1000

print int(debt)