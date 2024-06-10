n = input()
li = []
for item in map(int,raw_input().split()):
    if n >= 1:
        li.append(item)
    n -= 1
li.reverse()
for item2 in li:
    print item2,