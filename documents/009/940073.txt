def check(h,w):
	s = A[h][w]
	if A[h].count(s) > 1 or RA[w].count(s) > 1 or A9[h/3][w/3].count(s) > 1:
		return "*"
	else:
		return " "
R = range(9)
for r in range(input()):
	if r > 0: print
	A  = [raw_input().split() for i in R]
	RA = [[A[h][w] for h in range(9)] for w in R] 
	A9 = [[A[h][w:w+3]+A[h+1][w:w+3]+A[h+2][w:w+3] for w in [0,3,6]] for h in [0,3,6]]
	P = [[check(h,w) for w in R] for h in R] 
	for h in R:
		print "".join([P[h][w]+A[h][w] for w in R])