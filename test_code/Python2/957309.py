from itertools import starmap
from operator import mul

items = []
while 1:
    try:
        price, amount = map(int, raw_input().split(','))
    except EOFError:
        break
    items.append((price, amount))
print sum(starmap(mul, items))
print int(round(1.0 * sum(map(lambda a: a[1], items)) / len(items)))