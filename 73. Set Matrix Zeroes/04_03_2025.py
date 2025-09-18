# problem: https://leetcode.com/problems/set-matrix-zeroes/
# submission: https://leetcode.com/problems/set-matrix-zeroes/submissions/1595697769/
# actually, this code should be regarded as wrong since it breakes the fact that the matrix is of type int given in the problem statement!

# 7 min
# TC: O(m*n*(m+n) + (m*n)) -> O(m*n*(m+n))
# SC: O(1)

# I knew that this was a matrix problem since I am currently solving problems based on the algorithm types.

# As "in-place" changes are required, I tried to use a constant space, which also meets a follow-up question 2's criteria, and the below is the solution I came up with. Although the space complexity is O(1), time complexity is suboptimal. Other approaches can solve the problem in O(m*n) time complexity with either O(m+n) space complexity or O(1) space complexity. Refer to the markdown file and LeetCode Editorial for more details.

# cf.) In addition, the below approach works since Python is an untyped language, so I was able to assign 'a' to the matrix even though it is of type int (in the type hint). Even assigning an integer other than values that matrix[i][j] could take is impossible since the range of the value is [-2^31, 2^31-1], which is exactly a 4 byte integer. Therefore, I need to use a different approach to mark the cells in other languages.


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for k in range(n):
                        if matrix[i][k] != 0:
                            matrix[i][k] = 'a'

                    for k in range(m):
                        if matrix[k][j] != 0:
                            matrix[k][j] = 'a'

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 'a':
                    matrix[i][j] = 0

