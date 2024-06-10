from itertools import product

while 1:
    try:
        n = input()
        print len([1 for x in product(range(10), repeat=4) if sum(x) == n])
    except:
        break