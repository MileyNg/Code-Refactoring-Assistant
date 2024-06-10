nl = []; c = 0;
INF = 10**9+7; ans = 0;
while True:
    try:
        l = map(int, raw_input().split(','))
        nl.append(l)
        c += 1
    except EOFError:
        break
cn = (c + 1)/2
dp1, dp2 = [0], [0]
for i in xrange(1,cn):
    dp1 = [ max(dp1[j-1]+nl[i-1][j-1] if j>0 else 0, dp1[j]+nl[i-1][j] if j<i else 0) for j in xrange(i+1)]
for i in xrange(1,cn):
    dp2 = [ max(dp2[j-1]+nl[c-i][j-1] if j>0 else 0, dp2[j]+nl[c-i][j] if j<i else 0) for j in xrange(i+1)]
for i in xrange(cn):
    ans = max(ans, dp1[i] + dp2[i] + nl[cn-1][i])
print ans