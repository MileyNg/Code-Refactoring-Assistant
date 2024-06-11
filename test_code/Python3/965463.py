import sys

for line in sys.stdin:
    n = int(line)
    print(' '.join(map(str, [2**i for i, b in enumerate(bin(n)[-1:1:-1]) if b == '1'])))