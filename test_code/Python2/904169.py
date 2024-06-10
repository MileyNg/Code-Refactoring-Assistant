while True:
    li = raw_input().split()
    if li[1] == "+":
        print int(li[0]) + int(li[2])
    elif li[1] == "-":
        print int(li[0]) - int(li[2])
    elif li[1] == "*":
        print int(li[0]) * int(li[2])
    elif li[1] == "/":
        print int(li[0]) / int(li[2])
    elif li[1] == "?":
        break