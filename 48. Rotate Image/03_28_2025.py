# submission: https://leetcode.com/problems/rotate-image/submissions/1589360459/
# runtime: 0 ms (beats 100.00%), memory: 17.76 MB (beats 100.00%)
# 10 min

# TC: O(n^2 + n^2) -> O(n^2), where n is the length of the square matrix
# SC: O(1)


# First, I found out that I can solve the problem by rotating group of four cells. For example,

# 1. top-left corner element -> top-right corner element
# 2. top-right corner element -> bottom-right corner element
# 3. bottom-right corner element -> bottom-left corner element
# 4. bottom-left corner element -> top-left corner element

# We can do apply this algorithm for each and every layer of the matrix (from the outer most layer to the inner most layer). the submission for the above approach can be found here: https://leetcode.com/problems/rotate-image/submissions/1589360459/—Runtime: 0 ms (beats 100.00%), Memory: 17.76 MB (beats 100.00%)

# However, the above approach felt a bit confusing. Meanwhile, I realized that rotating 90 degrees clockwise is equivalent to:

# 1. Transposing the matrix
# 2. Flipping the matrix horizontally

# I assumed that this approach is easier to implement and straightforward, so I decided to go with this one.


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # in-place transpose
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # in-place horizontal flip
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
