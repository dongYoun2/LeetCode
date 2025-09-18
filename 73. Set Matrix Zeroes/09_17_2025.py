# submission: https://leetcode.com/problems/set-matrix-zeroes/submissions/1774458836/
# runtime: 7 ms, memory: 18.3 MB

# 8 min
# TC: O(m*n)
# SC: O(m*n)


# this is very straightforward approach, using the space complexity of O(m*n). Two follow-up questions optimize the space to first O(m+n) and then O(1).


from copy import deepcopy

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        matrix_cp = deepcopy(matrix)

        for r in range(m):
            for c in range(n):
                if matrix_cp[r][c] == 0:
                    for i in range(m):
                        matrix[i][c] = 0
                    for j in range(n):
                        matrix[r][j] = 0
