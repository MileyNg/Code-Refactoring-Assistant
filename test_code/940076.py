def check(h,w):
	s = A[h][w]
	tf = A[h].count(s) > 1 or B[w].count(s) > 1 or C[h/3][w/3].count(s) > 1
	return "*" if tf else " "
R = range(9)
for r in range(input()):
	if r > 0: print
	A = [raw_input().split() for i in R]
	B = [[A[h][w] for h in R] for w in R] 
	C = [[A[h][w:w+3]+A[h+1][w:w+3]+A[h+2][w:w+3] for w in [0,3,6]] for h in [0,3,6]]
	P = [[check(h,w) for w in R] for h in R] 
	for h in R:
		print "".join([P[h][w]+A[h][w] for w in R])