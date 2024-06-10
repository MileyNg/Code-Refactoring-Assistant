def insertion_sort(A, N):
    for j in range(1, N):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
        print " ".join(map(str, A))

if __name__ == "__main__":
    import sys
    N = int(sys.stdin.readline().strip())
    A = [ int(e) for e in sys.stdin.readline().strip().split() ]
    print " ".join(map(str, A))
    insertion_sort(A, N)