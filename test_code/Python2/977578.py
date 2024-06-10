n = int(raw_input())
res = 100000
for i in range(0,n):
    res = res * 1.05
    if res % 1000:
        res += 1000
    res = int(res/1000)*1000
print res