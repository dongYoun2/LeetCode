# submission: https://leetcode.com/problems/search-a-2d-matrix/submissions/2055123378/
# runtime: 0 ms (beats 100.00%), memory: 19.58 MB (beats 38.06%)
# solved using binary search
# 17 min

# TC: O(log m + log n) -> O(log (m*n)) (required in the problem)
# SC: O(1)


# i thought of using binary saerch twice—one on the first column to find the correct row, then another on the found row to check if the target exists. to achieve this, i simply considered using a bisect module, but since it requires a 1d array as the argument, it will take O(m) to construct the first column as a 1d array, which results in a O(m + log (m*n)) time complexity in total. therefore, i manually implemented the binary search twice.

# cf.) in the code, i used `hi` as the found row index, but it's more correct to use `mid`, though after the first binary search, though `hi` and the `mid` becomes the same value.


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        # binary search on the first column
        lo, hi = 0, m-1        
        while lo <= hi:
            mid = lo + (hi-lo) // 2
            curr = matrix[mid][0]

            if target == curr:
                return True
            
            if target < curr:
                hi = mid - 1
            else:
                lo = mid + 1

        # row_idx = mid
        row_idx = hi

        # bianry search on the find row
        lo, hi = 0, n-1
        while lo <= hi:
            mid = lo + (hi-lo) // 2
            curr = matrix[row_idx][mid]

            if target == curr:
                return True
            
            if target < curr:
                hi = mid - 1
            else:
                lo = mid + 1

        return False
