while True:
    a,b = map(int,raw_input().split())
    if a == 0 and b == 0:
        break
    else:
        print "#" * b
        for i in range(a-2):
            print "#" + "." * (b-2) + "#"
        print "#" * b
        print