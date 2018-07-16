# got TLE! And after looking at github, realizing that okay() can be memorized!
# actually, it's not memorized, but pre-compute. For each j, k, which g[:][index] is valid,
# and then store k in pair (j, g[:][index]) [clever, saved the loop in okay(), also make the main loop a lot less expensive]
# def okay(j, k, g, index):
# 	h, w = len(g), len(g[0])
# 	for i in range(h):
# 		ans = ((j & (1<<i)) > 0) + ((j & (1<<(i+1))) > 0) + ((k & (1<<i)) > 0) + ((k & (1<<(i+1))) > 0)
# 		if ans == 1 and not g[i][index]:
# 			return False
# 		if ans != 1 and g[i][index]:
# 			return False
# 	return True

# really clever
# https://gist.github.com/lotabout/891621ae8a01d8e512afd4b5254516b4
def gen(c1,c2,bitlen):
    a = c1 & ~(1<<bitlen)
    b = c2 & ~(1<<bitlen)
    c = c1 >> 1
    d = c2 >> 1
    return (a&~b&~c&~d) | (~a&b&~c&~d) | (~a&~b&c&~d) | (~a&~b&~c&d)

def answer(g):
    h, w = len(g), len(g[0])
    dp_x = w + 1
    dp_y = 1 << (h+1)
    dp = [[0 for i in range(dp_y)] for j in range(dp_x)]
    dp[0] = [1 for i in range(dp_y)]
    gg = [0 for i in range(w)]
    for i in range(w):
    	for j in range(h):
    		gg[i] += (1 << j) * int(g[j][i])
    pre = {}
    for i in range(dp_y):
    	for j in range(dp_y):
    		generate = gen(i, j, h)
    		if generate in gg:
    			if (i, generate) not in pre:
    				pre[(i, generate)] = []
    			pre[(i, generate)].append(j)
    # for i in range(1, dp_x):
    # 	for j in range(0, dp_y):
    # 		for k in range(0, dp_y):
    # 			if okay(j, k, g, i-1):
    # 				dp[i][j] += dp[i-1][k]
    for i in range(1, dp_x):
    	for j in range(0, dp_y):
    		if (j, gg[i-1]) not in pre:
    			continue
    		for k in pre[(j, gg[i-1])]:
    			dp[i][j] += dp[i-1][k]
    ans = 0
    for i in range(0, dp_y):
    	ans += dp[dp_x-1][i]
    return ans

print(answer([[True, True, False, True, False, True, False, True, True, False], [True, True, False, False, False, False, True, True, True, False], [True, True, False, False, False, False, False, False, False, True], [False, True, False, False, False, False, True, True, False, False]]))