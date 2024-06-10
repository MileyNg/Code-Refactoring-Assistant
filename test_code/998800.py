s = raw_input().split()
d = {}
w = None
mf = 0
m = None
ml = 0

for ww in s:
    if( len(ww) > ml ):
        m = ww
        ml = len(ww)
    try:
        d[ww] += 1
        if( d[ww] > mf ):
            mf = d[ww]
            w = ww
    except KeyError:
        d[ww] = 1

print w, m