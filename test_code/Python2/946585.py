n, m = raw_input().strip().split(' ')

n = int(n)
m = int(m)

a = [0] * n
b = [0] * m
c = [0] * n
ans = 1
ansv = 0

for i in range(n) :
	a[i] = input()

for i in range(m) :
	b = input()
	for j in range(n) :
		if (a[j] <= b) :
			c[j] += 1;
			if (c[j] > ansv) :
				ansv = c[j]
				ans = j + 1
			break

print ans