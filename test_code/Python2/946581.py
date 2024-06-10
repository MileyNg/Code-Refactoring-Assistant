dp = [range(8) for i in range(1001)]

for i in range(1001) :
	for j in range(8) :
		dp[i][j] = 0

dp[0][1] = 1

n = input()
s = raw_input().strip()

for i in range(n) :
	b = 0
	if s[i] != 'J' :
		b += 1
		if s[i] != 'O' :
			b += 1
	
	for j in range(8) :
		for k in range(8) :
			if (((k >> b) & 1) and (j & k) != 0) :
				dp[i + 1][k] = (dp[i + 1][k] + dp[i][j]) % 10007

sum = 0
for i in range(8) :
	sum = (sum + dp[n][i]) % 10007

print sum