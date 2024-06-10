from sys import stdin

x=[int(input()) for i in range(10)]

x.sort(reverse=True)

for i in x[:3]: print(i)