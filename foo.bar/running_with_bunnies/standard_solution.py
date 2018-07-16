# https://repl.it/@andrewmzhang/runningwithbunnies

def floyd_warshall(adj_matrix):
    # Implement floyd-warshall + keep track of the shortest path
    # Floyd Warshall is easily provable by induction
    # We will need all-pairs-shortest-path
    
    n = len(adj_matrix)
    
    dist = [[adj_matrix[x][y] for y in range(n)] for x in range(n)]
    paths = [[[i, j] for j in range(n)] for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if dist[j][k] > (dist[j][i] + dist[i][k]):
                    dist[j][k] = dist[j][i] + dist[i][k]
                    paths[j][k] = paths[j][i] + paths[i][i][1:]
                    
    return dist, paths
    
    
    
def has_neg_cycle(dist):
    # Floyd Warshall lets us know if there's a negative cycle of
    # a node to node cycle has a negative cost. 
    n = len(dist)
    for i in range(n):
        if dist[i][i] < 0:
            return True
    
    return False
    

def sanitize(path, n):
    # Given a path of node and what node is the last node,
    # returns a list of the bunnies in sorted order
    lst = list(set(path))
    if 0 in lst:
        lst.remove(0)
    if n in lst:
        lst.remove(n)
    lst.sort()
    
    lst = [node - 1 for node in lst]
    
    return lst

def answer(times, time_limit):
    # your code here
    
    # Run Floyd-Warshall, get the distances and the paths
    dist, paths = floyd_warshall(times)
    n = len(times)
    last = len(times) - 1

    # If we have a negative cycle, the solution is all bunnies, sine we
    # can go to the node with the negative cycle in finite time
    # loop over and over until we have a very large time_left and
    # get all the bunnies at some finite cost.  
    if has_neg_cycle(dist):
      lst = [i for i in range(n)]
      return sanitize(lst, last)
     
    # Run a DFS on the nodes in non-repeditive order
    # This works despite the DFS stopping at the bulkhead, since
    # if from node a to b was faster by going through
    # the bulkhead, Floyd Warshall will know about it, thus
    # we need not consider loops giving shorter paths. We have also determined
    # no negative cycles, so redudant loops are known to cost a non-negative time. 
    queue = [(0, time_limit, [], [])]
    best_path = []

    while len(queue) > 0:
        node, time_left, path, known_visited = queue.pop(0)
        
        # If the DFS hits the end, and there is time on the clock, record
        # this as a valid way to collect rabits. If there is no time,
        # chuck this useless path. 
        if node == last and time_left >= 0:
            bunnies = sanitize(path, last)
            if len(bunnies) > len(best_path):
                best_path = bunnies
                continue
        
        # If we are not at the end, run a DFS. Again, the DFS need not consider
        # a possibly shorter path that goes through the bulwark, or the start node,
        # since Floyd-Warshall will account for that. 
        for i in range(n):
            if i not in known_visited and i != node:
                queue.append((i, time_left - dist[node][i], path + paths[node][i], known_visited + [i]))
    return best_path