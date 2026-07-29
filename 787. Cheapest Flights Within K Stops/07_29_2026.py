# submission: https://leetcode.com/problems/cheapest-flights-within-k-stops/submissions/2086475999/
# runtime: 7 ms (beats 70.05%), memory: 20.20 MB (beats 66.38%)
# solved using bfs with a queue relaxation
# 25 min

# TC: O(k*E), where E is the number of edges (flights) in the graph
# SC: O(V+E), where V is the number of vertices (cities) in the graph


# directly noticed it's a shortest path problem. however, i couldn't think of the Dijkstra and Bellman-Ford algorithms. so, I attempted with the bfs since it's the easiest approach for the shortest distance on the unweighted graph. 

# there were two mistakes i made:

# 1. since this is an weighted graph, the path with a minimum weight (or cost) can have more edges, whereas in the unweighted graph, the shortest path is always the one with the least number of edges. therefore, we cannot simply skip the vertex just because we have already visited it. at first, i didn't consider this, so submitted a wrong solution: https://leetcode.com/problems/cheapest-flights-within-k-stops/submissions/2086461212/

# 2. then, simply removing the `visited` set (from the above) is not enough because that means there may be a huge number of unnecessary nodes pushed into the queue. we can see that it raises a memory limit exceeded error: https://leetcode.com/problems/cheapest-flights-within-k-stops/submissions/2086469025/

# therefore, we need to prune somehow. the idea is the same as the Bellman-Ford relaxation. we can simply update the cost of the vertex and push it into the queue again if the new cost is less than the previous one (`if nxt_p < cost[nghbr]:` part in the code below).

# cf.) this approach is exactly the same as the Editorial's Approach 1: Breadth First Search. for other approaches, refer to the README.md.


from collections import deque, defaultdict
import math


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # construct graph
        graph = defaultdict(list)
        for f, t, p in flights:
            graph[f].append((t, p))

        # construct cost table
        cost = {i: math.inf for i in range(n)}

        q = deque([(src, 0)])
        distance = 0
        while distance <= k and q:
            for _ in range(len(q)):
                curr, curr_p = q.popleft()
                for nghbr, p in graph[curr]:
                    nxt_p = curr_p + p
                    
                    if nxt_p < cost[nghbr]:
                        cost[nghbr] = nxt_p
                        q.append((nghbr, nxt_p))

            distance += 1

        return -1 if cost[dst] == math.inf else cost[dst]
