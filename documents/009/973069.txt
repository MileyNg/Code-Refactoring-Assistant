sids = input()
side_list = []

side_list = [int(s) for s in sids.split(' ', )]

a = side_list[0]
b = side_list[1]
c = side_list[2]

if c > b > a:
	print('Yes')

else:
	print('No')