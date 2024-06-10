while 1:
    try:
        speed = input()
    except EOFError:
        break
    height = 4.9 * (speed / 9.8) ** 2
    print int(round(height / 5 + 0.5)) + 1