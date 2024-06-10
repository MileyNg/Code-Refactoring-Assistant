LIMIT = 10 ** 80
n = int(input())
for i in range(n):
    a = int(input())
    b = int(input())
    c = a + b
    if a >= LIMIT or b >= LIMIT or c >= LIMIT:
        print('overflow')
    else:
        print(c)