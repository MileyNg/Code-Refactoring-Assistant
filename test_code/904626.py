try:
    a = [0] * 101
    while True:
        a[int(raw_input())] += 1
except:
    pass
mx = max(a)
for i in range(len(a)):
    if a[i] == mx:
        print i