[Problem Link](https://leetcode.com/problems/construct-quad-tree/)

## Optimized Recursive Solution

The solution below is an optimized recursive approach to construct a quad tree from a given grid. The key idea is to recursively divide the grid into quadrants until we **reach a base case of a 1x1 cell**, and then merge nodes if they are all leaves with the same value.

Unlike the previous solution `05_30_2025.py`, this version does not check for uniformity of the entire grid at each level, but rather checks only the quadrants. This reduces redundant scanning of the grid.


In the leetcode submission, `05_30_2025.py` solution is a little faster due to two reasons:
1. The full scanning time is negligible since the maximum grid size is only $2^6 \times 2^6$ given in the problem conditions.
2. This optimized solution has a higher recursion overhead because it has more (recursive)function calls than the `05_30_2025.py` code. (No pruning is done here.)

However, the optimized approach will become more efficient for larger grids as we can see by comparing the time complexity of both approaches.
<br>


- [Submission](https://leetcode.com/problems/construct-quad-tree/submissions/1649052035/) (Runtime: 107 ms, Memory: 18.7 MB)
- TC: $O(n^2)$, where $n$ is the length of the grid.
  - In the worst case, total number of nodes is $1 + 4 + 4^2 + \cdots + 4^{\log n} \approx O(n^2)$. This can be intuitvely thought of as where each 1 x 1 cells is a leaf node, which requires processing all nodes in the grid.
- SC: $O(\log n)$. For the recursion stack. (Output storage doesn't count.)
<br>

```python
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def build_quad_tree(grid, s_row, s_col, length):
            # Base case: 1x1 grid
            if length == 1:
                return Node(grid[s_row][s_col] == 1, True, None, None, None, None)

            half = length // 2

            # Recursive calls to sub-quadrants
            top_left = build_quad_tree(grid, s_row, s_col, half)
            top_right = build_quad_tree(grid, s_row, s_col + half, half)
            bottom_left = build_quad_tree(grid, s_row + half, s_col, half)
            bottom_right = build_quad_tree(grid, s_row + half, s_col + half, half)

            # Merge if all are leaves and have same value
            if top_left.isLeaf and top_right.isLeaf and bottom_left.isLeaf and bottom_right.isLeaf and (top_left.val == top_right.val == bottom_left.val == bottom_right.val):
                return Node(top_left.val, True, None, None, None, None)

            # Otherwise, return internal node
            return Node(True, False, top_left, top_right, bottom_left, bottom_right)


        return build_quad_tree(grid, 0, 0, len(grid))

```