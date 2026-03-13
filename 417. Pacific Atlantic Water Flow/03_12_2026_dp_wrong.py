# submission: https://leetcode.com/problems/pacific-atlantic-water-flow/submissions/1946514403/
# wrong solution
# spent 56 min, but could not solve it


# i attempted this problem with a DP approach, but it's a wrong approach. this is a graph-traversal problem; flood fill problem. typically, it can be solved with a BFS or DFS approach.

# the main reason DP fails here is because the dp table pacific[i][j], which indicates whether the cell (i,j) can reach the pacific ocean, does not have a valid one-pass dependency order, though it performs one forward (top-left -> bottom-right) sweep and one backward (bottom-right -> top-left) sweep. at fist, i only performed one forward sweep (submission: https://leetcode.com/problems/pacific-atlantic-water-flow/submissions/1946509489/), but then realizing from the failed test case where the flow path to pacific ocean can include moving down or right, i performed additional backward sweep to fix this issue. however, this is still not enough because there can be cyclic dependencies between cells. in these cases, there is no order where we can finalize one first. thus, information may need to propagate through a long path with many turns, and one or two scans do not guarantee reaching a fixed point (convergence).

# the deeper issue is that the DP algorithm assumes the global optimal solution can be achieved by solving the local subproblems in a valid order. however, in this problem, the dependencies between cells are not linear. rather, this problem has a global existence-of-path property, not a local one tied to a scan order.

# so, my takeaway is that if there's a 4-directional dependency (or movement) between cells, it's generally a graph-traversal (BFS or DFS) problem.

# cf.) a little disappointed that i couldn't solve this; should be able to solve this type of problem. i actually thought of using BFS starting from the borders of the pacific and atlantic, but something was confused and gave up while writing up the code.


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]

        # 1. check cells that can flow to pacific
        for c in range(n):
            pacific[0][c] = True

        for r in range(m):
            pacific[r][0] = True

        # top-left -> bottom-right
        for i in range(1, m):
            for j in range(1, n):
                top = pacific[i-1][j] and (heights[i][j] >= heights[i-1][j])
                left = pacific[i][j-1] and (heights[i][j] >= heights[i][j-1])
                pacific[i][j] = top or left

        # bottom-right -> top-left
        for i in range(m-1, 0, -1):
            for j in range(n-1, 0, -1):
                if not pacific[i][j]:
                    if i == m-1 and j != n-1:   # bottom row except the corner cell
                        pacific[i][j] = pacific[i][j+1] and (heights[i][j] >= heights[i][j+1])
                    elif i != m-1 and j == n-1: # right-most col except the corner cell
                        pacific[i][j] = pacific[i+1][j] and (heights[i][j] >= heights[i+1][j])
                    elif 0 <= i < m-1 and 0 <= j < n-1:
                        bottom = pacific[i+1][j] and (heights[i][j] >= heights[i+1][j])
                        right = pacific[i][j+1] and (heights[i][j] >= heights[i][j+1])
                        pacific[i][j] = bottom or right


        # 2. check cells that can flow to atlantic
        for c in range(n):
            atlantic[m-1][c] = True

        for r in range(m):
            atlantic[r][n-1] = True
        
        # bottom-right -> top-left
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                bottom = atlantic[i+1][j] and (heights[i][j] >= heights[i+1][j])
                right = atlantic[i][j+1] and (heights[i][j] >= heights[i][j+1])
                atlantic[i][j] = bottom or right
        
        # top-left -> bottom-right
        for i in range(m):
            for j in range(n):
                if not atlantic[i][j]:
                    if i == 0 and j != 0:   # top row except the corner cell
                        atlantic[i][j] = atlantic[i][j-1] and (heights[i][j] >= heights[i][j-1])
                    elif i != 0 and j == 0: # left-most col except the corner cell
                        atlantic[i][j] = atlantic[i-1][j] and (heights[i][j] >= heights[i-1][j])
                    elif 1 <= i < m and 1 <= j < n:
                        top = atlantic[i-1][j] and (heights[i][j] >= heights[i-1][j])
                        left = atlantic[i][j-1] and (heights[i][j] >= heights[i][j-1])
                        atlantic[i][j] = top or left

        return [(i, j) for i in range(m) for j in range(n) if pacific[i][j] and atlantic[i][j]]
