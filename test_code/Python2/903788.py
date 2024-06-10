if __name__ == "__main__":
    import sys
    N = int(sys.stdin.readline().strip())
    A = [int(e) for e in sys.stdin.readline().strip().split()]
    cnt = 0
    for i in range(N-1):
        for j in range(N-1, i, -1):
            if A[j] < A[j-1]:
                A[j-1], A[j] = A[j], A[j-1]
                cnt += 1
    print " ".join(map(str, A))
    print cnt