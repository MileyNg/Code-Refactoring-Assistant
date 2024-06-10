import math
print reduce(lambda a, b: int(math.ceil(a * 1.05 / 1000)) * 1000, range(input()), 100000)