a = [
    ['11', '11'],
    ['1', '1', '1', '1'],
    ['1111'],
    ['01', '11', '10'],
    ['110', '011'],
    ['10', '11', '01'],
    ['011', '110']
]


def f(b):
    for j in range(len(a)):
        for x in range(9 - len(a[j][0])):
            for y in range(9 - len(a[j])):
                c = True
                for i in range(len(a[j])):
                    if b[y + i][x:x + len(a[j][0])] != a[j][i]:
                        c = False
                if c:
                    return j

try:
    while True:
        b = [raw_input() for i in range(8)]
        print chr(ord('A') + f(b))
        raw_input()
except:
    pass