def answer(n):
	total_num = 41000
	nums = range(2, total_num+1)
	flags = [True for i in range(total_num)]
	for i in range(total_num/2):
		if flags[nums[i]]:
			for j in range(2, total_num/2/nums[i]):
					flags[j*nums[i]] = False
	s = ""
	for i in range(2, total_num/2):
		if flags[i]:
			s = s + str(i)
	print len(s)
	return s[n:n+5]

print answer(0)
