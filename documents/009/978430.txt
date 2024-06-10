count = 0
while True:
    try:
        s = input()
    except EOFError:
        break

    if all(s[i] == s[-1-i] for i in range(len(s)//2+1)):
        count += 1

print(count)