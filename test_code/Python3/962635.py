text = ''
while True:
    try:
        s = input()
    except:
        break
    text += s.lower()

for c in 'abcdefghijklmnopqrstuvwxyz':
    print('{} : {}'.format(c, text.count(c)))