import sys
from decimal import Decimal

(a, b) = [Decimal(i) for i in sys.stdin.readline().split(' ')]

print(a // b,  a % b,  round(a / b, 5))