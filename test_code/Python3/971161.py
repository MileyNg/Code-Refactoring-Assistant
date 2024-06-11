def main():

    data = list(map(int, input().split()))

    a = data[:3]
    b = data[3:]
    ans = [0 for x in range(3)]

    t = b[2] - a[2]
    if t < 0:
        ans[2] = t + 60
        b[1] -= 1
    else:
        ans[2] = t


    t = b[1] - a[1]
    if t < 0:
        ans[1] = t + 60
        b[0] -= 1

    else:
        ans[1] = t

    ans[0] = b[0] - a[0]
    for a in ans[:-1]:
        print(a, end=' ')
    print(ans[-1])

if __name__ == '__main__':
    for a in range(3):
        main()