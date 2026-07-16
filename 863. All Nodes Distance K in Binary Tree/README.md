[Problem](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)

I believe the [Parent Map + BFS](#parent-map--bfs) and the [Graph Construction + BFS](#graph-construction--bfs) solutions are the most straightforward and easy-to-come-up-with solutions during the coding interview.


## Parent Map + BFS

Once we have a parent hash table, we can think of tree + hash table as an undirected graph since we can go to any neighbor node (left, right, or parent) from a given node.

[Submission](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/submissions/2070247600/)—Runtime: 38 ms (beats 96.99%), Memory: 19.92 MB (beats 33.13%)

- TC: $O(n)$, where $n$ is the number of nodes in the tree.
- SC: $O(n)$

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Step 1: Record each node's parent.
        parent = {}

        def build_parent(node: Optional[TreeNode], par: Optional[TreeNode]) -> None:
            if not node:
                return

            parent[node] = par
            build_parent(node.left, node)
            build_parent(node.right, node)

        build_parent(root, None)

        # Step 2: BFS outward from target:
        # left child, right child, and parent.
        queue = deque([target])
        visited = {target}
        distance = 0

        while queue and distance < k:
            for _ in range(len(queue)):
                node = queue.popleft()

                for neighbor in (node.left, node.right, parent[node]):
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            distance += 1

        return [node.val for node in queue]

```


## Graph Construction + BFS

The key point is to build an undirected graph from the given tree, then perform BFS from the target node.


[Submission](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/submissions/2070254263/)—Runtime: 53 ms (beats 30.73%), Memory: 20.38 MB (beats 6.82%)

- TC: $O(n)$, where $n$ is the number of nodes in the tree.
- SC: $O(n)$

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Build undirected graph.
        graph = defaultdict(list)

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return

            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)

                dfs(node.left)

            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)

                dfs(node.right)

        dfs(root)

        # BFS from target.
        queue = deque([target])
        visited = {target}
        distance = 0

        while queue and distance < k:
            for _ in range(len(queue)):
                node = queue.popleft()

                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            distance += 1

        return [node.val for node in queue]

```


## Single DFS Distance Propagation (Postorder DFS; or Tree DP)

The key idea is that DFS returns the distance (or height) from the passed node to the target node, assuming that the target exists in the tree (or subtree) rooted at the passed node. If the target doesn't exist, the DFS returns -1. Once the target is found, we collect all k-distant nodes below it. While unwinding the recursion, we propagate the distance upwards to the parent node. If the target is in the left subtree at distance $d$ from the `node.left`, then the current node (`node`) is at distance $d + 1$. Then, either the current node itself is at distance $k$, or we collect all nodes at distance $k - d - 2$ from the right subtree (`node.right`). If the target is in the right subtree (which is equivalent to the target not being in the left subtree), symmetric logic applies.

The logic is the same as the [Multiple dfs w/ Ancestor Path + Opposite Subtree Search](./07_16_2026.py) solution, but this approach performs only one DFS, so is more elegant.

[Submission](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/submissions/2070256981/)—Runtime: 43 ms (beats 88.16%), Memory: 19.63 MB (beats 67.54%)

- TC: $O(n)$, where $n$ is the number of nodes in the tree.
- SC: $O(n)$

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = []

        def collect(node, dist):
            if not node:
                return

            if dist == 0:
                ans.append(node.val)
                return

            collect(node.left, dist - 1)
            collect(node.right, dist - 1)

        def dfs(node):
            if not node:
                return -1

            if node == target:
                collect(node, k)
                return 0

            left_dist = dfs(node.left)
            if left_dist != -1:
                if left_dist + 1 == k:
                    ans.append(node.val)
                else:
                    collect(node.right, k - left_dist - 2)

                return left_dist + 1

            right_dist = dfs(node.right)
            if right_dist != -1:
                if right_dist + 1 == k:
                    ans.append(node.val)
                else:
                    collect(node.left, k - right_dist - 2)

                return right_dist + 1

            return -1

        dfs(root)
        return ans

```
