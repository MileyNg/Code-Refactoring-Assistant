r, c = map(int, raw_input().split())

line = [map(int, raw_input().split()) for i in range(r)]
foot = [0 for i in range(c+1)]

for i in range(len(line)):
	line[i].append(sum(line[i]))
	for j in range(len(line[i])):
		foot[j] += line[i][j]

line.append(foot)
for l in line:
	print " ".join(map(str, l))