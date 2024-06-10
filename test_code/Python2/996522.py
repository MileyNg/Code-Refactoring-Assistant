station = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
while True:
    n = input()
    if n==0:
        break
    k = map(int, raw_input().split())
    s = raw_input()
    print "".join(station[(station.find(s[i])-k[i%n]+52)%52] for i in xrange(len(s)))