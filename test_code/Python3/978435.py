import re
password = 0
while True:
    try:
        s = input()
    except EOFError:
        break

    for n in re.findall('[0-9]+', s):
        password += int(n)

print(password)