# problem: https://leetcode.com/problems/search-a-2d-matrix/
# submission: https://leetcode.com/problems/search-a-2d-matrix/submissions/

# 15 min
# TC: O(log(m*n)) (required in the problem)
# SC: O(1)

# The input matrix is sorted in non-descending order, so we can use binary search to find whether the target exists in the matrix. (Since I am solving the problem based on the algorithm type, I knew that I had to use binary search.) We cannot use python bisect module since it rquires a 1d array as the argument.

# In the beginning, I came up with an approach to perform a binary search on the first column to find the correct row that "can" contain the target value, then perform a binary search again on that row. Since the time complexity for this is O(log m + log n), I thought of another algorithm that runs a binary search on the entire matrix as a 1d array, which the code below implements. However, by the time writing this comment, I realized that O(log m + log n) is the same as O(log (m*n)), so I could have used the first approach as well, LOL.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        s_idx = 0
        e_idx = (m - 1) * n + (n - 1)

        convert_idx_1d_to_2d = lambda idx: divmod(idx, n)

        while s_idx <= e_idx:
            med = s_idx + (e_idx - s_idx) // 2 # prevent overflow
            med_y, med_x = convert_idx_1d_to_2d(med)
            med_val = matrix[med_y][med_x]

            if med_val == target:
                return True

            if target < med_val:
                e_idx = med - 1
            else:
                s_idx = med + 1

        return False
