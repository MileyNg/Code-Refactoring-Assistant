while True:
    a,b = map(int,raw_input().split())
    if a == b == 0: break
    for i in range(a):
        if i % 2 == 0:
            if b % 2 == 0:
                print "#." * (b /2)
            else:
                print "#." * (b /2) + "#"
        else:
            if b % 2 == 0:
                print ".#" * (b /2)
            else:
                print".#" * (b /2) + "."
    print