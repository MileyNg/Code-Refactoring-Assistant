a = raw_input().split()
dic = {}
mx = ''
for s in a:
    dic[s] = dic.get(s, 0) + 1
    if len(s) > len(mx):
        mx = s
print max(dic.items(), key=lambda p: p[1])[0], mx