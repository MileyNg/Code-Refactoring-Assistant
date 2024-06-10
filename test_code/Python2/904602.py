try:
    while True:
        y = ((float(raw_input()) / 9.8) ** 2) * 4.9
        if y == int(y):
            print int((int(y) - 1) // 5) + 2
        else:
            print int(y // 5) + 2
except:
    pass