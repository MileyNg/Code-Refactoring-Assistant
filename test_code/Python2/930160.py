while True:
    height, width = map(int,raw_input().split())
    if height == 0 and width == 0:
        break
    for j in range(height):
        print "#"*width
    print ""