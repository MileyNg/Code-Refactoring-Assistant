chk = [
    (1,2,3),
    (4,5,6),
    (7,8,9),
    (1,4,7),
    (2,5,8),
    (3,6,9),
    (1,5,9),
    (3,5,7)
    ]
while True:
    s = "0"
    s += raw_input()
    if s[1]=='0':
        break
    s += raw_input()+raw_input()
    judge = "NA"
    for ch in chk:
        if s[ch[0]]==s[ch[1]]==s[ch[2]]:
            if s[ch[0]]=='b':
                judge = "b"
                break
            elif s[ch[0]]=='w':
                judge = "w"
                break
    print judge