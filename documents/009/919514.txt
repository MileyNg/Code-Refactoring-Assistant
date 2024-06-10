while True:
    ans = []
    data = {}
    r = input()
    if r == 0:
        break
    for i in xrange(r):
        tmp = map(int, raw_input().split())
        
        if tmp[0] in data.keys():
            data[tmp[0]] += tmp[1] * tmp[2]
        else:
            data.update({tmp[0]:tmp[1]*tmp[2]})
    
        if data[tmp[0]] >= 1000000 and tmp[0] not in ans:
            ans.append(tmp[0])
    if len(ans) == 0:
        print "NA"
    else:
        print "\n".join(map(str, ans))