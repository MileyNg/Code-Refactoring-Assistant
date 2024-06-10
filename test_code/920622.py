def operate( cmd, text, cur ):
    lentxt = len(text)
    if cmd == "forward char":
        if cur < lentxt: cur += 1
    elif cmd == "backward char":
        if cur > 0: cur -= 1
    elif cmd == "forward word":
        while cur < lentxt and text[cur] == ' ': cur += 1
        while cur < lentxt and text[cur] != ' ': cur += 1
    elif cmd == "backward word":
        while cur > 0 and text[cur - 1] == ' ': cur -= 1
        while cur > 0 and text[cur - 1] != ' ': cur -= 1
    elif cmd == "delete char":
        text = text[:cur] + text[cur + 1:]
    elif cmd == "delete word":
        d = 0
        while cur + d < lentxt and text[cur + d] == ' ': d += 1
        if cur + d != lentxt:
            while cur + d < lentxt and text[cur + d] != ' ': d += 1
            text = text[:cur] + text[cur + d:]
    else:
        ins = cmd[8:-1]
        text = text[:cur] + ins + text[cur:]
        cur += len(ins)
    return cur, text

if __name__ == "__main__":
    a = int(raw_input())
    for i in range(a):
        text = raw_input()
        cnt = int(raw_input())
        cursor = 0
        for j in range(cnt):
            command = raw_input()
            cursor, text = operate( command, text, cursor )
        print (text[:cursor] + '^' + text[cursor:])