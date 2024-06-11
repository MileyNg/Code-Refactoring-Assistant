s = ''
while True:
    try:
        s += input().lower()
    except EOFError:
        break

for c in 'abcdefghijklmnopqrstuvwxyz':
    print('{} : {}'.format(c, s.count(c)))