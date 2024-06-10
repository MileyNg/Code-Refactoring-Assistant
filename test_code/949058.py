era = [True]*1000001
for i in xrange(2,1000001):
        if era[i-2]:
                for j in xrange(i*2,1000001,i):
                        era[j-2]=False
while True:
        try:
                n = int(raw_input())
                print era[:n-1].count(True)
        except EOFError:
                break