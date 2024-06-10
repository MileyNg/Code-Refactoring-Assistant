a = []
while True:
    x = input()
    if x == 0: break
    a.append(x)
    
i = 0
for x in range(len(a)):
    print "Case " + str(i+1) + ": " + str(a[i])
    i += 1