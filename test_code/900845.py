def isOver(array,x,y):
	return True if (array[0]-x)**2+(array[1]-y)**2 <= 1.01 else False
	
while True:
    mx = 0
    n = int(raw_input())
    if n == 0: break
    seals = [map(float, raw_input().split(",")) for i in range(n)]
    x = 0
    while x < 10.0:
    	y = 0.0
    	while y < 10.0:
    		num = 0
    		for seal in seals:
    			if isOver(seal,x,y):
    				num += 1
    		mx = max(mx,num)
    		y += 0.1
        x += 0.1
    print mx