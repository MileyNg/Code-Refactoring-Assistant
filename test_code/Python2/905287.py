while 1:
    n=raw_input()
    if n=="0000": break
    if int(n)%1111==0:
        print "NA"
        continue
    ans = 0
    while n!="6174":
        n="".join(sorted(n))
        n=str(int(n[::-1])-int(n)).zfill(4)
        ans+=1
    print ans