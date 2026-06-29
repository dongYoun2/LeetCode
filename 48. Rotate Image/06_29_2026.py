# submission: https://leetcode.com/problems/rotate-image/submissions/2050461252/
# runtime: 0 ms (beats 100.00%), memory: 19.28 MB (beats 68.88%)
# 20 min

# refer to the 03_28_2025.py for a complexity analysis.


# i remember that i can first transpose the matrix and then flip it horizontally to rotate the matrix. i forgot that i need to implement it in-place so i first coded with a list implementation as shown in the comments in the code below. however, once i realized the in-place requirement, i modified the code properly.


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 1. transpose
        # matrix = [cols for cols in zip(*matrix)]

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 2. flip based on y-axis
        # matrix = [row[::-1] for row in matrix]

        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
