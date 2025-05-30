# submission: https://leetcode.com/problems/construct-quad-tree/submissions/1649025698/
# runtime: 94 ms, memory: 18.4 MB

# 35 min
# TC: O(n^2 * log n), where n is the number of rows/columns in the grid.
# - total log n recursion depths.
# - at each level (or depth), the grid is divided into 4 quadrants. There are O(4^d) nodes at depth d in the worst case, and each processes a grid of size (n/2^d)^2.
# SC: O(log n). For the recursion stack. (Output storage doesn't count.)


# From LeetCode Top Interview 150 - Divide & Conquer

# The problem itself wasn't that hard, but I mistakenly thought `m_row = (s_row + e_row) // 2` is the right middle row index. So passing wrong indices failed the test cases, which took me a bit of time to debug.

# cf.) To compare with the optimized solution and see how it can be improved, refer to the markdown file.


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
        def is_all_same(s_row, e_row, s_col, e_col):
            first = grid[s_row][s_col]

            return all(grid[i][j] == first for i in range(s_row, e_row + 1) for j in range(s_col, e_col + 1))


        def build_quad_tree(s_row, e_row, s_col, e_col):
            if is_all_same(s_row, e_row, s_col, e_col):
                return Node(grid[s_row][s_col], True, None, None, None, None)

            m_row = (s_row + e_row) // 2    # left middle row index
            m_col = (s_col + e_col) // 2    # left middle column index

            top_left = build_quad_tree(s_row, m_row, s_col, m_col)
            top_right = build_quad_tree(s_row, m_row, m_col + 1, e_col)
            bottom_left = build_quad_tree(m_row + 1, e_row, s_col, m_col)
            bottom_right = build_quad_tree(m_row + 1, e_row, m_col + 1, e_col)

            return Node(1, False, top_left, top_right, bottom_left, bottom_right)


        n = len(grid)
        return build_quad_tree(0, n - 1, 0, n - 1)
