[Problem](https://leetcode.com/problems/evaluate-division/)


## DFS Approach (with memoization)


The code below implements a DFS approach with memoization to solve the problem. The key idea is to construct a graph from the given equations and values, and then use DFS to find the path score between two vertices. The memoization is used to cache the results of the DFS calls to avoid redundant calculations (Memoization is not mandatory here. Note that iterative DFS solution in `05_13_2025.py` doesn't cache the results).

I tried solving for a second time (10/20/2025). At this time, I didn't konw which **topic** this problem belongs to. I spent half an hour, but counldn't solve it. However, at the first time (05/13/2025), I was able to solve it in an hour, knowing this is a graph problem in advance. I noticed how much difference it makes to know the topic in advance.

**TAKEAWAY**: Always try to ask myself which algorithm or data structure would be appropriate for the problem. Especially, once you notice it's a graph problem, it's quite straightforward which specific algorithm to use; for example, DFS for cyclic detection, and path finding or DFS for topological sort, etc.

- [Submission](https://leetcode.com/problems/evaluate-division/submissions/1806946811/) (Runtime: 0 ms, Memory: 17.75 MB)
Let $N$, $V$, $E$, and $Q$ be the number of equations, vertices (variables, $\leq 2N$), edges ($\approx 2N$), and queries respectively.
- TC: $O(N + Q*(V+E))$
  - Constructing graph: $O(N)$
  - DFS per query: $O(V+E)$
- SC: $O(V+E)$
  - Constructing graph: $O(V+E)$
  - Visited set: $O(V)$
  - Stack: $O(V)$
  - Output space is not counted

```python
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def construct_graph():
            graph = defaultdict(dict)

            for (v1, v2), w in zip(equations, values):
                graph[v1][v2] = w
                graph[v2][v1] = 1 / w

            return graph


        # dfs() also addresses the self-loop case
        def dfs(src: str, dst: str, seen: set, acc: float) -> float:
            if src == dst:
                return acc

            seen.add(src)

            for neighbor, weight in graph[src].items():
                if neighbor not in seen:
                    res = dfs(neighbor, dst, seen, acc * weight)

                    if res != -1.0:
                        return res

            return -1


        graph = construct_graph()
        memo = {}  # (src, dst) -> value (caching via memoization)
        ans = []
        for x, y in queries:
            # consider only valid vertices
            if x not in graph or y not in graph:
                ans.append(-1.0)
                continue

            if (x, y) in memo:
                ans.append(memo[(x, y)])
                continue

            path_score = dfs(x, y, set(), 1.0)
            memo[(x, y)] = path_score
            ans.append(path_score)

        return ans

```


## Weighted Union-Find (Disjoint Set) Approach


The code below is written by ChatGPT. For more detailed explanation with visualizations, refer the the Editorial section.


- [Submission](https://leetcode.com/problems/evaluate-division/submissions/1806947924/) (Runtime: 0 ms, Memory: 17.73 MB)
- TC: $O((N + Q) \cdot \alpha(V))$ amortized
  - Build (union over $N$ equations): $O(N \cdot \alpha(V))$ amortized ($\alpha$ is the inverse Ackermann function, $\approx$ constant)
  - Per query (two find operations): $O(\alpha(V))$ amortized
- SC: $O(V)$ (Parent and weight maps each store one entry per variable, and output space is not counted)


```python
from typing import Dict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        parent: Dict[str, str] = {}
        weight: Dict[str, float] = {}  # weight[x] = x / parent[x]

        def add(x: str) -> None:
            if x not in parent:
                parent[x] = x
                weight[x] = 1.0

        def find(x: str) -> Tuple[str, float]:
            """Return (root, ratio) where ratio = x / root."""
            if parent[x] != x:
                root, root_ratio = find(parent[x])
                # Path compression: update parent and weight to point to root
                weight[x] *= root_ratio
                parent[x] = root
            return parent[x], weight[x]

        def union(a: str, b: str, k: float) -> None:
            """
            Given a / b = k, connect roots so that invariant holds.
            If ra is attached under rb, set weight[ra] so that:
            (a / b) = k  ⇒ (wa * ra) / (wb * rb) = k  ⇒ ra / rb = k * wb / wa
            """
            add(a); add(b)
            ra, wa = find(a)
            rb, wb = find(b)
            if ra == rb:
                return
            # Attach ra under rb; update weight[ra] to satisfy equation
            parent[ra] = rb
            weight[ra] = k * wb / wa

        # Build structure
        for (a, b), k in zip(equations, values):
            union(a, b, k)

        # Answer queries
        ans = []
        for x, y in queries:
            if x not in parent or y not in parent:
                ans.append(-1.0)
                continue
            rx, wx = find(x)
            ry, wy = find(y)
            ans.append(wx / wy if rx == ry else -1.0)

        return ans

```