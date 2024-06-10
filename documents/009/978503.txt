n = int(input())
for i in range(n):
    s = sorted(input())
    print(int(''.join(s[::-1])) - int(''.join(s)))