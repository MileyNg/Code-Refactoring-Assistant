n, m = map(int, raw_input().split())
a = [[input(),i] for i in xrange(n)]
t = [[0,i+1] for i in xrange(n)]
for b in [input() for i in xrange(m)]:
    t[filter(lambda x: x[0]<=b, a)[0][1]][0] += 1
print sorted(t, reverse=True)[0][1]