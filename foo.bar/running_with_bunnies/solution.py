# data is weak, so this code passed the tests
# standard solution uses Floyd-Warshall

from Queue import Queue

def count_bunny(saved):
	if saved == 0:
		return 0
	return saved % 2 + count_bunny(saved >> 1)

def make_list(saved):
	temp = []
	while saved > 0:
		temp.append(saved % 2)
		saved = saved >> 1
	ans = []
	for i in range(len(temp)):
		if temp[i] == 1:
			ans.append(i)
	return ans

def answer(times, time_limit):
    time_borrow = 100
    dp = [[[False for i in range(40)] for j in range(1005 + time_borrow)] for k in range(10)]
    q = Queue()
    q.put((0, time_limit + time_borrow, 0))
    dp[0][time_limit + time_borrow][0] = True
    num = len(times)
    while not q.empty():
        where, time_left, saved = q.get()
        for i in range(num):
        	where_next = i
        	time_left_next = time_left - times[where][where_next]
        	saved_next = saved
        	if where_next > 0 and where_next < num-1:
        		saved_next = saved | (1<<(where_next-1))
        	if time_left_next < 0 or time_left_next >= 1005 + time_borrow:
        		continue
        	if dp[where_next][time_left_next][saved_next]:
        		continue
        	dp[where_next][time_left_next][saved_next] = True
        	q.put((where_next, time_left_next, saved_next))
    ans = 0
    cur_count = 0
    for j in range(time_borrow, 1005 + time_borrow):
    	for k in range(1<<(num-2)):
    		if dp[num-1][j][k]:
    			num_bunny = count_bunny(k)
    			if num_bunny > cur_count:
    				cur_count = num_bunny
    				ans = k
    			if num_bunny == cur_count and ans > k:
    				ans = k
    return make_list(ans)

print(answer([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1))



