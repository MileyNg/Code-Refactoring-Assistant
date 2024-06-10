import re, sys
ans = 0
for s in sys.stdin.readlines():
    ans += sum(map(int, re.findall('[0-9]+', s)))
print ans