# submission: https://leetcode.com/problems/pacific-atlantic-water-flow/submissions/1946622769/
# wrong solution
# spent 1 hr 23 min (including the time writing 03_12_2026_dp_wrong.py), but failed to solve it


# after attempting with DP (03_12_2026_dp_wrong.py), and giving up using a BFS starting with the borders of the pacific and atlantic (but, this approach was actually the correct one lol..), i then tried with DFS. however, i performed DFS on every cell, which makes the solution incorrect or too slow.

# i first initialized all cells of cache to [False, False] (submission: https://leetcode.com/problems/pacific-atlantic-water-flow/submissions/1946615806/). however, this is incorrect becuase border cells are either reachable to pacific, atlantic, or both (top-right and bottom-left corners). so, i edited the code like below, but it still failed; this is becuae i maintain a global `visited` set throughout the all DFS calls. i fixed this issue with ChatGPT, and now it's getting TLE (submission: https://leetcode.com/problems/pacific-atlantic-water-flow/submissions/1946644752/). therefore, we cannot guarantee that this submission is correct, but according to ChatGPT again, this is still wrong becauase when a cycle happens, especially on equal-height cells, dfs function returns cache[y][x] before it has been fully computed. at the moment, `cache[y][x]` may still be [False, False], not because the cell truly cannot reach either ocean, but because computation is still in progress.

# anyhow, the approach to perform DFS on every cell is incorrect. it's much cleaner to perform DFS (or BFS) starting from the borders of the pacific and atlantic, and then check if the cell can reach both oceans. refer to the README.md for the correct solutions.


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        is_pacific = lambda r, c: r < 0 or c < 0
        is_atlantic = lambda r, c: r >= m or c >= n

        cache = [[[False, False] for _ in range(n)] for _ in range(m)]

        # top row
        for c in range(n):
            cache[0][c][0] = True

        # left-most col
        for r in range(m):
            cache[r][0][0] = True

        # bottom row
        for c in range(n):
            cache[m-1][c][1] = True
        
        # right-most col
        for r in range(m):
            cache[r][n-1][1] = True
        
        dys = [-1, 0, 1, 0]
        dxs = [0, 1, 0, -1]

        is_valid = lambda r, c: 0 <= r < m and 0 <= c < n
        visited = set()


        def dfs(y, x):
            if (y, x) in visited:
                return cache[y][x]

            visited.add((y, x))
            ret_pacific = ret_atlantic = False

            for dy, dx in zip(dys, dxs):
                ny, nx = y + dy, x + dx
                
                if is_valid(ny, nx) and heights[y][x] < heights[ny][nx]:
                    continue

                if not is_pacific(ny, nx) and not is_atlantic(ny, nx):
                    tmp_pacific, tmp_atlantic = dfs(ny, nx)
                    ret_pacific = ret_pacific or tmp_pacific
                    ret_atlantic = ret_atlantic or tmp_atlantic
                
                if is_pacific(ny, nx):
                    ret_pacific = True
                
                if is_atlantic(ny, nx):
                    ret_atlantic = True

            cache[y][x] = [ret_pacific, ret_atlantic]
            return cache[y][x]


        return [(i, j) for i in range(m) for j in range(n) if all(dfs(i, j))]
