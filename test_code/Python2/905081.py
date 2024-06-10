while True:
    a = raw_input().split()
    if a.count('0') == 4:
        break
    b = zip(a, map(int, a))

    def f(b):
        if len(b) == 1:
            return b[0][0] if b[0][1] == 10 else 0

        for i in range(len(b)):
            for j in range(i + 1, len(b)):

                c = [b[k] for k in range(len(b)) if k != i and k != j]
                c.append(('({} * {})'.format(b[i][0], b[j][0]), b[i][1] * b[j][1]))
                d = f(c)
                if d:
                    return d

                c = [b[k] for k in range(len(b)) if k != i and k != j]
                c.append(('({} + {})'.format(b[i][0], b[j][0]), b[i][1] + b[j][1]))
                d = f(c)
                if d:
                    return d

                c = [b[k] for k in range(len(b)) if k != i and k != j]
                c.append(('({} - {})'.format(b[i][0], b[j][0]), b[i][1] - b[j][1]))
                d = f(c)
                if d:
                    return d

                c = [b[k] for k in range(len(b)) if k != i and k != j]
                c.append(('({} - {})'.format(b[j][0], b[i][0]), b[j][1] - b[i][1]))
                d = f(c)
                if d:
                    return d
        return 0
    print f(b)