while True:
    try:
        line = input()
    except:
        break
    a,b,c,d,e,f = map(int, line.strip().split())
    z = a * e - b * d
    x = c * e - b * f
    if x: x = x / z
    y = a * f - c * d
    if y: y = y / z
    print('{:.3f} {:.3f}'.format(x, y))