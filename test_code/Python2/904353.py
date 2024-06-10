a = []
try:
    while True:
        a.append(int(raw_input()))
except:
    pass
a.sort()
for i in range(-1, -4, -1):
    print a[i]