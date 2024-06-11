s = []
while True:
    cmd = input().strip().split()
    if cmd[0] == 'push':
        s.append(cmd[1])
    elif cmd[0] == 'pop':
        print(s.pop())
    else:
        break