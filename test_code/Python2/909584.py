def findMaxId(id_x):
	max_x=0
	max_id=0
	for i in range(n):
		if id_x[i]>max_x:
			max_x=id_x[i]
			max_id=i
	return max_id
	
n,r,l=map(int,raw_input().split())
log=[map(int,raw_input().split()) for i in range(r)]
log.insert(0,[1,0,0])
log.append([1,l,0])
id_t=[0]*n
id_x=[0]*n
max_id=0
for i in range(1,r+2):
	cur_id=log[i][0]-1
	id_t[max_id]+=log[i][1]-log[i-1][1]
	id_x[cur_id]+=log[i][2]
	if cur_id==max_id and log[i][2]<0:
		max_id=findMaxId(id_x)
	elif id_x[max_id]<id_x[cur_id] or (id_x[max_id]==id_x[cur_id] and max_id>cur_id):
		max_id=cur_id
print id_t.index(max(id_t))+1