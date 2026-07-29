[Problem](https://leetcode.com/problems/cheapest-flights-within-k-stops/)



## BFS with Queue Relaxation

Refer to the [07_29_2026.py](07_29_2026.py) file.



## Bellman-Ford variant


[Submission](https://leetcode.com/problems/cheapest-flights-within-k-stops/submissions/2086677973/)—Runtime: 65 ms (beats 33.10%), Memory: 20.35 MB (beats 62.29%)

TC: $O(kE)$
SC: $O(V+E)$


```python
from collections import defaultdict
import math


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # construct graph
        graph = defaultdict(list)

        for fr, to, p in flights:
            graph[fr].append((to, p))

        # cost[i] = cheapest price to reach city i
        # using at most the number of flights processed so far
        cost = {i: math.inf for i in range(n)}
        cost[src] = 0

        for _ in range(k + 1):
            # Updates from this round cannot be reused until the next round.
            nxt_cost = cost.copy()

            for curr in graph:
                if cost[curr] == math.inf:
                    continue

                for nghbr, p in graph[curr]:
                    nxt_cost[nghbr] = min(nxt_cost[nghbr], cost[curr] + p,)

            cost = nxt_cost

        return -1 if cost[dst] == math.inf else cost[dst]

```

cf.) This approach is exactly the same as the [Editorial's Approach 2: Bellman Ford](https://leetcode.com/problems/cheapest-flights-within-k-stops/editorial/#approach-2-bellman-ford).

## Modified Dijkstra (Priority Queue-based)



[Submission](https://leetcode.com/problems/cheapest-flights-within-k-stops/submissions/2086672241/)—Runtime: 3 ms (beats 89.13%), Memory: 21.27 MB (beats 14.60%)

TC: $O(kE \log(kE))$
SC: $O(V + kE)$


```python
from collections import defaultdict
import heapq
import math


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Construct graph.
        graph = defaultdict(list)

        for f, t, p in flights:
            graph[f].append((t, p))

        # stops[i] = fewest flights used to reach city i
        stops = [math.inf] * n

        # (current_price, current_city, flights_used)
        q = [(0, src, 0)]

        while q:
            curr_p, curr, distance = heapq.heappop(q)

            # A cheaper state with fewer flights has already reached this city.
            if distance > stops[curr]:
                continue

            stops[curr] = distance

            # First time dst is popped is the cheapest price
            # since the heap is ordered by price.
            if curr == dst:
                return curr_p

            if distance == k + 1:
                continue

            for nghbr, p in graph[curr]:
                heapq.heappush(q, (curr_p + p, nghbr, distance + 1))

        return -1

```

cf.) This approach is exactly the same as the [Editorial's Approach 3: Dijkstra](https://leetcode.com/problems/cheapest-flights-within-k-stops/editorial/#approach-3-dijkstra).