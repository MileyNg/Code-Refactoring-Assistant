while 1:
    m=raw_input()
    if m=="END OF INPUT":break
    print "".join(str(len(w)) for w in m.split(" "))