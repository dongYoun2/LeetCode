# submission: https://leetcode.com/problems/set-matrix-zeroes/submissions/2066641195/
# runtime: 0 ms (beats 100.00%), memory: 20.46 MB (beats 20.09%)
# 19 min
# solved using O(1) space (this solution's logic is exactly the same as the README.md's "Solution for the Follow-up Question: O(1) Space, Efficient Solution." refer to that for details and the complexity analysis.)


# after solving with the "07_13_2026.py" solution and looking at the follow-up question, i needed to solve this problem in O(1) space. first, i directly came up with using the first row and the first column to mark indices of rows and columns to be zeroed (from my memory since i had previously solved this problem). however, that leads to wrong solutions because since we are overwritting the first row and the column, we also need to record whether the first row and column can become zeroed in advance. after finding this case in the failing test cases, i was able to solve the problem in a constant space.

# two wrong submissions before finding the correct one, which is this solution:
# 1. https://leetcode.com/problems/set-matrix-zeroes/submissions/2066634641/
# 2. https://leetcode.com/problems/set-matrix-zeroes/submissions/2066635113/


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        first_row_zeros = first_col_zeros = False

        if matrix[0][0] == 0:
            first_row_zeros = first_col_zeros = True
        else:
            for j in range(n):
                if matrix[0][j] == 0:
                    first_row_zeros = True
                    break
            
            for i in range(m):
                if matrix[i][0] == 0:
                    first_col_zeros = True
                    break

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for r in range(1, m):
            if matrix[r][0] == 0:
                for j in range(n):
                    matrix[r][j] = 0
        
        for c in range(1, n):
            if matrix[0][c] == 0:
                for i in range(m):
                    matrix[i][c] = 0

        if first_row_zeros:
            for j in range(n):
                matrix[0][j] = 0
        
        if first_col_zeros:
            for i in range(m):
                matrix[i][0] = 0


# notes while solving:
# failed test case from prev implementation solving follow-up question
# 1  2  3  4
# 5  0  7  8
# 0  10 11 12
# 13 14 15 0
