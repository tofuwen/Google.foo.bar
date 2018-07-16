from Queue import Queue

def helper(maze):
	h = len(maze)
	w = len(maze[0])
	visited = [[False for i in range(w)] for j in range(h)]
	q = Queue()
	q.put(((0, 0), 0))
	visited[0][0] = True
	while not q.empty():
		(x, y), step = q.get()
		if x == h-1 and y == w-1:
			return step+1 # path length = step + 1
		for (step_x, step_y) in [(0,1), (1,0), (0,-1), (-1,0)]:
			next_x = step_x + x
			next_y = step_y + y
			if next_x >= h or next_x < 0:
				continue
			if next_y >= w or next_y < 0:
				continue
			if maze[next_x][next_y] == 1:
				continue
			if not visited[next_x][next_y]:
				visited[next_x][next_y] = True
				q.put(((next_x, next_y), step+1))
	return 1000000


def answer(maze):
	ans = helper(maze)
	h = len(maze)
	w = len(maze[0])
	for i in range(h):
		for j in range(w):
			if maze[i][j] == 1:
				maze[i][j] = 0
				ans = min(ans, helper(maze))
				maze[i][j] = 1
	return ans

print answer([[0,1,1], [1,1,1] ,[1,1,0]])