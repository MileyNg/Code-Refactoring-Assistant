sids = input()
side_list = []

side_list = [int(s) for s in sorted(sids.split(' ', ), key=lambda s: int(s), reverse=False)]

print(' '.join(map(str, side_list)))