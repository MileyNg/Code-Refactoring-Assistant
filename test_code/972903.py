sids = input()
side_list = []

side_list = [int(s) for s in sids.split(' ', )]

a = side_list[0]
b = side_list[1]

if a > b:
	print('a > b')

elif a < b:
	print('a < b')

elif a == b:
	print('a == b')