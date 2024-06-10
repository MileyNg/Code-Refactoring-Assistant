tarou = 0
hanako = 0
for i in xrange(input()):
    a, b = raw_input().split()
    if a > b:
        tarou += 3
    elif a < b:
        hanako += 3
    else:
        tarou += 1
        hanako += 1
print tarou, hanako