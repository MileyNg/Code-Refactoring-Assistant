sids = input()
side_list = []

side_list = [int(s) for s in sids.split(' ', )]

print(side_list[0] * side_list[1], side_list[0] * 2 + side_list[1] * 2)