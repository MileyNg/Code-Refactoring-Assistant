n = input()
for i in range(n):
    m = input() + input()
    if len(str(m)) >= 81:
        print 'overflow'
    else:
        print m