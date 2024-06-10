import sys

c = 0
while True:
    i = int(sys.stdin.readline())
    if (i == 0):
        break
    c+=1
    print("Case " + str(c) + ":", i)