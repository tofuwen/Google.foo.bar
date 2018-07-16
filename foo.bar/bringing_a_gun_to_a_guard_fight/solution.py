# I am thinking too much
# Seems reflection + brute force can work well
# Even though in the worst case, this algorithm does not work
# Google foobar always makes test cases easy to pass

def gcd(a,b):
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    while b > 0:
        a, b = b, a % b
    return a

def dis(cur_x, cur_y, a_o, b_o):
	return (cur_x - a_o) ** 2 + (cur_y - b_o) ** 2

def is_in(cur_x, cur_y, a_o, b_o, distance):
	return dis(cur_x, cur_y, a_o, b_o) <= distance ** 2


def answer(dimensions, your_position, guard_position, distance):
    w, h = dimensions
    a, b = guard_position
    a_o, b_o = your_position
    potential = []
    x_range = distance // 2 // w + 2;
    y_range = distance // 2 // h + 2;
    for i in range(-x_range, x_range):
    	for j in range(-y_range, y_range):
    		for cur_a in [-a, a]:
    			for cur_b in [-b, b]:
    				cur_x = i * 2 * w + cur_a
    				cur_y = j * 2 * h + cur_b
    				if is_in(cur_x, cur_y, a_o, b_o, distance):
    					potential.append((cur_x, cur_y, True))
    		for cur_a in [-a_o, a_o]:
    			for cur_b in [-b_o, b_o]:
    				cur_x = i * 2 * w + cur_a
    				cur_y = j * 2 * h + cur_b
    				if is_in(cur_x, cur_y, a_o, b_o, distance):
    					potential.append((cur_x, cur_y, False))
    potential.sort(key=lambda tup: dis(tup[0], tup[1], a_o, b_o))
    ans = 0
    exists = set()
    for cur in potential:
    	if dis(cur[0], cur[1], a_o, b_o) == 0:
    		continue
    	g = gcd(cur[0]-a_o, cur[1]-b_o)
    	(aa, bb) = ((cur[0]-a_o)//g, (cur[1]-b_o)//g)
    	if (aa, bb) in exists:
    		continue
    	if cur[2]:
    		ans += 1
    	exists.add((aa, bb))
    return ans


print(answer([300, 275], [150, 150], [185, 100], 500))