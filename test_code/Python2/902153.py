stack = []
while 1:
    L = raw_input().split()
    if L[0] == 'quit':
        break
    if L[0] == 'push':
        stack.append(L[1])
    elif L[0] == 'pop':
        print stack.pop()
    