_ = raw_input()
nums = [int(x) for x in raw_input().split(" ")]
x = nums.pop()

res_ = [0 for i in range(21)]
res_[nums[0]] = 1
nums = nums[1:]

for n in nums:
	res = [0 for i in range(21)]
	for (i, r) in enumerate(res_):
		if r > 0:
			if 0 <= i-n <= 20:
				res[i-n] += r
			if 0 <= i+n <= 20:
				res[i+n] += r
	res_ = res

print "%d" % res_[x]