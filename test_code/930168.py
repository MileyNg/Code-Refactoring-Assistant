while True:
    height, width = map(int,raw_input().split())
    if height == 0 and width == 0:
        break
    for i in range(height):
        board = ""
        for j in range(width):
            if i % 2 == 0:
                if j % 2 == 0:
                    board += "#"
                else:
                    board += "."
            else:
                if j % 2 == 0:
                    board += "."
                else:
                    board += "#"
        print board
    print ""