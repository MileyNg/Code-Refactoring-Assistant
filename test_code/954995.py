while 1:
    try:
        nm = map(int, raw_input().split())
        if nm == [0, 0]:
            break
        n = nm[0]
        m = nm[1]
        p = map(int, raw_input().split())
        p_sorted = sorted(p)
        sum = 0
        for i in range(n):
            if (i+1) % m != 0:
                sum += p_sorted[-1-i]
        print sum
    except:
	pass