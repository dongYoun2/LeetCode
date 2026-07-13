# submission: https://leetcode.com/problems/set-matrix-zeroes/submissions/1774464503/
# runtime: 0 ms (beats 100.00%), memory: 18.32 MB (beats 100.00%)
# solved using m+n space (two sets for marking rows and columns to be zeroed)

# 11 min
# TC: O(m*n)
# SC: O(m+n)


# once looking at the follow-up question, realized that m*n space solution is not optimal. so, with the hint that there's also a m+n space solution in the follow-up statement, i came up with the below solution. however, this is still not optimal. the optimal solution is the O(1) space approach, which can be found in the README.md.

# this approach solves the problem in three passes:
# 1. First pass: remember which rows/cols must be zero using two sets.
# 2. Second pass: zero all rows based on the rows set.
# 3. Third pass: zero all columns based on the cols set.


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        zero_rows, zero_cols = set(), set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        for row in zero_rows:
            for j in range(n):
                matrix[row][j] = 0

        for col in zero_cols:
            for i in range(m):
                matrix[i][col] = 0


# notes while solving:
# row_set: 0, 2
# col_set: 3, 2