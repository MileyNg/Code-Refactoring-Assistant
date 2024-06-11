from collections import Counter

current = last_month = Counter()
this_month = Counter()

while True:
    try:
        s = input()
    except EOFError:
        break
    if s:
        customer, day = map(int, s.split(','))
        current[customer] += 1
    else:
        current = this_month

for i in last_month.keys():
    if i in this_month:
        print(i, last_month[i] + this_month[i])