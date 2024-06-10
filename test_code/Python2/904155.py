def partition(A, p, r):
    pivot = A[r]
    ptr = p
    for i in range(p, r):
        if A[i] <= pivot:
            A[ptr], A[i] = A[i], A[ptr]
            ptr += 1
    A[ptr], A[r] = A[r], A[ptr]
    return ptr

if __name__ == "__main__":
    import sys
    N = int(sys.stdin.readline().strip())
    A = [int(e) for e in sys.stdin.readline().strip().split()]
    pivIdx = partition(A, 0, N-1)
    strA = map(str, A)
    strA[pivIdx] = "[{0}]".format(strA[pivIdx])
    print " ".join(strA)