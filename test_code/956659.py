n = input()
for i in xrange(n):
    num = raw_input()
    print int(''.join(sorted(num, reverse=True))) - int(''.join(sorted(num)))