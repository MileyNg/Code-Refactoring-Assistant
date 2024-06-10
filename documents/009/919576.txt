while True:
    n = input()
    ans = []
    if n == 0: break
    tmp = [0] * (n+1)
    for i in range(n):
        ans.append(map(int, raw_input().split()))
        ans[i].append(sum(ans[i]))
        for j in range(len(ans[i])):
            tmp[j] += ans[i][j]
    ans.append(tmp)
    for a in ans:
        print "".join(map(lambda x: str(x).rjust(5), a))