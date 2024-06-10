inf = 0x101010
def solve(start,goal):
	cost = [inf]*n
	visited = [False]*n
	cost[start] = 0
	while 1:
		min = inf
		next = -1
		visited[start] = True
		for i in range(n):
			if visited[i]: continue
			if graph[start][i] > -1:
				d = cost[start] + graph[start][i]
				if d < cost[i]:
					cost[i] = d
			if min > cost[i]:
				min = cost[i]
				next = i
		start = next
		if next == -1: break
	return cost[goal]

n = input()
m = input()
graph = [[-1]*n for i in range(n)]
for i in range(m):
	a,b,c,d = map(int,raw_input().split(","))
	graph[a-1][b-1] = c
	graph[b-1][a-1] = d
x1,x2,y1,y2 = map(int,raw_input().split(","))
print y1-y2-solve(x1-1,x2-1)-solve(x2-1,x1-1)