def L(cake1,cake2):
    return ((cake1+cake2)**2-abs(cake1-cake2)**2)**0.5
 
while 1:
    try:
        Cakes=map(int,raw_input().split())
        size_max=Cakes.pop(0)
        Cakes=sorted(Cakes)[::-1]
        size_min=999
        for j in range(len(Cakes)):
            cakes=Cakes[:]
            box=[cakes.pop(j)]
            while cakes:
                cos=[L(box[-1],i)/(box[-1]+i) for i in cakes]
                box.append(cakes.pop(cos.index(min(cos))))
            size=box[0]+box[-1]
            for i in range(len(box)-1):
                size+=L(box[i],box[i+1])
            size_min=min(size,size_min)
        print "OK" if size_min<=size_max else "NA"
    except:
        break