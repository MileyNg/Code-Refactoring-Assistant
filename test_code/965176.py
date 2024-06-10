stack = []

while True:
    try:
        n = int(input())
    except:
        break

    if n:
        stack.append(n)
    else:
        print(stack.pop())