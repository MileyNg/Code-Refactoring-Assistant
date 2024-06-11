import sys
import math
from decimal import Decimal

r = Decimal(sys.stdin.readline())
area = r ** Decimal(2) * Decimal(math.pi)
circumference = r * Decimal(2) * Decimal(math.pi)

print(round(area, 5), round(circumference, 5))