days=(31,29,31,30,31,30,31,31,30,31,30,31)
day=('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
while True:
	total=0
	m,d=map(int,raw_input().split(" "))
	if m!=0:
		for i in range(m-1):
			total+=days[i]
		total+=d
		print day[(total+3)%7]
	else:
		break