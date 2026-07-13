# submission: https://leetcode.com/problems/set-matrix-zeroes/submissions/2066626114/
# runtime: 7 ms (beats 58.88%), memory: 20.30 MB (beats 61.38%)
# 6 min
# this solution is the same as the "09_17_2025_better.py" and README.md's "Using `set` to Track Rows and Columns" approach. refer to them for details and the complexity analysis.


# i first considered setting -1 for cells of rows and columns to be zeroed, but noticing that values can be negative, i cannot use this approach. then, i came up with the idea to use two sets to mark the indices of rows and columns to be zeroed.


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        rows, cols = set(), set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for r in rows:
            for j in range(n):
                matrix[r][j] = 0
        
        for c in cols:
            for i in range(m):
                matrix[i][c] = 0
