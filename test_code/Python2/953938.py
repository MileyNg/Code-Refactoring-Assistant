bus = "0123456789543210123456789"
rbus = "543210"
for i in xrange(input()):
    s, t = raw_input().split()
    if t<s<'6':
        left = rbus.find(s, 0)
        right = rbus.find(t, left)
        print " ".join(rbus[left:right+1])
    else:
        left = bus.find(s, 0)
        right = bus.find(t, left)
        print " ".join(bus[left:right+1])