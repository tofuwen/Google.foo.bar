def helper(l0, l1, l2):
	l0.extend(l1)
	l0.extend(l2)
	l0.sort(reverse=True)
	s = ""
	for i in range(0, len(l0)):
		s = s + str(l0[i])
	if len(s) == 0:
		return 0
	return int(s)

def answer(l):
    l0 = []
    l1 = []
    l2 = []
    total = 0
    for i in l:
    	total = total + i
    	if i % 3 == 0:
    		l0.append(i)
    	if i % 3 == 1:
    		l1.append(i)
    	if i % 3 == 2:
    		l2.append(i)
    l0.sort()
    l1.sort()
    l2.sort()
    if total % 3 == 1:
    	if len(l1) > 0:
    		return helper(l0, l1[1:], l2)
    	else:
    		if len(l2) > 1:
    			return helper(l0, l1, l2[2:])
    	return 0
    if total % 3 == 2:
    	if len(l2) > 0:
    		return helper(l0, l1, l2[1:])
    	else:
    		if len(l1) > 1:
    			return helper(l0, l1[2:], l2)
    	return 0
    return helper(l0, l1, l2)

print answer([1])

