mountains = []
while 1:
    try:
        mountains.append(input())
    except EOFError:
        break
mountains.sort()
print mountains[-1] - mountains[0]